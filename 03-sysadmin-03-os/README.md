1. chdir("/temp")
2. Вот что получилось найти:
newfstatat(AT_FDCWD, "/home/vagrant/.magic.mgc", 0xffffee3f8788, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/vagrant/.magic", 0xffffee3f8788, 0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}, 0) = 0
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
3. Один из вариантов это найти удаленный файл lsof | grep -i del
и далее echo " " > /proc/<PID>/fd/<номер дескриптора>
4. Зомби не занимают памяти (как процессы-сироты), но блокируют записи в таблице процессов, размер которой ограничен для каждого пользователя и системы в целом.
5. root@vagrant:~# opensnoop-bpfcc 
PID    COMM               FD ERR PATH
390    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.procs
390    systemd-udevd      14   0 /sys/fs/cgroup/unified/system.slice/systemd-udevd.service/cgroup.threads
855    vminfo              6   0 /var/run/utmp
632    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
632    dbus-daemon        21   0 /usr/share/dbus-1/system-services
632    dbus-daemon        -1   2 /lib/dbus-1/system-services
632    dbus-daemon        21   0 /var/lib/snapd/dbus-1/system-services/
640    irqbalance          6   0 /proc/interrupts
640    irqbalance          6   0 /proc/stat
640    irqbalance          6   0 /proc/irq/20/smp_affinity
640    irqbalance          6   0 /proc/irq/0/smp_affinity
6. Part of the utsname information is also accessible via /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.
7. 