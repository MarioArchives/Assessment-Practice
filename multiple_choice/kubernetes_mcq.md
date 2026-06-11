# Kubernetes Multiple Choice Questions

---

**Q1.** What is the smallest deployable unit in Kubernetes?

A) Container
B) Pod
C) Deployment
D) Node

---

**Q2.** A `Deployment` is to a `ReplicaSet` as a manager is to a worker. What does the Deployment add on top of a ReplicaSet?

A) The ability to run multiple replicas
B) Rolling updates, rollback history, and update strategy management
C) Pod scheduling onto specific nodes
D) Persistent storage for stateful workloads

---

**Q3.** Which Service type exposes an application **only within the cluster** (no external access)?

A) NodePort
B) LoadBalancer
C) ClusterIP
D) ExternalName

---

**Q4.** You need to store a database password as a Kubernetes object and inject it into a Pod as an env var. Which resource type is most appropriate?

A) ConfigMap
B) Secret
C) PersistentVolume
D) ServiceAccount

---

**Q5.** What is the role of `etcd` in a Kubernetes cluster?

A) It is the container runtime that runs pods
B) It is the distributed key-value store that holds all cluster state
C) It is the network plugin that assigns IPs to pods
D) It is the scheduler that places pods onto nodes

---

**Q6.** A `DaemonSet` ensures:

A) Exactly N replicas of a pod run across the cluster
B) One replica of a pod runs on **every** (or selected) node
C) Pods are started in a specific ordered sequence
D) Jobs run to completion exactly once

---

**Q7.** What is the difference between a liveness probe and a readiness probe?

A) Liveness probes route traffic; readiness probes restart containers
B) Liveness probes restart the container if it fails; readiness probes remove it from Service endpoints if it fails
C) They are identical; the naming is only a convention
D) Readiness probes only run at container startup; liveness probes run continuously

---

**Q8.** In Kubernetes RBAC, what is the difference between a `Role` and a `ClusterRole`?

A) A `Role` applies to all namespaces; a `ClusterRole` applies to one namespace
B) A `Role` is namespace-scoped; a `ClusterRole` applies cluster-wide (and to non-namespaced resources)
C) `ClusterRole` can only be bound to service accounts, not users
D) There is no functional difference; only naming differs

---

**Q9.** A node is tainted with `key=value:NoSchedule`. Which statement is true?

A) No pods can run on this node under any circumstances
B) Pods without a matching toleration will not be scheduled onto this node
C) All existing pods on the node are immediately evicted
D) Only pods with `nodeSelector: key=value` can run on this node

---

**Q10.** What happens when a `PersistentVolumeClaim` (PVC) is deleted but its bound `PersistentVolume` (PV) has `reclaimPolicy: Retain`?

A) The PV is deleted along with the PVC
B) The PV is released but its data is preserved; it must be manually reclaimed
C) The PV is immediately made available for new PVCs
D) The PV is automatically scrubbed and re-bound to the next pending PVC

---

**Q11.** Which resource would you use to **run a batch job to completion** (not a continuously running service)?

A) Deployment
B) StatefulSet
C) Job
D) DaemonSet

---

**Q12.** An `initContainer` in a Pod spec:

A) Runs alongside the main containers in parallel
B) Runs to completion before any main containers start
C) Provides sidecar functionality such as log shipping
D) Replaces the main container if it fails to start

---

**Q13.** You run `kubectl apply -f deployment.yaml`. The Deployment already exists. What happens?

A) The command fails with "AlreadyExists"
B) The existing Deployment is deleted and recreated
C) The existing Deployment is patched with the changes from the file (declarative update)
D) Nothing; `apply` only creates new resources

---

**Q14.** Which `kubectl` command shows the rollout history of a Deployment?

A) `kubectl describe deployment <name>`
B) `kubectl rollout history deployment/<name>`
C) `kubectl get deployment <name> -o yaml`
D) `kubectl logs deployment/<name>`

---

**Q15.** What does a `HorizontalPodAutoscaler` (HPA) scale based on by default?

A) Memory usage only
B) CPU utilization (and optionally custom/external metrics)
C) Number of incoming HTTP requests, measured via Ingress
D) Node disk I/O

---

**Q16.** What is the difference between resource **requests** and resource **limits** in a Pod spec?

A) Requests are enforced at runtime; limits are only advisory
B) Requests are used by the scheduler to find a suitable node; limits cap the resource usage at runtime
C) Limits are used by the scheduler; requests cap runtime usage
D) They are interchangeable; both serve the same purpose

---

**Q17.** A `NetworkPolicy` that selects a set of pods and specifies no `ingress` rules:

A) Allows all ingress traffic to the selected pods
B) Denies all ingress traffic to the selected pods
C) Has no effect on ingress traffic
D) Blocks only external (outside-cluster) ingress

---

**Q18.** In Helm, what is a `values.yaml` file used for?

A) Defining the Kubernetes API version and kind for all chart resources
B) Providing default configuration values that templates reference with `{{ .Values.* }}`
C) Declaring the chart's dependencies on other Helm charts
D) Storing secrets that are encrypted before being committed to the chart

---

**Q19.** What does `kubectl port-forward pod/<name> 8080:80` do?

A) Exposes port 80 on the pod to the internet via NodePort 8080
B) Forwards local port 8080 on your machine to port 80 on the pod
C) Changes the pod's container port from 80 to 8080
D) Creates a Service of type NodePort on port 8080

---

**Q20.** A `StatefulSet` provides which guarantee that a `Deployment` does not?

A) Higher availability through more replicas
B) Stable network identities and persistent storage per pod, with ordered deployment/scaling
C) Automatic rollback on failed updates
D) Node affinity for co-locating pods on the same host

---

**Q21.** Which command opens an interactive shell inside a running container?

A) `kubectl exec -it <pod> -- /bin/sh`
B) `kubectl run <pod> --it`
C) `kubectl attach <pod> --interactive`
D) `kubectl debug <pod> --shell`

---

**Q22.** What are the three QoS classes Kubernetes assigns to Pods, from highest to lowest priority?

A) Critical, Standard, Minimal
B) Guaranteed, Burstable, BestEffort
C) High, Medium, Low
D) Reserved, Shared, Open

---

**Q23.** Which Pod phase indicates all containers have terminated successfully and none will be restarted?

A) `Running`
B) `Completed`
C) `Succeeded`
D) `Terminated`

---

**Q24.** What does a `PodDisruptionBudget` (PDB) guarantee?

A) Pods are evenly distributed across all nodes
B) Pods are never evicted under any circumstances
C) A maximum number of Pods allowed in a namespace
D) A minimum number (or percentage) of Pods remain available during voluntary disruptions

---

**Q25.** What does a `CronJob` add on top of a regular `Job`?

A) A cron-schedule for automatically creating Jobs at specified times
B) The ability to run pods to completion
C) Parallel execution of multiple pods
D) Persistent storage for job output

---

**Q26.** A Pod where every container has `requests` and `limits` set to identical values falls into which QoS class?

A) Burstable
B) Guaranteed
C) BestEffort
D) Reserved

---

**Q27.** What does `kubectl rollout undo deployment/<name>` do?

A) Deletes the Deployment and recreates it from scratch
B) Scales the Deployment to zero replicas
C) Rolls back to the previous ReplicaSet revision
D) Pauses the current rollout

---

**Q28.** An `emptyDir` volume:

A) Persists data after the Pod is deleted
B) Is backed by a PersistentVolume automatically
C) Can only be used by one container at a time
D) Is created when the Pod starts and deleted when the Pod is removed from the node

---

**Q29.** Which resource type stores non-sensitive configuration data for use by Pods as env vars or mounted files?

A) ConfigMap
B) Secret
C) PersistentVolumeClaim
D) ServiceAccount

---

**Q30.** What does `kubectl top pods` require to function?

A) Prometheus installed in the cluster
B) The Metrics Server to be running
C) `kubectl` version 1.25 or higher
D) Nodes with at least 8 GB of RAM

---

**Q31.** In a Service spec, what does `sessionAffinity: ClientIP` do?

A) Encrypts traffic from specific client IPs
B) Restricts the Service to in-cluster clients only
C) Routes all traffic from the same client IP to the same backend Pod
D) Balances traffic based on client geolocation

---

**Q32.** The Kubernetes control-plane component responsible for assigning a node to newly created Pods with no node assigned is:

A) kube-apiserver
B) etcd
C) kube-controller-manager
D) kube-scheduler

---

**Q33.** What does `kubectl cp <pod>:/remote/path ./local/path` do?

A) Copies a file from a container to your local filesystem
B) Creates a ConfigMap from a local file
C) Clones a Pod spec to a new namespace
D) Copies a Kubernetes resource definition between namespaces

---

**Q34.** A `ResourceQuota` applied to a namespace:

A) Limits the CPU and memory of individual Pods
B) Sets aggregate limits on total resource consumption and object counts within the namespace
C) Prevents all Pods from being scheduled on the same node
D) Enforces a minimum number of replicas for every Deployment

---

**Q35.** What is the difference between `kubectl create` and `kubectl apply`?

A) `create` is declarative; `apply` is imperative
B) `apply` only works with Deployments
C) `create` fails if the resource already exists; `apply` creates or patches existing resources
D) They are interchangeable for all resource types

---

**Q36.** What is the difference between `kubectl cordon` and `kubectl drain`?

A) `cordon` evicts existing pods; `drain` only blocks new scheduling
B) `drain` is for namespaces; `cordon` is for nodes
C) They are equivalent; both only affect scheduling
D) `cordon` marks a node unschedulable for new pods; `drain` also evicts existing pods from the node

---

**Q37.** What is the sidecar container pattern?

A) An additional container in the same Pod that augments the main container (e.g. log shipping, Envoy proxy)
B) A container that runs before the main container to set up prerequisites
C) A container that monitors the main container and restarts it on failure
D) A container in a separate Pod that shares a volume with the main Pod

---

**Q38.** `kubectl apply -f deployment.yaml` when the Deployment already exists:

A) Fails with "AlreadyExists"
B) Patches the existing Deployment with the changes from the file (declarative update)
C) Deletes and recreates the Deployment
D) Does nothing; `apply` only creates new resources

---

**Q39.** Which field in a Pod spec controls what happens when a container exits?

A) `lifecycle.postStart`
B) `terminationMessagePolicy`
C) `restartPolicy`
D) `activeDeadlineSeconds`

---

**Q40.** What is the function of `kube-proxy` on each node?

A) Proxies kubectl commands to pods on behalf of the API server
B) Runs the container runtime on each node
C) Monitors node health and reports to the control plane
D) Maintains network rules (iptables/ipvs) to implement Service virtual IPs and load balancing

---
