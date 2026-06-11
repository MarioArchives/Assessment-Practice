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
