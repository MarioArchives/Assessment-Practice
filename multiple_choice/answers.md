# Answer Key

## Python MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **B**  | `y = x` creates an alias, not a copy. Both names point to the same list object, so `y.append(4)` mutates `x`. |
| 2  | **B**  | Mutable default arguments are evaluated once at function definition. The same list object is reused across calls. |
| 3  | **C**  | The GIL is released during I/O operations (and other blocking syscalls), allowing threads to overlap. It is NOT released for CPU-bound work. |
| 4  | **B**  | `yield from` delegates to a sub-generator/iterable, transparently forwarding values, `send()`, and `throw()` calls. |
| 5  | **B**  | CPython interns small integers (typically -5 to 256). `256 is 256` → True. `257` creates two separate objects → False. |
| 6  | **B**  | `nonlocal x` binds `x` to the enclosing function's scope. `global` would bind to module scope. |
| 7  | **B**  | `__str__` is for readable end-user display. `__repr__` should be unambiguous and ideally `eval(repr(obj)) == obj`. |
| 8  | **B**  | Python MRO (C3 linearisation): D → B → C → A. `D.method()` calls `B.method()` which calls `super()` → `C.method()` which calls `super()` → `A.method()`. Result: `"B" + "C" + "A"` = `"BCA"`. |
| 9  | **B**  | `lru_cache` requires hashable arguments. Lists are unhashable, so `f([1, 2])` raises `TypeError`. |
| 10 | **A**  | `__slots__` replaces the per-instance `__dict__` with a fixed set of slots, reducing memory and preventing arbitrary attribute creation. |
| 11 | **B**  | Generators are single-pass iterators. Once exhausted, re-iterating yields nothing. |
| 12 | **B**  | `raise X from Y` sets `X.__cause__ = Y`. So `e.__cause__` is the `TypeError` instance. |
| 13 | **B**  | `gather` returns results in the same order as inputs. `wait` returns `(done, pending)` sets with no guaranteed order. |
| 14 | **C**  | `frozen=True` makes the dataclass immutable. Attempting `p.x = 10` raises `dataclasses.FrozenInstanceError` (a subclass of `AttributeError`). |
| 15 | **B**  | `__get__(self, obj, objtype)` is called when the attribute is accessed. `__set__` is for assignment, `__getattr__` is a fallback for missing attributes. |
| 16 | **A**  | The walrus operator assigns and simultaneously evaluates to the assigned value, making it usable inline in conditions, comprehensions, etc. |
| 17 | **C**  | Python 3.7+ dicts preserve insertion order. Re-assigning an existing key does not change its position — `[1, 2]`. |
| 18 | **B**  | `list.__contains__` is O(n) linear scan. `set.__contains__` is O(1) average (hash lookup). |
| 19 | **A**  | A context manager requires `__enter__` (returns the value bound by `as`) and `__exit__` (handles cleanup and suppresses exceptions if it returns True). |
| 20 | **A** (with caveat per D) | The final `len(results)` is deterministically `5` because `join()` ensures all threads complete before the `print`. However, the *values* inside `results` are in non-deterministic order. If the question asks only about `len`, the answer is **A**. If it asks about values too, **D** is the most precise answer. |
| 21 | **A** | `__new__` allocates and returns the instance; `__init__` only initialises it after creation. Used in singletons, immutable types (e.g. `str` subclasses), and custom allocation. |
| 22 | **B** | `partial(power, exp=2)` pre-fills `exp=2`; `square(3)` calls `power(3, exp=2)` = 3² = 9. |
| 23 | **C** | `copy.copy()` creates a new container but shares references to nested objects. `deepcopy()` recursively copies all nested objects. |
| 24 | **D** | When Python sees `x = 20` anywhere inside `f()`, `x` is treated as a local throughout the function. Reading it before the assignment raises `UnboundLocalError`. |
| 25 | **A** | `Optional[str]` is shorthand for `Union[str, None]` — the standard way to express a nullable type. |
| 26 | **B** | Python's TimSort algorithm is stable by specification (guaranteed since Python 2.2). Equal elements preserve their relative input order. |
| 27 | **C** | `@classmethod` always receives the class object as `cls`. `@staticmethod` is a plain function — no implicit first argument. |
| 28 | **D** | The metaclass `__new__` injects `greeting = 'hello'` into the class namespace before the class object is created, so `MyClass.greeting` resolves to `'hello'`. |
| 29 | **A** | `isinstance(x, T)` returns `True` for instances of `T` or any subclass. `type(x) == T` is an exact type match and returns `False` for subclass instances. |
| 30 | **B** | `Exception` is the base of all "normal" exceptions. `BaseException` also includes `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`. |
| 31 | **C** | Generators are single-pass. Once all `yield` statements are exhausted, any further `next()` call raises `StopIteration`. |
| 32 | **D** | `__post_init__` is called by the dataclass-generated `__init__` as its final step, after all fields have been set. |
| 33 | **A** | `@contextmanager` splits at `yield`: code before `yield` runs on enter, the yielded value is bound by `as`, code after `yield` runs on exit. |
| 34 | **B** | `multiprocessing` spawns separate OS processes, each with its own GIL, enabling true parallel CPU execution. `threading` is limited by the GIL for CPU-bound work. |
| 35 | **C** | `__all__` is a list of names exported by `from module import *`. It does not affect `import module` or direct `module.attr` access. |
| 36 | **D** | IEEE 754 cannot represent 0.1 or 0.2 exactly. `0.1 + 0.2` evaluates to `0.30000000000000004`, which is not equal to `0.3`. |
| 37 | **A** | `defaultdict(list)` calls `list()` (the default factory) for missing keys, returning `[]`. No `KeyError` is raised. |
| 38 | **B** | `a[:]` creates a shallow copy. Rebinding `b[0] = 99` only affects `b`'s slot; `a[0]` remains `1`. |
| 39 | **C** | All lambdas close over the *variable* `i`, not its value at creation time. After the loop, `i == 2`, so all three lambdas return `2`. |
| 40 | **D** | `B` inherits `val` from `A`; it is the *same* list object. `B.val.append(1)` mutates the shared list, so `A.val` also shows `[1]`. |
| 41 | **A** | The `None` sentinel pattern is the idiomatic fix. `list()` as a default still evaluates once at definition — same problem. Type annotations do not affect runtime behaviour. |
| 42 | **B** | `yield from` is more than syntactic sugar: it also forwards `send()` values and `throw()` calls bidirectionally between the outer caller and the sub-generator, enabling coroutine chaining. |
| 43 | **C** | Because `count += 1` appears in the function body, Python treats `count` as a local variable throughout. Reading it before the assignment raises `UnboundLocalError`. |
| 44 | **D** | `sys.exit()` raises `SystemExit`, which inherits from `BaseException` (not `Exception`). The first `except Exception` clause is skipped; `except BaseException` catches it. |
| 45 | **A** | `Pool.map` distributes work across processes and collects results **in the same order as the input iterable**, regardless of which worker finished first. |
| 46 | **B** | `os.fork()` gives each child process a private copy-on-write address space. Threads created by `threading.Thread` share the parent's heap, stack segments, and globals. |
| 47 | **C** | Neither `outer` nor `inner` assigns to `x` — they only call `x.append()`, which mutates the existing object. No `UnboundLocalError` is triggered because no binding occurs. |
| 48 | **D** | `KeyboardInterrupt` (and `SystemExit`, `GeneratorExit`) inherit from `BaseException`. A bare `except Exception:` clause will never catch them, which is usually the desired behaviour. |
| 49 | **A** | `nonlocal` targets the nearest enclosing scope that is not global. It makes assignment (`=`, `+=`, etc.) modify the outer variable rather than create a new local binding. |
| 50 | **B** | `make_counter()` creates a closure over `count`. Each call to `c()` executes `nonlocal count; count += 1`, incrementing the shared variable: 1, 2, 3. |

> **Q20 note:** In practice the answer expected is **A** — `len(results) == 5` is guaranteed due to the `join()` barrier. Answer **D** is also defensible since `list.append` is not atomically safe across the GIL in all Python implementations (though CPython's GIL does make it safe in practice).

---

## Kubernetes MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **B**  | A Pod is the atomic unit. It wraps one or more containers that share network and storage. |
| 2  | **B**  | A Deployment manages a ReplicaSet and adds rolling-update strategy, rollback history, and pause/resume. |
| 3  | **C**  | ClusterIP allocates a virtual IP reachable only within the cluster. NodePort and LoadBalancer add external access. |
| 4  | **B**  | Secrets are base64-encoded (and optionally encrypted at rest) objects intended for sensitive data. ConfigMaps are for non-sensitive config. |
| 5  | **B**  | etcd is the backing store for all Kubernetes state. Every object (pods, services, configs) is persisted there. |
| 6  | **B**  | A DaemonSet ensures one Pod per node (or per selected node). Typical use: log collectors, node exporters, network agents. |
| 7  | **B**  | Liveness: if probe fails, kubelet restarts the container. Readiness: if probe fails, the pod is removed from Service endpoints (no traffic) but not restarted. |
| 8  | **B**  | `Role` is scoped to a single namespace. `ClusterRole` can grant permissions on cluster-scoped resources (nodes, PVs) and across all namespaces. |
| 9  | **B**  | A `NoSchedule` taint prevents the scheduler from placing pods without a matching toleration. Existing pods are not evicted (use `NoExecute` for eviction). |
| 10 | **B**  | `Retain` means the PV is released (no longer bound) but the data and PV object remain. An admin must manually delete or re-bind it. |
| 11 | **C**  | A `Job` runs pods to completion. `CronJob` wraps a Job for scheduled execution. |
| 12 | **B**  | Init containers run sequentially to completion before any app containers start. Useful for waiting on dependencies, seeding data, etc. |
| 13 | **C**  | `kubectl apply` is declarative: it computes a diff and patches the existing resource. `kubectl create` fails if the resource already exists. |
| 14 | **B**  | `kubectl rollout history deployment/<name>` lists revision history. Use `--revision=N` to see details of a specific revision. |
| 15 | **B**  | The default HPA metric is CPU utilization (as a percentage of requested CPU). Custom and external metrics require additional metric server configuration. |
| 16 | **B**  | Requests are used by the scheduler to find a node with sufficient capacity. Limits are enforced at runtime by the container runtime (cgroups). |
| 17 | **B**  | A NetworkPolicy that selects pods but specifies no `ingress` rules denies all ingress. The mere existence of a matching NetworkPolicy changes the default from "allow all" to "deny all" for that direction. |
| 18 | **B**  | `values.yaml` holds default values. Templates reference them via `{{ .Values.key }}`. Users override them with `-f custom-values.yaml` or `--set`. |
| 19 | **B**  | `port-forward` tunnels traffic from a local port to a port on a pod (or service), entirely within the `kubectl` process. No Service is created. |
| 20 | **B**  | StatefulSets provide stable DNS hostnames (`pod-0`, `pod-1`, ...), ordered rolling updates, and per-pod PVCs that survive rescheduling. |
| 21 | **A** | `-i` keeps stdin open; `-t` allocates a TTY. `--` separates kubectl flags from the container command. `kubectl attach` connects to an existing process, not a new shell. |
| 22 | **B** | Guaranteed: all containers have `requests == limits`. Burstable: some have requests/limits set. BestEffort: no requests or limits at all. |
| 23 | **C** | `Succeeded` is the terminal phase for Pods where all containers exited with code 0. `Completed` is not a valid Pod phase name. |
| 24 | **D** | A PDB sets `minAvailable` or `maxUnavailable`. The API server enforces this during voluntary disruptions (node drain, rolling updates). |
| 25 | **A** | `CronJob` wraps a `Job` spec with a `spec.schedule` field using standard cron syntax (e.g. `"0 * * * *"`). |
| 26 | **B** | Guaranteed QoS requires *every* container in the Pod to have `requests.cpu == limits.cpu` and `requests.memory == limits.memory`. |
| 27 | **C** | `rollout undo` reverts to the previous revision in the Deployment's history (stored as old ReplicaSets). Use `--to-revision=N` for a specific revision. |
| 28 | **D** | `emptyDir` is ephemeral: created when the Pod is assigned to a node, shared by all containers in the Pod, deleted when the Pod terminates or is evicted. |
| 29 | **A** | ConfigMaps store non-sensitive data as key-value pairs. Use Secrets for sensitive data (passwords, tokens, keys). |
| 30 | **B** | The Metrics Server scrapes resource metrics from kubelets and exposes them via the `metrics.k8s.io` API. `kubectl top` queries this API. |
| 31 | **C** | `sessionAffinity: ClientIP` makes kube-proxy consistently route requests from the same source IP to the same Pod. Default timeout is 10800 s. |
| 32 | **D** | The scheduler watches for `Pending` Pods with `spec.nodeName` unset, scores candidate nodes, and sets `spec.nodeName` via the API server. |
| 33 | **A** | `kubectl cp` uses `tar` to stream files between the local machine and a container. It requires `tar` to be available inside the container. |
| 34 | **B** | `ResourceQuota` enforces aggregate namespace limits: total CPU, memory, number of Pods, Services, PVCs, etc. `LimitRange` controls individual Pod/container limits. |
| 35 | **C** | `kubectl create` is imperative and returns an error if the resource exists. `kubectl apply` performs a three-way merge (last-applied + live state + new spec). |
| 36 | **D** | `cordon` only sets the `unschedulable` taint. `drain` also evicts existing Pods gracefully, respecting PDBs and termination grace periods. |
| 37 | **A** | A sidecar shares the Pod's network namespace and optionally volumes, enabling augmentation without modifying the main container image. |
| 38 | **B** | `kubectl apply` records the last-applied config in an annotation, enabling future three-way merges. `kubectl create` does not track this and fails on re-application. |
| 39 | **C** | `restartPolicy` can be `Always` (Deployment default), `OnFailure` (Job default), or `Never`. It applies to all containers in the Pod. |
| 40 | **D** | kube-proxy watches Services and EndpointSlices and translates Service VIPs into iptables/ipvs rules, load-balancing traffic to backend Pod IPs. |
| 41 | **A** | The readiness probe controls Service endpoint membership, not container lifecycle. A failed readiness probe pulls the Pod from rotation; a failed liveness probe triggers a restart. |
| 42 | **B** | `reclaimPolicy: Delete` provisions and deletes storage in lockstep with the PVC. Cloud-provisioned disks (EBS, GCE PD) are deleted automatically. Use `Retain` to keep data after PVC deletion. |
| 43 | **C** | `Succeeded` and `Failed` are the two terminal Pod phases. `Failed` means at least one container exited with a non-zero code and `restartPolicy` prevents a retry. |
| 44 | **D** | The controller-manager runs all built-in controllers (Deployment, ReplicaSet, Job, Node, etc.) in a single binary. The Deployment controller reconciles replica counts by creating/deleting ReplicaSets. |
| 45 | **A** | `ResourceQuota` enforces hard limits on total namespace consumption. `LimitRange` sets per-object defaults and bounds — e.g. if a Pod requests no CPU, `LimitRange` injects a default. Both can coexist. |
| 46 | **B** | kube-proxy (iptables mode) inserts DNAT rules: packets to `ClusterIP:port` are rewritten to a random backend Pod IP before routing. In IPVS mode, a virtual server handles the load balancing. |
| 47 | **C** | The presence of a NetworkPolicy selecting a pod activates the deny-by-default posture for the direction(s) specified. With no `ingress` rules listed, all ingress is denied. Egress is unaffected unless `egress` rules are also absent. |
| 48 | **D** | Init containers run serially in the order they are listed. Each must exit with code 0 before the next starts. If any init container fails, the Pod restarts (subject to `restartPolicy`). |
| 49 | **A** | `requests != limits` (128Mi vs 256Mi) makes this Burstable. Guaranteed requires every container to have equal requests and limits for both CPU and memory. BestEffort requires none. |
| 50 | **B** | `kubectl describe` adds: recent Events (scheduling, image pull, probe failures), container `State` and `Last State`, `Conditions`, volume mounts, and resource requests/limits — essential for debugging. |

---

## Linux MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **A** | The kernel is the OS core: it schedules processes on CPUs, manages virtual memory, handles I/O, and exposes privileged services via the system call interface. |
| 2  | **B** | Kernel space code runs in CPU ring 0 with full hardware access. User-space code runs in ring 3; it must trap into the kernel via syscalls to perform privileged operations. |
| 3  | **C** | The MMU translates each process's virtual addresses to physical RAM pages. Each process sees an isolated virtual address space. |
| 4  | **D** | Namespaces partition kernel resources: PID namespace (isolated PID 1), net namespace (isolated network stack), mnt namespace (isolated filesystem tree), etc. Containers combine several namespaces. |
| 5  | **A** | Linux is monolithic: the kernel image includes core subsystems (scheduler, VFS, network stack, most drivers). Loadable Kernel Modules (LKMs) allow drivers to be inserted/removed without rebooting. |
| 6  | **B** | The shell (bash, zsh, sh, fish) is a user-space REPL. It parses commands, sets up pipes/redirections, and uses `fork()` + `exec()` to launch external programs. |
| 7  | **C** | `PATH` is a colon-separated list. When you type `ls`, the shell searches each directory left-to-right until it finds an executable named `ls`. |
| 8  | **D** | `source` (or `.`) executes the file in the *current* shell process, so aliases, functions, and variable assignments take effect immediately. Running it as a script would execute in a subshell. |
| 9  | **A** | Examples: `cd`, `export`, `source`, `echo`, `alias`. Built-ins can modify shell state (e.g. `cd` changes the working directory); external commands cannot since they run in a child process. |
| 10 | **B** | The shell performs a linear left-to-right search and stops at the first match. `which <cmd>` shows which directory wins. |
| 11 | **C** | systemd is PID 1 on most major distros (Ubuntu, Debian, RHEL, Arch, Fedora). It uses unit files to declare service dependencies, starts them in parallel, and manages the cgroup hierarchy. |
| 12 | **D** | `--now` combines `enable` (create boot symlinks) and `start` (start immediately) in a single command. |
| 13 | **A** | `journalctl -u <service>` queries the binary journal filtered to that unit. Useful flags: `-f` (follow), `-e` (jump to end), `--since "1 hour ago"`. |
| 14 | **B** | `Type=oneshot` is for "run and exit" services (e.g. sysctl setup, DB migrations). systemd marks the service `active (exited)` once the process exits with code 0. |
| 15 | **C** | `multi-user.target` ≈ runlevel 3: networking, multiple users, no display manager. `graphical.target` ≈ runlevel 5 and depends on `multi-user.target`. |
| 16 | **D** | User programs cannot access hardware directly. They invoke the kernel via syscalls (e.g. `read`, `write`, `open`, `fork`). The CPU switches from user mode to kernel mode via a trap/software interrupt. |
| 17 | **A** | `fork()` creates a child as a near-identical copy of the parent. The underlying Linux syscall is `clone()`, also used by `pthread_create()` to share address space. `exec()` replaces the process image, it does not create one. |
| 18 | **B** | `strace -p <pid>` attaches to a process and prints every syscall invocation with arguments and return values. Essential for debugging "black box" binaries. |
| 19 | **C** | The VFS layer presents a uniform interface. Block/character devices, named pipes, Unix sockets, and directories are all file-descriptor-accessible via `read()`/`write()`. |
| 20 | **D** | The directory entry is just a (name → inode-number) mapping. The inode holds all file metadata plus pointers to data blocks. Two directory entries (hard links) can share one inode. |
| 21 | **A** | `link()` creates a new directory entry pointing to the same inode and increments the link count. Data blocks are freed only when the count hits 0. Hard links cannot span filesystems. |
| 22 | **B** | `/proc` is a pseudo-filesystem: no data lives on disk. The kernel generates its content on-the-fly. It exposes `/proc/cpuinfo`, `/proc/meminfo`, `/proc/<pid>/maps`, sysctl values, and more. |
| 23 | **C** | `df` ("disk free") reports filesystem-level usage (mounted filesystems, used/available blocks). `du -sh .` reports directory tree size. |
| 24 | **D** | `rwxr-x---` in octal is 750. Owner (7=rwx), Group (5=r-x), Others (0=---). Group members can read and execute, but not write. |
| 25 | **A** | Classic example: `/usr/bin/passwd` has setuid root so a regular user can update `/etc/shadow` without a root shell. The effective UID becomes the file owner's UID during execution. |
| 26 | **B** | `chown user file` changes the owner. `chown user:group file` changes both. `chgrp group file` changes only the group. Requires root or being the current owner. |
| 27 | **C** | Octal 644 = 110 100 100. Owner: rw- (6); Group: r-- (4); Others: r-- (4). The standard permission for regular files. |
| 28 | **D** | `sudo` checks the sudoers policy, prompts for the user's own password, forks a child with root privileges, runs the command, then exits. The calling shell's UID is unchanged. |
| 29 | **A** | The kernel's page reclaim algorithm pages out least-recently-used anonymous pages to swap when physical RAM is under pressure. Pages are read back on access (a page fault), incurring I/O latency. |
| 30 | **B** | `vm.swappiness` can be set via `sysctl -w vm.swappiness=10`. Lower values keep more data in RAM; 0 avoids swapping except when absolutely necessary. Default is 60. |
| 31 | **C** | `free -h` shows total, used, free, shared, buff/cache, and available for both RAM and swap. `-m` for megabytes, `-g` for gigabytes. |
| 32 | **D** | cgroups v1/v2 enforce resource quotas: container runtimes create a cgroup per container and set limits via cgroup files. The OOM killer respects cgroup memory limits. |
| 33 | **A** | OverlayFS stacks read-only image layers under a thin read-write container layer. Writes to existing files trigger copy-on-write; the image layers are never modified. |
| 34 | **B** | The writable layer is stored under `/var/lib/docker/overlay2/<id>/`. It persists until `docker rm` or `docker container prune`. `--rm` on `docker run` removes it automatically at exit. |
| 35 | **C** | VMs require a hypervisor and run a full guest kernel per VM (stronger isolation, higher overhead). Containers share the host kernel and are isolated by namespaces and cgroups (lower overhead). |
| 36 | **D** | `ls -a` adds hidden files (dotfiles); `ls -l` adds the long format. Combined, `-la` lists all files including hidden ones with full metadata. |
| 37 | **A** | `-r`/`-R` makes grep descend into all subdirectories. Without it, grep only scans files explicitly listed or the current directory level. |
| 38 | **B** | `a` = all users; `u` = display CPU/mem columns; `x` = include daemonised/non-tty processes. Together `aux` gives a full process list regardless of terminal or ownership. |
| 39 | **C** | `>` redirects fd 1 (stdout) to the file. `2>&1` duplicates fd 1 to fd 2 (stderr). Both streams now go to the file. Note: `command 2>&1 > file.txt` would only redirect stdout; stderr would still go to the terminal. |
| 40 | **D** | The kernel creates an in-memory pipe (a kernel buffer). The left command writes to the write end; the right command reads from the read end. No disk I/O involved. |
| 41 | **C** | The PID namespace virtualises the process table. A container's init process sees itself as PID 1 and can only see other processes within the same namespace. The host still sees the real PID. |
| 42 | **D** | `fork()` copies the process; `exec()` overlays the child with the new binary. The shell waits for the child to exit (via `waitpid()`), then prompts for the next command. |
| 43 | **A** | `--now` is the inverse of `enable --now`: it runs `systemctl stop` AND `systemctl disable` atomically. Without `--now`, `disable` only removes the symlinks without stopping a running service. |
| 44 | **B** | `du` only sees directory entries. A deleted-but-still-open file has no directory entry, so `du` misses it, but `df` reports the blocks as used because the kernel has not freed them. Use `lsof +L1` to find such files. |
| 45 | **C** | `rm` calls `unlink()`, which removes the directory entry and decrements the hard-link count. The inode and data blocks are freed by the kernel only when the link count hits zero AND no process holds the file open. |
| 46 | **D** | An inode number like `42` is meaningful only within its filesystem. A hard link on a different filesystem that pointed to inode `42` would reference whatever random file has that inode there — the kernel forbids this. |
| 47 | **A** | Without a user specifier, `+x` applies to `a` (all: owner, group, others). To restrict to owner only, use `u+x`. To see the exact bits, run `stat` or `ls -l` after. |
| 48 | **B** | `-R` (recursive) descends into all subdirectories and applies the ownership change to every file and directory it finds. Commonly used when setting up web roots or application directories. |
| 49 | **C** | "available" ≠ "free". Available = free RAM + reclaimable buffers/cache. Linux aggressively caches disk data in RAM; that memory is instantly reclaimable when a process needs it. |
| 50 | **D** | The cgroup memory limit is enforced by the kernel. When a process in the cgroup tries to allocate memory beyond the limit, the kernel OOM-kills the heaviest consumer in that cgroup rather than triggering a system-wide OOM event. |
| 51 | **B** | Signals are the kernel's async IPC primitive. Delivery interrupts the process; it either runs a registered handler (`sigaction`), takes the default action (terminate, core dump, stop, ignore), or the signal stays blocked/pending. |
| 52 | **C** | Always try `SIGTERM` first so the process can flush buffers, close connections, and clean up. `SIGKILL` never reaches the process — the kernel destroys it directly, so no cleanup code runs (risk: corrupted state, leftover lock files). |
| 53 | **A** | `kill` defaults to `SIGTERM` (15). `kill -9` = `SIGKILL`, `kill -HUP` = `SIGHUP`. `kill -l` lists all signals with their numbers. |
| 54 | **D** | `SIGKILL` (9) and `SIGSTOP` (19) are enforced entirely by the kernel: a process can never install a handler for them, block them, or ignore them. This guarantees the admin can always kill or suspend a runaway process. |
| 55 | **B** | The terminal driver turns `Ctrl+C` into `SIGINT` for the entire foreground process group — that is why a whole pipeline dies together. `Ctrl+\` sends `SIGQUIT` (with core dump); `Ctrl+Z` sends `SIGTSTP`. |
| 56 | **C** | Both suspend a process (resumed with `SIGCONT` or `fg`/`bg`), but `SIGTSTP` is the polite terminal-generated stop that a program may catch (e.g. vim resets the terminal first). `SIGSTOP` is unconditional, like `SIGKILL` for pausing. |
| 57 | **A** | `SIGHUP` originally meant "terminal hung up". Daemons have no terminal, so the convention is to reuse it for config reload: `kill -HUP $(cat /run/nginx.pid)` or `nginx -s reload`. systemd services often map it via `ExecReload=`. |
| 58 | **D** | When a terminal closes, the kernel sends `SIGHUP` to its jobs, which normally kills them. `nohup` sets `SIGHUP` to ignored (and redirects output to `nohup.out`). Alternatives: `setsid`, `disown`, tmux/screen, or a systemd unit. |
| 59 | **B** | State `D` (uninterruptible sleep) means the task is blocked inside a kernel syscall, typically disk or network-filesystem I/O. Signals — even `SIGKILL` — are only processed when the syscall finishes. Persistent D-state usually indicates hung storage. |
| 60 | **C** | The MMU raises a page fault; if the kernel finds the address invalid for that process, it delivers `SIGSEGV` (segmentation violation). Default action: terminate with core dump. Classic causes: NULL/dangling pointers, buffer overruns, stack overflow. |
| 61 | **A** | `trap 'handler' SIGNALS` registers cleanup code. `EXIT` is a bash pseudo-signal that fires on any script exit, making it the idiomatic place for temp-file cleanup. `trap -l` lists signals; `trap - INT` restores the default. |
| 62 | **D** | On child exit the kernel sends the parent `SIGCHLD`. The parent reaps the child with `wait()`/`waitpid()`, freeing its process-table entry. Parents that never reap leak zombies. Ignoring `SIGCHLD` explicitly makes the kernel auto-reap. |
| 63 | **B** | A zombie (state `Z`, `<defunct>` in ps) is already dead — it holds no memory or CPU, just an exit-status record awaiting the parent's `wait()`. `kill -9` cannot affect it. Fix the parent (or kill it so PID 1 adopts and reaps the zombie). |
| 64 | **C** | `pkill -SIGNAL pattern` matches process names (add `-f` to match the full command line); `pgrep` shows what would match first — always safer to check. `killall name` matches exact names. Plain `kill` needs a PID. |
| 65 | **A** | Shared between threads: address space (heap, globals, code), file descriptors, signal handlers, cwd. Private per thread: stack, registers, program counter, TID, errno. Processes get full isolation; threads get cheap data sharing plus shared failure. |
| 66 | **D** | Linux has no separate thread concept in the kernel — everything is a `task_struct`. `pthread_create()` calls `clone()` with the flags CLONE_VM, CLONE_FILES, CLONE_SIGHAND and CLONE_THREAD, so the new task shares memory and files. `fork()` is `clone()` with nothing shared. |
| 67 | **B** | Threads in one process form a thread group; `getpid()` returns the shared TGID (the "process ID" you see in `ps`), while `gettid()` returns the per-thread TID. The thread-group leader's TID equals the TGID. |
| 68 | **C** | This makes `fork()` cheap even for huge processes: only page tables are copied at fork time. A write by either side triggers a page fault, and the kernel copies just that page. This is also why `fork()` + `exec()` is efficient. |
| 69 | **A** | `exec` does not create a process — it transforms the calling one: new code, new heap/stack, same PID, same open FDs (minus `O_CLOEXEC` ones). That FD inheritance is exactly how the shell wires up redirections before exec'ing a command. |
| 70 | **D** | Orphans are adopted by PID 1 (systemd) or the nearest process marked `PR_SET_CHILD_SUBREAPER`. PID 1 reaps adopted children as they exit, which is why orphans do not become permanent zombies — and why a container's PID 1 must reap children. |
| 71 | **B** | `ps -T -p PID` lists threads with their SPID/TID column; `top -H` shows per-thread CPU usage. You can also `ls /proc/PID/task/` — one subdirectory per thread. Useful for finding which thread of a busy process is burning CPU. |
| 72 | **C** | Nice ranges -20 (most favored) to 19 (least favored); default 0. Only root can lower (raise priority). `nice -n 10 cmd` starts nicer; `renice -n 5 -p PID` adjusts a running one. Real-time policies (SCHED_FIFO/RR, priorities 1-99) are a separate mechanism. |
| 73 | **A** | A process switch must swap CR3 (page-table base) and lose TLB entries, which is the expensive part. Same-process thread switches keep the address space, so only registers and stack pointer change. Still a kernel-mode switch, unlike userspace green threads. |
| 74 | **D** | Signals like `SIGSEGV` are process-directed in effect: the default action (terminate + core) applies to the whole thread group. This shared blast radius is the classic argument for process isolation (e.g. nginx workers, Chrome per-tab processes). |
| 75 | **D** | Real unit types: service, socket, timer, target, mount, automount, path, device, slice, scope, swap. There is no `.cron` — scheduled jobs use `.timer` units. `systemctl list-units --type=timer` shows active timers. |
| 76 | **B** | Precedence (high to low): `/etc/systemd/system` (admin) beats `/run/systemd/system` (runtime) beats `/usr/lib/systemd/system` (package). A same-named unit in `/etc` completely shadows the packaged one. `systemctl cat <unit>` shows which files are in effect. |
| 77 | **C** | systemd keeps units parsed in memory and does not watch the files. `daemon-reload` re-parses everything (it even warns you if you forget). Note: `systemctl reload <svc>` is different — it runs the service's own `ExecReload=` (e.g. nginx config reload). |
| 78 | **A** | Drop-ins are merged over the base unit, so package updates to the original file still apply. `systemctl edit --full` copies the whole unit to `/etc` instead. `systemctl cat` shows base + drop-ins; `systemctl revert` deletes the overrides. |
| 79 | **D** | Wrong Type is a classic bug: a daemon that forks under `Type=simple` looks "dead" to systemd (main process exited); a non-forking app under `Type=forking` hangs the start job until timeout. Modern daemons prefer simple/exec/notify over forking. |
| 80 | **B** | With `Type=notify` the service calls `sd_notify(0, "READY=1")` when actually ready to serve, so dependent units start at the right moment. Compare `Type=simple`: "started" the instant the process is forked, ready or not. `Type=exec` waits only for execve success. |
| 81 | **C** | `on-failure` = unclean exit only. Other values: `always` (even clean exits), `on-abnormal` (signals/timeouts, not bad exit codes), `no` (default). Tune with `RestartSec=`, and `StartLimitIntervalSec=`/`StartLimitBurst=` to stop restart loops. |
| 82 | **A** | These are orthogonal axes: ordering (`After=`/`Before=`) vs requirement (`Requires=`/`Wants=`). `Requires=` alone can start both units simultaneously. The common correct pair is `After=x.service` plus `Requires=x.service` (or `Wants=`). |
| 83 | **D** | `Wants=` = best-effort: start it if you can, carry on if not. `Requires=` = hard: if the required unit fails to start or is stopped, this unit fails/stops too. Docs recommend `Wants=` unless the unit truly cannot run without the other. |
| 84 | **B** | "Enabled" is literally a symlink in the target's `.wants/` directory — nothing more. At boot, `multi-user.target` pulls in everything in its `.wants/` dir. `disable` removes the symlink; `is-enabled` checks it; `preset` applies distro defaults. |
| 85 | **C** | A timer unit is a trigger; the work lives in the same-named service (override with `Unit=`). `OnCalendar=` uses calendar syntax (`Mon..Fri 02:00`), `OnBootSec=`/`OnUnitActiveSec=` give monotonic timers. `Persistent=true` catches up runs missed while powered off — an edge cron handles poorly. |
| 86 | **A** | `journalctl -b` = current boot; `-b -1` = previous boot (gold for "why did it crash before reboot?"). `list-boots` enumerates them. Requires persistent journal storage (`/var/log/journal` existing or `Storage=persistent`). |
| 87 | **D** | `-p err` filters priority 0-3 (emerg, alert, crit, err). Priorities follow syslog levels 0-7 (debug=7). Combine freely: `-u` unit, `--since`/`--until` time, `-g` grep pattern, `-o json` for structured output, `-k` for kernel messages only. |
| 88 | **B** | `mask` is the "never run this" hammer — `start` then fails with "Unit is masked". Use it to stop dependencies or admins from resurrecting a service (e.g. masking a conflicting DNS daemon). `unmask` reverses it. `disable` still allows `systemctl start` and dependency activation. |
| 89 | **C** | `blame` lists per-unit init times, `critical-chain` shows the dependency path that gated boot (more honest, since units start in parallel), `systemd-analyze` alone gives kernel vs userspace totals, and `plot > boot.svg` draws the whole timeline. |
| 90 | **A** | `set-default` re-links `default.target` (what the system boots into). `get-default` shows the current one. `isolate` switches target NOW without persisting — the modern runlevel change. `/etc/inittab` is pre-systemd and ignored. |
| 91 | **D** | User units live in `~/.config/systemd/user/`, start at login, and run with the user's privileges — great for dev services and agents. By default they stop at logout; `loginctl enable-linger <user>` keeps them running without a session. |
| 92 | **B** | Declared via a `.socket` unit with `ListenStream=`; systemd creates the FD, passes it to the service on activation. Benefits: on-demand start, zero-downtime restarts (socket buffers connections while the service restarts), and services that can start in any order since the socket exists first. |
| 93 | **C** | Interactive non-login shells read `~/.bashrc`. Login shells (ssh, console, `bash -l`) read `/etc/profile` then the first of `~/.bash_profile`, `~/.bash_login`, `~/.profile` — which is why most distros source `~/.bashrc` from `~/.bash_profile` to unify behavior. |
| 94 | **A** | The environment is a per-process key-value table copied to children at `fork()`/`exec()`. `export` marks a shell variable for inclusion. `env` shows the environment; `FOO=bar cmd` sets it for one command only; children can never modify the parent's environment. |
| 95 | **D** | Convention: 0 = success, non-zero = failure (126 = not executable, 127 = command not found, 128+N = killed by signal N, so 137 = SIGKILL/OOM). The `&&` (and-list) and or-list operators branch on it; `set -e` aborts a script on any non-zero status. |
| 96 | **B** | Builtin `exec` without redirection-only usage calls `execve()` from the shell itself: no fork, the command inherits PID. In Docker entrypoints, `exec "$@"` makes the app PID 1 so it receives `docker stop`'s SIGTERM instead of the wrapper shell swallowing it. |
| 97 | **C** | The working directory is per-process state. `fork()` copies it down; children cannot push changes up. Same reason `export`, `umask`, `ulimit`, and `alias` are builtins. This is the crispest demonstration that the shell is just a normal user-space process. |
| 98 | **A** | Shebang handling is in the kernel's `execve()` binfmt logic, not the shell: it rewrites the exec as interpreter + script path. `env` searches `$PATH` for `python3`, making the script portable across systems where python lives in different places. |
| 99 | **D** | The kernel logs to an in-memory ring buffer, readable via `dmesg` or `journalctl -k`. Check it for hardware errors, OOM-killer kills, segfault records, and firewall logs. `-T` gives human timestamps; `-w` follows like `tail -f`. |
| 100 | **B** | `modprobe wifi_driver` reads dependency info from `depmod`'s map and loads prerequisites first; `insmod` takes a literal `.ko` path and fails on unresolved symbols. `lsmod` lists loaded modules, `modprobe -r` unloads, `/etc/modprobe.d/` configures options and blacklists. |

---

## TypeScript MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **B**  | Object LITERALS passed directly undergo excess property checking, so (2) errors on `z`. A variable like `q` is checked structurally — extra properties are fine — so (1) compiles. |
| 2  | **B**  | `unknown` is the type-safe top type: you must narrow it (typeof, instanceof, guards) before using it. `any` opts the value out of type checking completely. |
| 3  | **C**  | Interfaces and type aliases exist only at compile time. Type erasure means no JS is emitted for them, which is also why `instanceof` cannot test an interface. |
| 4  | **B**  | `kind` is a discriminant. Checking it narrows the union to the matching member, so `s.radius` is safe inside the `"circle"` case. |
| 5  | **C**  | `as const` gives the narrowest immutable type: a readonly tuple of the literal types `1` and `2`, not a widened `number[]`. |
| 6  | **B**  | `Partial<T>` maps every property to an optional one: `{ [K in keyof T]?: T[K] }`. |
| 7  | **B**  | `Omit<User, "id">` removes `id`, leaving `name` and `email`. `Pick` selects listed keys; `Exclude` operates on union members, not object properties. |
| 8  | **B**  | `Record<K, V>` builds an object type with keys `K` and values `V`. It describes a plain object, not a `Map`. |
| 9  | **B**  | `keyof` yields a union of the type's property names as string literal types: `"a"` or `"b"`. |
| 10 | **B**  | In type position `typeof` queries the static type of a value, so `Config` is the inferred object type. (The runtime `typeof` operator is unrelated.) |
| 11 | **C**  | `T` must extend `{ length: number }`. Strings and arrays have `length`; the primitive `number` does not, so `longest(10, 20)` is rejected. |
| 12 | **B**  | Exhaustiveness check: if every variant is handled, `s` is `never` in `default` and the assignment compiles. Add a new variant and `s` is no longer `never`, producing a compile error at exactly this line. |
| 13 | **C**  | `??` (nullish coalescing) falls back only on `null`/`undefined`, so the first line prints `0`. Logical OR falls back on ANY falsy value (0, "", false, NaN), so the second line prints `"fallback"`. |
| 14 | **A**  | Numeric enums get a reverse mapping: `Direction.Up` is `0` and `Direction[0]` is `"Up"`. (String enums have no reverse mapping.) |
| 15 | **B**  | Declaration merging is interface-only: repeated `interface Foo` blocks combine. A duplicate `type Foo` alias is a "duplicate identifier" error. |
| 16 | **B**  | `readonly T[]` removes the mutating methods (`push`, `pop`, `splice`, ...) from the type, so `xs.push(0)` is a compile error. There is no runtime freezing. |
| 17 | **B**  | An intersection requires the value to satisfy BOTH constituents, so it needs `a: string` and `b: number`. |
| 18 | **B**  | An `async` function always returns a Promise; the resolved value's type is inferred, giving `Promise<number>`. |
| 19 | **B**  | The `pet is Fish` type predicate tells the compiler that a `true` return proves `pet` is a `Fish`, narrowing it inside `if (isFish(pet))` blocks. |
| 20 | **C**  | Under `strictNullChecks`, `null` is not assignable to `string` — (1) errors. (2) explicitly includes `null` in the type, so it compiles. |
| 21 | **B**  | `satisfies` validates against the wide type WITHOUT widening: `palette.green` stays `string` instead of the wide union, so string methods still compile. A plain annotation would widen every property. |
| 22 | **C**  | Mapping every key with a `?` modifier is exactly the definition of `Partial<T>`. |
| 23 | **A**  | `Exclude<T, U>` is a distributive conditional type: it is applied to each union member separately, dropping the ones assignable to `U`, leaving the union of `"b"` and `"c"`. |
| 24 | **B**  | Only the overload signatures form the public API; the (necessarily wider) implementation signature is hidden from callers. Resolution happens at compile time, top overload first. |
| 25 | **C**  | The `if` branch returns, so control-flow analysis removes `string` from the union: after the block `x` is narrowed to `number`. |
| 26 | **B**  | `let` widens literals to their base type so they can be reassigned. `const` cannot be reassigned, so the narrowest literal type `"hello"` is kept. |
| 27 | **B**  | Template literal types distribute over union members, producing the union of `"btn-small"` and `"btn-large"`. |
| 28 | **A**  | `infer U` captures the promised type when `T` matches `Promise<...>`, giving `string`. `number` does not match, so the false branch returns `T` unchanged. |
| 29 | **A**  | `typeof make` is the function type; `ReturnType` extracts its inferred return type — no explicit annotation needed. |
| 30 | **C**  | A tuple type fixes both element types AND length. Indexing gives the precise per-position types, so (1) and (2) compile; `["b"]` is missing the `number` element. |
| 31 | **B**  | An optional property may be absent, so reading it yields `number` or `undefined`. (With `?` the `undefined` is implicit in the property's type.) |
| 32 | **C**  | The non-null assertion `!` only silences the compiler — it emits no check. At runtime `undefined.length` throws a TypeError. |
| 33 | **B**  | The `in` operator is a narrowing guard: only the `Fish` member of the union has a `swim` property, so `x` is `Fish` inside the block. |
| 34 | **B**  | A `void` return type means the caller promises to ignore the result, so functions returning values are assignable. This is why `array.forEach(x => list.push(x))` works. |
| 35 | **B**  | TypeScript `private` is erased — the field is reachable at runtime via bracket access. ES `#fields` are part of JavaScript and enforced by the engine itself. |
| 36 | **B**  | Parameter properties (`private`, `public`, `readonly`, etc. on constructor params) declare the class property and assign the argument in one step. |
| 37 | **B**  | Abstract classes exist to be subclassed; instantiating one directly is a compile-time error. |
| 38 | **C**  | `Box` with no type argument uses the generic default, so `b.value` is `string`. |
| 39 | **B**  | `const enum` members are inlined at every use site and the enum object is erased entirely — zero runtime footprint (and therefore no reverse mapping). |
| 40 | **B**  | `import type` guarantees the import is erased from the output, avoiding side effects and circular-import issues. Using the name as a value is a compile error. |
| 41 | **C**  | A direct `as` between types with insufficient overlap is rejected. Asserting through `unknown` (or `any`) first defeats the check — legal but a deliberate escape hatch. |
| 42 | **B**  | `await` (and the `Awaited` utility type) unwrap promises recursively, so a nested `Promise<Promise<number>>` awaits to plain `number`. |
| 43 | **B**  | `Readonly<T>` only affects the top level: reassigning `c.nested` errors, but the nested object's own properties remain writable. |
| 44 | **A**  | `NonNullable<T>` strips `null` and `undefined` from the union, leaving `string`. |
| 45 | **B**  | Truthiness narrowing removes `null` from the TYPE. Note the runtime check also excludes `""`, but the empty string is still a `string` — types do not track emptiness. |
| 46 | **C**  | `typeof Color` is the enum OBJECT's type; `keyof` of that gives the member names as a union of string literals. (`keyof Color` alone would be the keys of the number type.) |
| 47 | **B**  | `mixed` is inferred as an array of string-or-number elements, which matches (1) exactly. It is not assignable to (2): the array is neither all-strings nor all-numbers. |
| 48 | **B**  | The definite assignment assertion suppresses `strictPropertyInitialization` when a field is set outside the constructor (e.g. by a DI framework or `init()` method). It changes nothing at runtime. |
| 49 | **B**  | Function assignability ignores missing trailing parameters: the implementation may simply not use them. This is why you can pass `(item) => ...` where `(item, index, array) => ...` is expected. |
| 50 | **B**  | TypeScript compares classes structurally, like all other types: identical shapes are mutually assignable. Adding a `private` member would make each class nominal-ish and break this. |

---

## Go MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **B**  | Go uses M:N scheduling (GMP model): many goroutines (G) are multiplexed onto a smaller pool of OS threads (M) via logical processors (P). `GOMAXPROCS` controls the number of Ps. |
| 2  | **C**  | Since Go 1.4, goroutines start with a 2 KB contiguous stack. When a stack overflow is detected the runtime allocates a larger contiguous stack, copies the contents, and resumes — enabling millions of goroutines cheaply. |
| 3  | **B**  | Receiving from a closed channel immediately returns the zero value and `false` for the `ok` variable. It never blocks and never panics. |
| 4  | **B**  | Deferred function *arguments* are evaluated immediately when the `defer` statement is reached, not when the deferred function runs. `add(x, 5)` is evaluated with `x=10` → 15. "done" prints first; 15 prints on exit. |
| 5  | **B**  | The Go memory model guarantees: a send on a channel happens before the corresponding receive completes (and for unbuffered channels, the receive happens before the send completes). Unsynchronised concurrent access is a data race regardless of read/write ratio. |
| 6  | **B**  | A slice header (pointer, length, capacity) is passed by value, but the pointer references the same underlying array. Modifying elements via `s[i]` mutates the shared array; the caller sees `[2 4 6]`. |
| 7  | **B**  | An interface value is nil only when BOTH its type and value components are nil. A typed nil pointer (`var p *T = nil; var i I = p`) gives the interface a non-nil type component, so `i == nil` is false — a frequent source of bugs. |
| 8  | **B**  | `i := i` declares a new variable in each loop body, capturing the current value. Without this shadowing all closures share the same `i` (which would be 3 after the loop). With it, each closure captures its own copy: 0, 1, 2. |
| 9  | **C**  | Go only detects deadlock when ALL goroutines are asleep simultaneously. A single blocked goroutine leaks silently, holding its stack and any objects it references. `pprof` goroutine profiles or context cancellation are the remedies. |
| 10 | **B**  | Accessing a missing map key returns the zero value (0 for `int`) without panicking. `m["missing"]++` is equivalent to `m["missing"] = m["missing"] + 1` — it creates the key. Reading from an uninitialised (`nil`) map is also safe; writing to one panics. |
| 11 | **B**  | `GOMAXPROCS` sets the number of logical processors (P) and thus the number of OS threads simultaneously executing Go code. It defaults to `runtime.NumCPU()`. More goroutines than `GOMAXPROCS` can be runnable; only `GOMAXPROCS` run at once. |
| 12 | **C**  | Receiving from a nil channel blocks forever. Sending to a nil channel also blocks forever. Closing a nil channel panics. These semantics are useful for disabling a `select` case by setting its channel to nil. |
| 13 | **B**  | Concurrent reads without any writes are safe. Any concurrent write alongside other reads or writes is a data race. Since Go 1.6 the runtime detects concurrent map read/write and panics. `sync.Map` is optimised for specific high-read-ratio patterns, not a general replacement. |
| 14 | **B**  | `a = s[1:3]` has len=2, cap=4, sharing s's backing array. `append(a, 99)` has spare capacity so it writes 99 at index 3 of the shared array, mutating `s[3]`. `s` becomes `[1 2 3 99 5]`; `b` is `[2 3 99]`. |
| 15 | **B**  | `sync.Mutex`, `sync.RWMutex`, `sync.WaitGroup`, and `sync.Once` are all usable at their zero value. `var mu sync.Mutex` is a valid, unlocked mutex. Copying them after first use is the bug to avoid. |
| 16 | **B**  | Named return values are ordinary variables. `return 0` sets `result = 0`. The deferred closure then runs `result++`, so the function returns 1. Deferred functions can observe and modify named returns. |
| 17 | **B**  | The closure captures the loop variable `item` by reference. By the time goroutines are scheduled, the loop may have advanced. The fix is to pass `item` as an argument: `go func(item T) { process(item) }(item)`. |
| 18 | **D**  | When multiple cases in a `select` are simultaneously ready, Go's runtime picks one pseudo-randomly. This prevents starvation but means channel-priority must be encoded with nested `select` statements, not case ordering. |
| 19 | **B**  | The method set of `T` contains only value receiver methods. The method set of `*T` contains both value and pointer receiver methods. Because `Sound` has a pointer receiver, only `*Cat` satisfies `Animal`. |
| 20 | **A**  | `wg.Wait()` blocks until `wg.Done()` is called. The goroutine prints "goroutine" before calling `wg.Done()`, establishing a happens-before relationship. "goroutine" always appears before "main". |
| 21 | **B**  | `context.WithCancel` returns a derived context and a cancel function. Calling `cancel()` closes `ctx.Done()`, signalling all code selecting or polling on it to stop. Cancellation propagates to child contexts. |
| 22 | **A**  | A buffered channel with capacity 3 holds up to 3 values without blocking. `len(ch)` is the number of queued items (3); `cap(ch)` is the buffer size (3). |
| 23 | **C**  | The idiomatic pattern: `select { case v := <-ch: … case <-time.After(d): … }`. `time.After` returns a channel that receives after the duration. For long-running loops prefer `time.NewTimer` to avoid timer leaks. |
| 24 | **C**  | A package may have multiple `init` functions, even in the same file. They run in declaration order after all variable initialisations. `x` starts at 1, each `init` increments it → 3. |
| 25 | **B**  | `recover()` inside a deferred function catches the panic and returns the panic value. The function exits normally after the deferred call; "unreachable" never runs. A `recover()` outside a deferred function has no effect. |
| 26 | **B**  | Value receivers copy the receiver, including the embedded `sync.Mutex`. The copy's `Lock`/`Unlock` operate on the copy's state, not the original's. `go vet` reports "lock value copied". The fix is a pointer receiver `(c *Cache)`. |
| 27 | **B**  | `-race` instruments every memory access with calls into ThreadSanitizer. At runtime, concurrent conflicting accesses to the same memory location without synchronisation are reported with goroutine stack traces. It adds ~5–10× overhead. |
| 28 | **C**  | Go strings are immutable byte sequences. `[]byte(s)` allocates a copy. Modifying `b` does not affect `s`. `s` stays "hello"; `string(b)` is "Hello". |
| 29 | **B**  | `Scale` has a value receiver and returns a new `Point`; it does not modify `p`. The returned value is discarded. `p` remains `{3 4}`. A common mistake is expecting value-receiver methods to mutate the original. |
| 30 | **B**  | `iota` is the index of the const within the block (0-based). A = 0, B = 1 (repeats last expr `iota`), C = 2×2 = 4, D = 3×2 = 6 (repeats `iota * 2`). Output: `0 1 4 6`. |
| 31 | **B**  | An unrecovered panic in any goroutine terminates the entire process. There is no goroutine-level isolation. This is why long-running goroutine-spawning loops (e.g. HTTP servers) wrap handlers in a `defer recover()`. |
| 32 | **B**  | `fmt.Errorf("…: %w", err)` wraps the error so `errors.Is` and `errors.As` can unwrap the chain. Option A loses the original error type. Option D is from the third-party `pkg/errors` package, not the standard library. |
| 33 | **B**  | The closure captures the loop variable `item` by reference. All goroutines may see the same (often last) value by the time they run. Fix: pass `item` as a goroutine argument — `go func(item string) { … }(item)`. |
| 34 | **C**  | Accessing a missing map key returns the zero value: `nil` for `[]int`. `append(nil, 1)` creates a new slice and returns it. The result is stored back in `m["nums"]`. Second append: `[1]` → `[1 2]`. |
| 35 | **B**  | Deferred functions run LIFO at the end of the surrounding function. Arguments are evaluated immediately: at i=0,1,2 three defers register. On exit they fire in reverse: 2, 1, 0. |
| 36 | **B**  | `time.After(d)` creates a `*time.Timer` and a backing goroutine that fires after `d`. If the `select` returns via the `done` case before the timer fires, the timer goroutine and its channel linger until the duration elapses. In hot loops this accumulates. Use `time.NewTimer` with an explicit `t.Stop()`. |
| 37 | **B**  | `fmt` checks whether the argument implements `fmt.Stringer`. `MyInt` does, so `String()` is called, returning `"MyInt(42)"`. Note: calling `fmt.Sprintf("…", m)` (without `int(m)`) inside `String()` would recurse infinitely; `int(m)` breaks the cycle. |
| 38 | **B**  | In a multi-value assignment, the right-hand side is evaluated fully before any assignment occurs. `*a` (10) and `*b` (20) are both read, then `*a` is set to 20 and `*b` is set to 10. Output: `20 10`. |
| 39 | **A**  | `1` and `2` are synchronised via the channel sends. After `close(ch)`, `range ch` exits and the goroutine prints "done" — but `time.Sleep` is not a synchronisation barrier. If the goroutine hasn't finished by the time `main` returns, "done" is lost. Use a `sync.WaitGroup` instead. |
| 40 | **B**  | Escape analysis is a compile-time pass. Variables whose lifetimes are bounded to their stack frame stay on the stack (cheap allocation, no GC pressure). Variables that outlive their frame — returned pointers, goroutine captures, interface conversions — escape to the heap. Use `go build -gcflags="-m"` to inspect decisions. |
| 41 | **C**  | Maps, slices, and functions are not comparable with `==` — using `==` on them is a compile error. Structs are comparable if all fields are comparable. Arrays are comparable. Interfaces are comparable (but panic at runtime if the dynamic type is not). |
| 42 | **B**  | `sync.Once.Do(f)` guarantees `f` runs exactly once regardless of how many goroutines call `Do` concurrently. All concurrent callers block until the first execution of `f` completes. Zero value is ready to use. |
| 43 | **B**  | Arrays are value types in Go. `b := a` copies the entire array. Modifying `b[0]` does not affect `a`. This is the opposite of slice behaviour, where the slice header is copied but the backing array is shared. |
| 44 | **B**  | `s2 = s[:2]` shares the backing array with `s` and has capacity ≥ 3. `append(s2, 99)` has spare capacity, so it writes 99 at index 2 of the shared array, mutating `s[2]`. `s` becomes `[1 2 99]`. |
| 45 | **C**  | Writing to *distinct* indices of a slice from concurrent goroutines is safe — those are separate memory locations with no overlap. The `wg.Wait()` provides the happens-before edge needed to read `results` safely afterwards. This is idiomatic Go. |
| 46 | **B**  | `sync.Mutex` is not reentrant. A goroutine that calls `Lock()` while already holding the lock deadlocks (blocks forever waiting for itself to unlock). The runtime detects this only if ALL goroutines are asleep simultaneously. |
| 47 | **B**  | With a single iteration variable in `range`, Go assigns the **index** (0-based), not the value. To iterate values, use `for _, v := range slice`. Output: `0 1 2 `. |
| 48 | **B**  | The single-value form `v := x.(T)` panics if `x` does not hold a `T`. The two-value "comma-ok" form `v, ok := x.(T)` sets `ok = false` without panicking, allowing safe dynamic type checks. |
| 49 | **B**  | The goroutine closes the channel after 10 ms. The `time.After` fires after 1 s. Since 10 ms ≪ 1 s, the channel case is always ready first. |
| 50 | **B**  | Go's GC is a concurrent, tri-color mark-and-sweep collector. It runs mostly concurrently with the application (short stop-the-world pauses for write-barrier setup and final marking). It is not reference counting. It triggers automatically based on heap growth, tunable via `GOGC`. |

---

## React MCQ

| Q  | Answer | Explanation |
|----|--------|-------------|
| 1  | **A**  | The virtual DOM is a plain JS object tree mirroring the real DOM. React diffs the previous and next trees, then applies only the changed nodes to the real DOM — far cheaper than rebuilding the entire tree. |
| 2  | **C**  | React's two heuristics: (1) different element types → tear down the whole subtree; (2) `key` lets React match children across renders. These reduce diffing from O(n³) to O(n). |
| 3  | **C**  | Fiber (React 16+) rewrote the reconciler to represent work as a linked list of "fiber" nodes. This lets React pause, resume, or abort rendering mid-tree, enabling concurrent features. |
| 4  | **B**  | `key` is the identity signal for the reconciler. React uses it to detect adds, removes, and reorders within a list without rescanning every sibling. |
| 5  | **B**  | When items are reordered or deleted, the index shifts. React matches the new `key=0` to the old `key=0` node and reuses its DOM and component state for the wrong item. Stable, unique IDs from data are the fix. |
| 6  | **B**  | React batches both `setCount` calls into a single render. Both read `count` from the same closed-over render snapshot (0), so both compute `0 + 1 = 1`. The result is 1, not 2. |
| 7  | **C**  | The functional update form `setCount(c => c + 1)` receives the latest queued state, not the stale closure value. Calling it twice correctly produces `0 → 1 → 2`. |
| 8  | **B**  | `[]` means "no dependencies that can change" — run once on mount. The returned cleanup function runs once on unmount. This mirrors `componentDidMount` + `componentWillUnmount`. |
| 9  | **B**  | With no dependency array `useEffect` runs after every render. `setCount` causes a render, which causes the effect to run again — an infinite loop. Fix: add `[count]` and use a functional update, or use `[]` with `setCount(c => c + 1)`. |
| 10 | **C**  | Each render creates a fresh closure. If a `useEffect` (or `useCallback`) captures a variable and runs after a subsequent render, it holds the value from the render it was created in, not the current one. |
| 11 | **B**  | Without `return () => clearInterval(id)`, the interval keeps firing after the component unmounts, calling `setCount` on an unmounted component — a memory leak and a React warning. |
| 12 | **C**  | `useCallback` memoizes the function reference. The same function object is returned on every render until a dependency changes. This prevents inline functions from breaking `React.memo` or `useEffect` comparisons. |
| 13 | **C**  | `useMemo` caches the computed value between renders. If `a` and `b` are the same as the last render (by reference/value), the cached result is returned without re-running the computation. |
| 14 | **D**  | `useRef` returns a stable object `{ current }`. Mutating `.current` does not notify React — no re-render occurs. This makes it suitable for timers, DOM nodes, and other values that should not drive UI updates. |
| 15 | **B**  | React hooks must be called unconditionally at the top level of every render. Calling `useState` inside an `if` block changes the hook call order between renders, corrupting React's internal state array. |
| 16 | **D**  | `React.memo` is a higher-order component that does a shallow prop comparison before each render. If all props are reference-equal to the previous render, the child is skipped. |
| 17 | **A**  | React re-renders children by default whenever the parent renders, regardless of props. The child receives a new set of prop objects and React recurses into it. `React.memo` opts out of this default. |
| 18 | **C**  | `React.memo` uses `Object.is` for each prop. `{ color: 'red' }` is a new object literal on every render — a different reference — so `Object.is(prev.style, next.style)` is `false` and the child re-renders. |
| 19 | **D**  | Moving the object to module scope or wrapping it in `useMemo(() => ({ color: 'red' }), [])` gives a stable reference. `React.memo`'s shallow comparison then sees equality and skips the render. |
| 20 | **A**  | `useLayoutEffect` fires in the same synchronous pass as DOM mutations, before the browser gets a chance to paint. Use it to measure or adjust layout (e.g. tooltip positioning) so the user never sees a flash. |
| 21 | **B**  | `items.push(4)` mutates the existing array in place; the reference stored in state is still the same object. React's `Object.is` check sees no change and skips the re-render. Always create a new array. |
| 22 | **C**  | `[...items, newItem]` creates a new array reference, which React detects as a state change and schedules a re-render. `push` (option A) returns the length; option B mutates in place. |
| 23 | **D**  | `useReducer` separates "what happened" (actions) from "how state changes" (reducer). It is well-suited to state with multiple sub-values or complex transition logic. `dispatch` is stable across renders (no need for `useCallback`). |
| 24 | **B**  | An `async` function always returns a Promise. `useEffect` treats its callback's return value as a cleanup function — if it's a Promise instead, cleanup never runs, and React may warn about missing cleanup. |
| 25 | **A**  | The standard pattern: `useEffect(() => { async function load() { … } load(); }, [dep])`. The outer callback is synchronous (returns `undefined` or a cleanup function); the async work is internal. |
| 26 | **C**  | If `id` changes rapidly, multiple fetches are in-flight simultaneously. An older (slower) response arriving after a newer one will call `setData` with stale data. Fix: use an `AbortController` or a cancelled-flag cleanup. |
| 27 | **D**  | In development, `StrictMode` intentionally double-invokes render functions and effects to expose impure renders and missing cleanups. It has no effect in production. |
| 28 | **A**  | Before React 18, only React event handlers were batched. React 18 batches all updates — inside `setTimeout`, Promises, `addEventListener` callbacks — into a single re-render. Use `flushSync` to opt out. |
| 29 | **D**  | Without `forwardRef`, a `ref` prop on a function component is ignored (and produces a warning). `forwardRef` lets the parent wire a ref directly to a DOM element or imperative handle inside the child. |
| 30 | **A**  | `useImperativeHandle(ref, () => ({ focus, reset }), [])` replaces the raw DOM node the parent would normally receive with a curated object exposing only the intended API. |
| 31 | **D**  | Every render of `App` evaluates `{ user, setUser }`, producing a new object. `useContext` consumers compare the value by reference (`Object.is`), so they all re-render even when `user` has not changed. |
| 32 | **A**  | `useMemo(() => ({ user, setUser }), [user])` produces the same object reference when `user` is unchanged, so consumers do not re-render unnecessarily. `setUser` is already stable — no need to list it. |
| 33 | **D**  | Changing `key` is the idiomatic way to force a full remount. React treats the new key as a new identity, unmounts the old tree (running cleanups), and mounts a fresh instance with default state. |
| 34 | **C**  | `ReactDOM.createPortal(child, domNode)` renders `child` into `domNode` (e.g. `document.body`) while keeping it in the React component tree. Events still bubble up through React's synthetic event system. |
| 35 | **A**  | Error boundaries must be class components because no hook equivalent exists for `getDerivedStateFromError`. They catch errors during rendering, in lifecycle methods, and in constructors of the tree below them. Function components can be wrapped in an error boundary class. |
| 36 | **B**  | `React.lazy` integrates with the module bundler's dynamic `import()`. The component's code is not downloaded until the first render, shrinking the initial bundle. |
| 37 | **A**  | While the lazy component loads, React throws a special Promise. The nearest `<Suspense>` boundary catches it and renders `fallback` until the Promise resolves and the real component is ready. |
| 38 | **C**  | `flushSync` exits React's normal batching. All state updates inside the callback are processed immediately and synchronously committed to the DOM before `flushSync` returns. Useful for integrating with third-party DOM libraries. |
| 39 | **D**  | `ReactDOM.render` is the legacy synchronous root. `createRoot` opts the tree into React 18's concurrent scheduler, enabling time-slicing, automatic batching, Suspense on data, and `startTransition`. |
| 40 | **A**  | `startTransition` marks an update as "interruptible". If a higher-priority event (a keystroke, a click) arrives while React is working on the transition, React pauses, handles the urgent event first, then resumes. |
| 41 | **C**  | Without `act()`, state updates and effects may still be pending when your `expect` runs, producing false positives or flaky tests. `act()` drains the React work queue before control returns. |
| 42 | **A**  | The `use` prefix is a contract, not a technical requirement. It tells linters (and humans) that the function may call hooks and must follow the Rules of Hooks. Any such function is a custom hook. |
| 43 | **D**  | `useContext` subscribes the component to the nearest Provider above it. Whenever the Provider's `value` changes (by reference), every consumer re-renders — even those that only care about a sub-field. Split contexts or memoize selectors to reduce this. |
| 44 | **A**  | The render phase is pure: React calls your component function and diffs the output. The commit phase applies mutations to the real DOM, runs `useLayoutEffect`, then (asynchronously) runs `useEffect`. |
| 45 | **B**  | Prop drilling couples intermediate components to data they do not use, making refactoring painful. Context, composition, or state-management libraries are the usual remedies. |
| 46 | **C**  | Inline objects (`{}`) and inline arrow functions (`() => {}`) are allocated at every render call. `React.memo`'s shallow comparison sees a new reference and re-renders the child regardless. The fix is `useMemo` / `useCallback` in the parent. |
| 47 | **D**  | The second argument is `arePropsEqual(prev, next)`. Return `true` to skip the render (props "are equal"). It is the inverse of `shouldComponentUpdate`. Incorrect use can cause stale UI — prefer the default shallow check when possible. |
| 48 | **B**  | `setState` enqueues the update; React processes it asynchronously. The DOM reflects the previous render until React commits the next one. `useLayoutEffect` runs after the commit, making it the right place to read post-update layout. |
| 49 | **B**  | When a lazy component is not yet loaded, React propagates a Promise up the tree. The nearest `<Suspense>` catches it and swaps in `fallback` until the Promise resolves, then replaces the fallback with the loaded component. |
| 50 | **D**  | `[]` means "run once on mount" → mirrors `componentDidMount`. The returned cleanup runs on unmount → mirrors `componentWillUnmount`. `componentDidUpdate` is mirrored by `useEffect` with a non-empty dependency array. |
