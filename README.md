1. chdir("/tmp")
2. Результат который получил:
stat("/home/vagrant/.magic.mgc", 0x7ffe1ca75f40) = -1 ENOENT (No such file or directory)
stat("/home/vagrant/.magic", 0x7ffe1ca75f40) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
stat("/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}) = 0
openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3
3. 