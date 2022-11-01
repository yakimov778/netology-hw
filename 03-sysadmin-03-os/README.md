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
5. 