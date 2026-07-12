# Linux Multiple Choice Questions

---

**Q1.** What is the primary role of the Linux kernel?

A) Manage hardware resources and provide services to user-space programs via system calls
B) Interpret commands typed by the user and launch programs
C) Provide the graphical desktop environment
D) Store and retrieve files on disk

---

**Q2.** What is the key difference between kernel space and user space?

A) Kernel space runs in RAM; user space runs in swap
B) Kernel space runs with full hardware privileges; user space runs with restricted privileges and must use system calls to access hardware
C) User space has direct access to hardware; kernel space is sandboxed
D) They are the same; the distinction is only historical

---

**Q3.** When the Linux kernel loads a new process, it provides:

A) A fixed 4 MB region of physical RAM
B) A single shared address space used by all processes
C) A virtual address space that appears private to the process, backed by physical memory via the MMU
D) A region of swap space only, until physical RAM is available

---

**Q4.** Linux namespaces are used to:

A) Name containers in an image registry
B) Group kernel modules by function
C) Define the shell environment for a user session
D) Isolate a process's view of system resources (PID, network, mount, UTS, IPC, user)

---

**Q5.** The Linux kernel is best described as:

A) A monolithic kernel — most drivers and subsystems run in kernel space, with loadable module support
B) A microkernel — most drivers run in user space
C) An exokernel — hardware is exposed directly to applications
D) A hybrid kernel — exactly half of the drivers run in user space

---

**Q6.** What is a shell?

A) The kernel's hardware abstraction layer
B) A user-space program that interprets user commands and launches other programs
C) A type of filesystem for storing executables
D) The daemon that manages system services at boot

---

**Q7.** What does the `PATH` environment variable control?

A) The user's home directory location
B) The current working directory
C) The list of directories searched left-to-right when a command is typed without a full path
D) The user's default login shell

---

**Q8.** What does `source ~/.bashrc` (equivalently `. ~/.bashrc`) do?

A) Creates a subshell, runs ~/.bashrc in it, then exits
B) Restarts the login shell
C) Installs all packages listed in ~/.bashrc
D) Executes ~/.bashrc in the current shell process, applying variable and alias definitions immediately

---

**Q9.** What is a shell built-in command?

A) A command implemented inside the shell itself, not as a separate executable on disk
B) A command stored in `/usr/bin`
C) A command that requires root privileges to execute
D) A command specific to bash that cannot run in other shells

---

**Q10.** The PATH entry `/usr/local/bin:/usr/bin:/bin` means:

A) These directories are searched in reverse order (right to left)
B) These directories are searched left to right; the first match wins
C) All matching executables from all three directories are executed
D) Only `/bin` is searched; the others are fallbacks

---

**Q11.** What is `systemd`?

A) A shell configuration daemon that manages environment variables
B) A log rotation utility used to compress old log files
C) The init system (PID 1) on most modern Linux distributions, responsible for starting services and managing the system lifecycle
D) A kernel module for managing block devices

---

**Q12.** Which command starts a systemd service **and** also enables it to start at every future boot?

A) `systemctl start <service>`
B) `systemctl enable <service>`
C) `service <name> start --persist`
D) `systemctl enable --now <service>`

---

**Q13.** How do you view recent logs for a specific systemd service?

A) `journalctl -u <service>`
B) `cat /var/log/<service>.log`
C) `systemctl logs <service>`
D) `dmesg | grep <service>`

---

**Q14.** A systemd unit file with `Type=oneshot` in `[Service]` means:

A) The process must fork; systemd tracks the child PID
B) systemd considers the service active only after the process exits; suitable for scripts that run to completion
C) The service is started once at boot and cannot be restarted
D) The service is socket-activated

---

**Q15.** Which systemd target is roughly equivalent to the traditional "multi-user" runlevel with networking but no GUI?

A) `rescue.target`
B) `graphical.target`
C) `multi-user.target`
D) `default.target`

---

**Q16.** What is a system call?

A) A function call between two user-space processes
B) A signal sent from the kernel to a process
C) A call to a shared library function in libc
D) The mechanism by which a user-space program requests a service from the kernel, causing a privilege transition to kernel mode

---

**Q17.** Which system call(s) create a new process on Linux?

A) `fork()` / `clone()`
B) `exec()`
C) `spawn()`
D) `create()`

---

**Q18.** What does `strace` do?

A) Profiles CPU usage of a running process
B) Traces system calls and signals issued by a process
C) Displays memory allocation patterns
D) Monitors filesystem changes in real time

---

**Q19.** What does the phrase "everything is a file" mean in Linux?

A) All data must be stored in plain text files
B) All processes share a single file descriptor table
C) Devices, sockets, pipes, and directories are all represented in the VFS and accessed through the same read/write interface
D) The kernel stores all state in /proc

---

**Q20.** What information does an inode store?

A) The file's name and its path in the directory tree
B) The file's contents directly
C) The file's directory entry and parent directory inode
D) The file's metadata (permissions, owner, timestamps, size, data block pointers) but not its name

---

**Q21.** What is a hard link?

A) A directory entry that points directly to the same inode as the original; data is not removed until all hard links are deleted
B) A shortcut file that stores the path to the target
C) A special file that can only be created by root
D) A link that can cross filesystem boundaries

---

**Q22.** What does the `/proc` filesystem provide?

A) Persistent storage for process core dumps
B) A virtual filesystem that exposes kernel and process state as readable files (e.g. `/proc/<pid>/status`, `/proc/cpuinfo`)
C) The location where installed packages are stored
D) A read-only snapshot of the root filesystem for recovery purposes

---

**Q23.** What does `df -h` show?

A) The disk usage of the current directory tree
B) The size of individual files in the current directory
C) Disk space usage of all mounted filesystems in human-readable form
D) The inode usage per filesystem

---

**Q24.** In the permission string `rwxr-x---`, what can members of the file's group do?

A) Read, write, and execute
B) Nothing — no permissions at all
C) Read and write only
D) Read and execute only

---

**Q25.** What does the `setuid` bit on an executable do?

A) Runs the executable with the file owner's privileges, not the invoking user's
B) Allows any user to write to the file
C) Automatically sets the file's group ID to root
D) Makes the file immutable

---

**Q26.** Which command changes the owning user of a file?

A) `chmod newowner file`
B) `chown newowner file`
C) `chgrp newowner file`
D) `usermod file`

---

**Q27.** What does `chmod 644 file` set?

A) Owner: read/write/execute; Group: read; Others: read
B) Owner: read/write; Group: read/write; Others: read
C) Owner: read/write; Group: read only; Others: read only
D) Owner: read/write; Group: read/execute; Others: read

---

**Q28.** What does `sudo` do?

A) Switches to the root user permanently for the session
B) Changes file permissions to allow all users access
C) Authenticates the user and grants an unlimited root shell
D) Runs a single command with elevated (typically root) privileges, then returns to the invoking user's identity

---

**Q29.** What is swap space?

A) A disk area (partition or file) used by the kernel as overflow when physical RAM is full, by paging out less-used memory pages
B) A region of RAM reserved exclusively for the kernel
C) A CPU cache buffer for frequently accessed data
D) The `/tmp` directory used for temporary files by running processes

---

**Q30.** What does the `vm.swappiness` kernel parameter control?

A) The maximum size of the swap partition
B) How aggressively the kernel swaps memory pages to disk (0 = avoid; 100 = aggressive)
C) The encryption algorithm used for swap space
D) Whether swap is enabled at boot

---

**Q31.** Which command shows current memory and swap usage in human-readable form?

A) `df -h`
B) `vmstat -s`
C) `free -h`
D) `top -b -n 1`

---

**Q32.** What are Linux cgroups used for in the context of containers?

A) Isolating the filesystem view of each container via mount namespaces
B) Providing a separate network stack to each container
C) Managing container image layers on disk
D) Limiting and accounting for resource usage (CPU, memory, I/O) for groups of processes

---

**Q33.** What is the difference between a container image and a running container?

A) An image is a read-only layered snapshot; a container adds a writable layer on top and is an executing process
B) A container is stored on disk; an image runs in memory
C) They are the same thing viewed from different perspectives
D) An image can only produce one container at a time

---

**Q34.** What happens to a Docker container's writable layer after its process exits?

A) It is automatically committed back to the base image
B) It persists on disk until the container is explicitly removed with `docker rm`
C) It is deleted immediately when the process exits
D) It is merged with the base image layer on the next `docker build`

---

**Q35.** Containers differ from virtual machines in that containers:

A) Provide stronger isolation because each has its own kernel
B) Cannot run on the same host as virtual machines
C) Share the host kernel and use namespaces/cgroups for isolation, making them more lightweight
D) Require a hypervisor to network together

---

**Q36.** What does `ls -la` display?

A) Only hidden files (those beginning with `.`)
B) Files sorted by last access time
C) Symbolic links only
D) All files including hidden ones, in long format showing permissions, owner, size, and timestamps

---

**Q37.** What does `grep -r "error" /var/log/` do?

A) Recursively searches all files under `/var/log/` for lines containing "error"
B) Replaces every occurrence of "error" with nothing in all log files
C) Searches only the top-level files in `/var/log/` (not subdirectories)
D) Creates a file named "error" in `/var/log/`

---

**Q38.** What does `ps aux` display?

A) Only processes owned by the current user
B) All running processes for all users with their CPU and memory usage
C) Only kernel threads
D) Process priority (nice) values only

---

**Q39.** What does `command > file.txt 2>&1` do?

A) Appends both stdout and stderr of `command` to `file.txt`
B) Redirects only stderr to `file.txt`, leaving stdout on the terminal
C) Redirects both stdout and stderr of `command` to `file.txt`, overwriting it
D) Reads `file.txt` as stdin while discarding all output

---

**Q40.** What does the pipe operator `|` do in `ls -l | grep ".txt"`?

A) Appends the output of `ls -l` to the input buffer of `grep`
B) Runs both commands simultaneously, sharing CPU time between them
C) Saves the output of `ls -l` to a temp file, then `grep` reads that file
D) Connects the stdout of `ls -l` directly to the stdin of `grep`, without an intermediate file

---

**Q41.** Which Linux namespace type gives a container its own process ID tree with a private PID 1?

A) UTS namespace
B) Net namespace
C) PID namespace
D) IPC namespace

---

**Q42.** When you type `ls -l /tmp` in bash, which sequence of operations occurs?

A) The shell directly calls the kernel to list the directory without forking
B) The shell sends the command to a background daemon for execution
C) The kernel's built-in command interpreter handles it directly
D) The shell calls `fork()`, the child calls `exec()` with `/bin/ls`, the kernel runs `ls`, output is written to stdout, then the child exits

---

**Q43.** What does `systemctl disable --now nginx` do?

A) Stops the nginx service immediately AND removes the symlinks that would start it at next boot
B) Stops nginx but leaves the boot symlinks in place
C) Removes the boot symlinks but does not stop the currently running service
D) Deletes the nginx unit file from disk

---

**Q44.** `df -h` shows a filesystem at 95% full, but `du -sh /` accounts for far less data than the disk capacity. What is the most likely explanation?

A) `df` includes swap space in its measurement
B) Files were deleted but are still held open by a running process, keeping the blocks allocated while `du` cannot see them
C) `/proc` and `/sys` consume disk space that `du` misses
D) `df` counts inodes, not actual data blocks

---

**Q45.** When you run `rm file.txt`, what precisely happens at the filesystem level?

A) The inode and data blocks are immediately freed
B) The file is moved to a hidden `.trash` directory
C) The directory entry is removed and the inode's link count is decremented; inode and data blocks are freed only when the count reaches 0
D) The data blocks are zeroed out before being freed for security

---

**Q46.** Why can hard links NOT span different filesystems (e.g. linking from `/` to `/mnt/data`)?

A) It is a security restriction the kernel enforces to prevent privilege escalation
B) Different filesystems use incompatible on-disk formats
C) The kernel simply has not implemented cross-filesystem hard links yet
D) Inode numbers are only unique within a single filesystem; a hard link on a different filesystem would reference an arbitrary or wrong inode

---

**Q47.** What does `chmod +x script.sh` do?

A) Adds execute permission for the owner, group, and others (equivalent to `chmod a+x`)
B) Adds execute permission for the owner only
C) Sets permissions to exactly `--x--x--x`, removing all read and write bits
D) Removes execute permission from all

---

**Q48.** What does `chown -R alice:developers /project` do?

A) Changes only `/project`'s owner to `alice` and group to `developers`
B) Recursively changes the owner to `alice` and the group to `developers` for `/project` and everything inside it
C) Only changes the group; `-R` is not valid with `chown`
D) Grants `alice` and `developers` read/write access via ACLs

---

**Q49.** In `free -h` output, what does the "available" column represent?

A) The same as "free" — completely unused physical RAM
B) Total RAM minus the size of swap
C) An estimate of memory available to new processes without swapping, including reclaimable page cache and buffers
D) The maximum RAM the system could use if all swap were disabled

---

**Q50.** A container is started with `--memory=256m`. Its process keeps allocating memory and exceeds the limit. What happens?

A) The container is paused until other containers release memory
B) The container is allowed to exceed the limit temporarily, then CPU-throttled as a penalty
C) The container is stopped and automatically restarted by the runtime
D) The kernel OOM killer terminates a process inside the container's cgroup to bring usage back under the limit

---

**Q51.** What is a signal in Linux?

A) A message written to a process's stdin by the kernel
B) An asynchronous notification delivered by the kernel to a process, interrupting its normal flow to trigger a handler or a default action
C) A synchronous function call between two cooperating processes
D) A hardware interrupt handled entirely inside the kernel

---

**Q52.** What is the key difference between `SIGTERM` and `SIGKILL`?

A) `SIGTERM` only works on child processes; `SIGKILL` works on any process
B) `SIGKILL` asks politely; `SIGTERM` forces immediate termination
C) `SIGTERM` (15) can be caught, handled, or ignored, allowing graceful shutdown; `SIGKILL` (9) cannot be caught or ignored — the kernel terminates the process immediately
D) They are identical except for their numeric values

---

**Q53.** Which signal does `kill 1234` send by default?

A) `SIGTERM` (15)
B) `SIGKILL` (9)
C) `SIGINT` (2)
D) `SIGHUP` (1)

---

**Q54.** Which two signals can NEVER be caught, blocked, or ignored by a process?

A) `SIGTERM` and `SIGINT`
B) `SIGSEGV` and `SIGABRT`
C) `SIGHUP` and `SIGQUIT`
D) `SIGKILL` and `SIGSTOP`

---

**Q55.** Pressing `Ctrl+C` in a terminal sends:

A) `SIGKILL` to the shell
B) `SIGINT` to the foreground process group
C) `SIGTERM` to the most recently started process
D) `SIGQUIT` to all processes owned by the user

---

**Q56.** What is the difference between `SIGTSTP` (sent by `Ctrl+Z`) and `SIGSTOP`?

A) `SIGTSTP` stops the process permanently; `SIGSTOP` is temporary
B) They are two names for the same signal
C) `SIGTSTP` can be caught or ignored by the process; `SIGSTOP` cannot — it always suspends the process
D) `SIGSTOP` only works on background jobs

---

**Q57.** By convention, what does sending `SIGHUP` to a daemon like nginx typically do?

A) Causes it to reload its configuration files without a full restart
B) Terminates it immediately without cleanup
C) Suspends it until `SIGCONT` is received
D) Forces it to rotate its log files and exit

---

**Q58.** What does `nohup long_job.sh &` accomplish?

A) Runs the job with higher scheduling priority in the background
B) Restarts the job automatically if it crashes
C) Prevents the job from writing to the terminal
D) Makes the job ignore `SIGHUP`, so it keeps running after the terminal that started it closes

---

**Q59.** You run `kill -9 1234` but the process does not die; `ps` shows its state as `D`. Why?

A) The process has caught and ignored `SIGKILL`
B) The process is in uninterruptible sleep (usually blocked on I/O, e.g. a hung NFS mount); the signal is only acted upon when the kernel operation completes
C) You need to use `kill -SIGKILL` instead of `kill -9`
D) PID 1234 is a kernel thread that cannot receive signals

---

**Q60.** When is `SIGSEGV` delivered to a process?

A) When it exceeds its CPU time limit
B) When it divides by zero
C) When it accesses memory outside its valid virtual address space (e.g. dereferencing an invalid pointer)
D) When it opens too many file descriptors

---

**Q61.** In a bash script, what does `trap 'rm -f "$TMPFILE"' EXIT INT TERM` do?

A) Registers a handler that removes the temp file when the script exits normally or receives `SIGINT`/`SIGTERM`
B) Blocks `SIGINT` and `SIGTERM` so the script cannot be interrupted
C) Sends `SIGINT` and `SIGTERM` to the process holding `$TMPFILE` open
D) Deletes the temp file immediately, then exits the script

---

**Q62.** What is `SIGCHLD` and why does it matter?

A) A signal a child sends to request more memory from its parent
B) The signal used by the shell to launch child processes
C) A deprecated signal replaced by `waitpid()`
D) A signal delivered to a parent when a child terminates or stops; the parent should then call `wait()`/`waitpid()` to reap the child's exit status

---

**Q63.** What is a zombie process?

A) A process that survived `kill -9` and keeps consuming CPU
B) A process that has terminated but whose parent has not yet called `wait()` to collect its exit status; only its process-table entry remains
C) A background process detached from any terminal
D) A process stuck in uninterruptible sleep

---

**Q64.** How do you send `SIGUSR1` to a running process named `myapp` without looking up its PID first?

A) `kill -USR1 myapp`
B) `signal myapp SIGUSR1`
C) `pkill -USR1 myapp`
D) `killall -9 myapp`

---

**Q65.** What is the fundamental difference between a process and a thread?

A) Threads in a process share the same virtual address space, heap, and file descriptors, but each has its own stack and registers; separate processes have isolated address spaces
B) Threads run in kernel space; processes run in user space
C) A process can only contain one thread on Linux
D) Threads cannot make system calls; only their parent process can

---

**Q66.** How does the Linux kernel implement threads?

A) As green threads scheduled entirely by glibc in user space
B) As special kernel-space processes that cannot be scheduled independently
C) Through a dedicated `thread_create()` system call unrelated to process creation
D) As tasks created with `clone()` using flags like `CLONE_VM` and `CLONE_FILES` to share resources; the scheduler treats every task the same way

---

**Q67.** In a multithreaded program, what does `getpid()` return when called from different threads?

A) A different PID for each thread
B) The same value in every thread — the thread group ID (TGID); `gettid()` returns each thread's unique TID
C) The PID of whichever thread called it first
D) The parent process's PID

---

**Q68.** What does copy-on-write mean for `fork()`?

A) The child gets an immediate full copy of the parent's memory
B) The child can read but never write the parent's memory
C) Parent and child initially share the same physical pages marked read-only; a page is copied only when either process writes to it
D) The kernel writes the parent's memory to swap before creating the child

---

**Q69.** What happens when a process calls `execve()`?

A) Its address space is replaced with the new program's image; the PID stays the same and open file descriptors remain open unless marked close-on-exec
B) A new child process is created running the new program
C) The old program keeps running in parallel with the new one
D) The process is suspended until the new program finishes

---

**Q70.** What happens to a child process whose parent dies before it does (an orphan)?

A) The kernel kills it immediately with `SIGKILL`
B) It becomes a zombie until the system reboots
C) It is suspended until a new parent adopts it manually
D) It is re-parented to PID 1 (or the nearest subreaper), which will reap it when it exits

---

**Q71.** Which command shows the individual threads of process 1234?

A) `ps -ef | grep 1234`
B) `ps -T -p 1234` (or `top -H -p 1234`)
C) `pstree -a 1234`
D) `cat /proc/1234/cmdline`

---

**Q72.** What is the range and meaning of process nice values?

A) 0 to 100, where 100 is the highest priority
B) 1 to 99, used only for real-time processes
C) -20 (highest priority) to 19 (lowest priority); `renice` adjusts it for a running process
D) -100 to 100, where negative values pause the process

---

**Q73.** Why is a context switch between two threads of the same process cheaper than between two processes?

A) No address-space switch is needed — the page tables and most TLB entries stay valid because both threads share the same virtual memory
B) Thread switches happen in user space without kernel involvement
C) Threads do not need their registers saved and restored
D) The kernel batches thread switches together once per second

---

**Q74.** One thread in a multithreaded server dereferences a NULL pointer. What happens?

A) Only that thread dies; the others continue unaffected
B) The kernel restarts the failed thread automatically
C) The thread blocks until the memory becomes valid
D) The whole process receives `SIGSEGV` and (by default) terminates — all threads share the process's fate

---

**Q75.** Which of the following is NOT a systemd unit type?

A) `.timer`
B) `.socket`
C) `.mount`
D) `.cron`

---

**Q76.** Where should an administrator place a custom unit file so it takes precedence over the package-provided one?

A) `/usr/lib/systemd/system/` — the canonical location for all units
B) `/etc/systemd/system/` — units here override same-named units shipped by packages in `/usr/lib/systemd/system/`
C) `/var/lib/systemd/` — the runtime unit directory
D) `~/.systemd/units/` — per-user overrides for system units

---

**Q77.** After editing a unit file on disk, what must you run before the change takes effect?

A) `systemctl reload <service>`
B) `systemctl reset-failed`
C) `systemctl daemon-reload` — systemd re-reads unit files from disk
D) Nothing; systemd watches unit files with inotify

---

**Q78.** What does `systemctl edit nginx` do?

A) Creates a drop-in override file under `/etc/systemd/system/nginx.service.d/`, leaving the original packaged unit file untouched
B) Opens the packaged unit file in `/usr/lib/systemd/system/` for direct editing
C) Edits the nginx configuration in `/etc/nginx/nginx.conf`
D) Renames the unit so the packaged version is disabled

---

**Q79.** What is the difference between `Type=simple` and `Type=forking` in a `[Service]` section?

A) `simple` services restart automatically; `forking` services do not
B) `forking` services run as root; `simple` services run unprivileged
C) `simple` runs the service in a login shell; `forking` does not
D) With `simple`, the `ExecStart` process itself is the main process and is considered started immediately; with `forking`, the process is expected to fork and the parent to exit, with systemd tracking the child (often via `PIDFile=`)

---

**Q80.** What does `Type=notify` mean for a systemd service?

A) systemd emails the administrator when the service changes state
B) The service signals its own readiness explicitly via `sd_notify()`, so systemd only considers it started when the service says it is ready
C) The service is notified by systemd whenever another unit starts
D) journald sends desktop notifications for every log line the service writes

---

**Q81.** With `Restart=on-failure`, when will systemd restart the service?

A) On any exit, including a clean stop via `systemctl stop`
B) Only when the machine reboots
C) When the process exits with a non-zero code, is killed by a signal, or a timeout/watchdog trips — but not on a clean exit or operator stop
D) Only when the watchdog timer expires

---

**Q82.** In a unit file, what is the difference between `After=network.target` and `Requires=network.target`?

A) `After=` is ordering only (start me later, if both start); `Requires=` is a dependency (pull it in, fail with it) but implies no ordering — robust units declare both
B) They are synonyms; `Requires=` is the deprecated spelling
C) `After=` pulls in the dependency; `Requires=` only orders startup
D) `Requires=` works only for targets; `After=` works only for services

---

**Q83.** How does `Wants=` differ from `Requires=`?

A) `Wants=` also stops the unit when the wanted unit stops
B) `Wants=` is evaluated only at boot; `Requires=` at every start
C) `Wants=` is stronger — it restarts the unit if the wanted unit crashes
D) `Wants=` is a weaker dependency: the wanted unit is started too, but if it fails or is missing, this unit still starts — preferred for robustness

---

**Q84.** What does `systemctl enable myapp` actually do on disk, given `WantedBy=multi-user.target` in the unit's `[Install]` section?

A) Copies the unit file into `/etc/systemd/system/`
B) Creates a symlink `/etc/systemd/system/multi-user.target.wants/myapp.service` pointing to the unit file, so the target pulls it in at boot
C) Appends the service name to `/etc/systemd/system.conf`
D) Sets an `enabled=true` flag inside the unit file

---

**Q85.** How does a systemd timer unit (`backup.timer`) trigger work?

A) The timer file contains an `ExecStart=` line that runs directly
B) It writes an entry into the user's crontab which cron then executes
C) When the timer elapses (e.g. `OnCalendar=daily`), it activates the matching unit — by default the service with the same name (`backup.service`)
D) It sends `SIGALRM` to the target service's main process

---

**Q86.** Which command shows journal logs from the current boot only?

A) `journalctl -b`
B) `journalctl -f`
C) `journalctl --current`
D) `journalctl -u boot`

---

**Q87.** What does `journalctl -p err -u nginx --since "2 hours ago"` show?

A) All nginx log lines from the last two hours, ordered by severity
B) Only lines containing the literal string "err" in nginx logs
C) Error logs from every unit except nginx
D) nginx unit messages from the last two hours at priority `err` or more severe (crit, alert, emerg)

---

**Q88.** How does `systemctl mask <unit>` differ from `systemctl disable <unit>`?

A) `mask` hides the unit from `systemctl list-units` but it still runs
B) `mask` symlinks the unit to `/dev/null`, making it impossible to start — even manually or as a dependency; `disable` only removes the boot symlinks but allows manual and dependency starts
C) They are identical; `mask` is the older name
D) `mask` uninstalls the package that owns the unit

---

**Q89.** What does `systemd-analyze blame` show?

A) The units that failed during the last boot
B) Which unit caused the most recent system crash
C) How long each unit took to initialize during boot, sorted slowest first
D) The dependency tree of the default target

---

**Q90.** How do you make a machine boot to a text console (no GUI) by default?

A) `systemctl set-default multi-user.target`
B) `systemctl isolate multi-user.target`
C) Edit `/etc/inittab` and set runlevel 3
D) `systemctl disable graphical.target`

---

**Q91.** What is `systemctl --user` used for?

A) Showing which user each system service runs as
B) Running system units with sudo privileges dropped
C) Filtering `systemctl` output to units started by the current user
D) Managing per-user systemd units (stored in e.g. `~/.config/systemd/user/`), which run inside the user's session without root

---

**Q92.** What is systemd socket activation?

A) A firewall feature that opens ports for enabled services
B) systemd listens on the service's socket itself and starts the service on the first incoming connection, handing the socket over — enabling on-demand start and parallel boot
C) A mechanism for services to notify systemd over a Unix socket that they crashed
D) Automatic TLS termination for any `.socket` unit

---

**Q93.** Which startup file does bash read for an interactive NON-login shell (e.g. opening a new terminal window in a GUI session)?

A) `/etc/profile` then `~/.bash_profile`
B) `~/.bash_login`
C) `~/.bashrc`
D) `~/.profile` only

---

**Q94.** What is the difference between `FOO=bar` and `export FOO=bar` in a shell?

A) `export` places the variable in the environment so child processes inherit it; without `export` it exists only in the current shell
B) Without `export` the variable is read-only
C) `export` makes the variable persist across reboots
D) There is no difference in bash

---

**Q95.** What does `$?` contain in a shell?

A) The PID of the last background job
B) The number of arguments passed to the script
C) The name of the current shell
D) The exit status of the most recently executed foreground command (0 means success)

---

**Q96.** What does the shell built-in `exec` do when given a command, as in `exec java -jar app.jar`?

A) Runs the command in a new subshell with elevated priority
B) Replaces the shell process itself with the command — same PID, and the shell is gone when the command exits; commonly used in container entrypoint scripts so signals reach the app directly
C) Schedules the command to run when the shell exits
D) Runs the command and prevents it from being killed

---

**Q97.** Why must `cd` be a shell built-in rather than an external program?

A) Changing directories requires root privileges that only the shell has
B) External programs cannot call the `chdir()` system call
C) An external command runs in a child process, so its `chdir()` would only change the child's working directory — the shell's own directory would be unchanged
D) It is only a convention; `/bin/cd` works the same way

---

**Q98.** When you execute a script starting with `#!/usr/bin/env python3`, what handles that first line?

A) The kernel: during `execve()` it detects the `#!` magic, and runs the named interpreter with the script path as argument
B) The shell parses the line and decides which interpreter to spawn
C) Python reads the line to configure its own runtime options
D) systemd resolves the interpreter from its unit configuration

---

**Q99.** What does `dmesg` display?

A) The systemd journal for all units
B) Desktop notification history
C) Mail delivery status messages
D) The kernel ring buffer — boot messages, driver/hardware events, OOM-killer actions, and other kernel log output

---

**Q100.** What is the difference between `modprobe` and `insmod` for loading kernel modules?

A) `insmod` loads modules permanently; `modprobe` only until reboot
B) `modprobe` resolves and loads a module's dependencies automatically (using module name); `insmod` inserts exactly one file with no dependency handling
C) `modprobe` is for network drivers only
D) They are identical; `modprobe` is the modern name

---
