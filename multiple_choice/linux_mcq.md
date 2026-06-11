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
