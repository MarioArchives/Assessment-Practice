"""
Challenge 9 — Async Process Supervisor
----------------------------------------
Implement an async process supervisor that manages a pool of subprocesses.

Requirements:
  - `start()` — launch `workers` copies of `command`
  - Each worker is monitored; if it exits unexpectedly it is restarted
  - Track the restart count per worker
  - Once a worker has been restarted `max_restarts` times, stop restarting it
  - `status()` — return a list of `WorkerStatus` objects (one per worker slot)
  - `stop()` — send SIGTERM to all running workers and await their exit

WorkerStatus fields:
  worker_id : int
  pid       : int | None  (None if not running)
  restarts  : int
  running   : bool
"""

import asyncio
from asyncio.subprocess import Process
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class WorkerStatus:
    worker_id: int
    pid: Optional[int]
    restarts: int
    running: bool
    process: Optional[Process]
    monitor: Optional[Process]

    def __str__(self) -> str:
        return f"worker id: {self.worker_id} \nrestarts count: {self.restarts} \nrunning: {self.running} \npid: {self.pid}"


class ProcessSupervisor:
    def __init__(self, command: List[str], workers: int = 1, max_restarts: int = 3):
        self.commands = command
        self._worker_pool = {}
        for worker_id in range(workers):
            worker_status = WorkerStatus(
                worker_id=worker_id,
                pid=0,
                restarts=0,
                running=False,
                process=None,
                monitor=None,
            )
            self._worker_pool[worker_id] = worker_status

        self.max_restarts = max_restarts

    async def _monitor(self, worker_id: int) -> None:
        if (
            restarts_not_reached := self._worker_pool[worker_id].restarts
            <= self.max_restarts
        ):
            while restarts_not_reached:
                await self._worker_pool[worker_id].process.wait()
                self._worker_pool[worker_id].running = False
                if self._worker_pool[worker_id].restarts < self.max_restarts:
                    self._worker_pool[worker_id].restarts += 1
                    await self.start_worker(worker_id)
                restarts_not_reached = (
                    self._worker_pool[worker_id].restarts < self.max_restarts
                )
        else:
            self._worker_pool[worker_id].running = False

    async def start_worker(self, worker_id: int) -> None:
        if (
            restarts_not_reached := self._worker_pool[worker_id].restarts
            <= self.max_restarts
        ):
            while restarts_not_reached:
                try:
                    worker_process = await asyncio.create_subprocess_exec(
                        *self.commands
                    )
                    self._worker_pool[worker_id].pid = worker_process.pid
                    self._worker_pool[worker_id].running = True
                    self._worker_pool[worker_id].process = worker_process

                    if self._worker_pool[worker_id].monitor:
                        self._worker_pool[worker_id].monitor.cancel()

                    self._worker_pool[worker_id].monitor = asyncio.create_task(
                        self._monitor(worker_id)
                    )
                    break
                except Exception:
                    self._worker_pool[worker_id].restarts += 1
                    self._worker_pool[worker_id].running = False
                restarts_not_reached = (
                    self._worker_pool[worker_id].restarts <= self.max_restarts
                )

        else:
            self._worker_pool[worker_id].running = False

    async def start(self) -> None:
        """Launch all workers and begin monitoring them."""
        for worker_id in self._worker_pool.keys():
            await self.start_worker(worker_id)

    def status(self) -> List[WorkerStatus]:
        """Return the current status snapshot of all worker slots."""
        return [self._worker_pool[workerid] for workerid in self._worker_pool.keys()]

    async def stop(self) -> None:
        """Gracefully stop all workers and cancel monitor tasks."""
        # your implementation here
        for _, worker_status in self._worker_pool.items():
            worker_status.monitor.cancel()
            if worker_status.running:
                worker_status.process.terminate()
                await worker_status.process.wait()
                worker_status.running = False
                worker_status.pid = 0
                worker_status.process = None
                worker_status.restarts = 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


async def test_starts_correct_number_of_workers():
    sup = ProcessSupervisor(command=["sleep", "10"], workers=3)
    await sup.start()
    await asyncio.sleep(0.2)
    statuses = sup.status()
    assert len(statuses) == 3
    assert all(s.running for s in statuses), "All workers should be running"
    assert all(s.running for s in statuses), "All workers should be running"
    await sup.stop()


async def test_restarts_exited_worker():
    sup = ProcessSupervisor(command=["sleep", "0.1"], workers=1, max_restarts=5)
    await sup.start()
    await asyncio.sleep(0.6)  # worker should die and be restarted several times
    statuses = sup.status()
    assert statuses[0].restarts >= 1, "Worker should have been restarted at least once"
    await sup.stop()


async def test_stop_terminates_all_workers():
    sup = ProcessSupervisor(command=["sleep", "5"], workers=2)
    await sup.start()
    await asyncio.sleep(0.1)
    await sup.stop()
    statuses = sup.status()
    assert all(not s.running for s in statuses), "All workers should be stopped"


async def test_max_restarts_honoured():
    sup = ProcessSupervisor(command=["sleep", "0.05"], workers=1, max_restarts=2)
    await sup.start()
    await asyncio.sleep(1.5)
    statuses = sup.status()
    assert statuses[0].restarts <= 2, "Should not exceed max_restarts"
    print(statuses)
    assert not statuses[0].running, "Worker should have given up after max_restarts"
    await sup.stop()


async def test_worker_ids_are_unique():
    sup = ProcessSupervisor(command=["sleep", "5"], workers=4)
    await sup.start()
    await asyncio.sleep(0.1)
    ids = [s.worker_id for s in sup.status()]
    assert len(set(ids)) == 4, "Worker IDs must be unique"
    await sup.stop()


if __name__ == "__main__":
    asyncio.run(test_starts_correct_number_of_workers())
    asyncio.run(test_restarts_exited_worker())
    asyncio.run(test_stop_terminates_all_workers())
    asyncio.run(test_max_restarts_honoured())
    asyncio.run(test_worker_ids_are_unique())
    print("All tests passed!")
