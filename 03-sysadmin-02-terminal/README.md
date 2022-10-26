# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"


1. $ type cd
cd is a shell builtin. cd является встроенной командой.
2. $ grep -c <some_string> <some_file>
3. systemd
4. $ ls -l /d 2> /dev/pts/1
5. $ cat < in.txt > out.txt
  или одновременно с выводом на stdout:
  $ cat in.txt | tee out.txt
6. $ echo "text" > /dev/tty4 // находясь в графическом режиме введя данную команду, данные получилв в tty4(ctr+alt+f4)
Вводимы данные в tty4 не получится.
7.$ bash 5>&1 //создание дескриптора 5, перенаправляем в STDOUT
  $ echo netology > /proc/$$/fd/5 //перенаправляем результат команды в дескриптор 5
  netology
8. lsattr ; ls ~ ; ls /ddd  3>&1 1>&2 2>&3 | wc -l //в pipe передается stdout с дескриптором 2 (stderr)
9. cat /proc/$$/environ //Вывод переменных окружения
можно использовать команду env
10. /proc/<pid>/cmdline - файл только на чтение, который содержит строку запуска процессов, кроме зомби-процессов.
/proc/<pid>/exe - сожержит полное имя выполняемого файла для процесса.
11. sse 4_2
12. По умолчанию при запуске команды через SSH не выделяется TTY. Если же не указывать команды, то будет выделение TTY, т. к. предполагается, что будет запущен сеанс оболочки. Возможно использовать ssh -t localhost 'tty' //принужительное создание псевдотерминала
, но

ssh -t localhost 'tty'
vagrant@localhost's password:  //vagrant
/dev/pts/2
Connection to localhost closed.
13. для переноса процесса из другой сессии использовал reptyr <PID>, перед етим естественно запустил sceen для возможности закрыть терминал и оставить процесс работать дальше, но reptyr не работала пока не сделал поправил /proc/sys/kernel/yama/ptrace_scope // тоесть записал 0, root$ echo 0 > /proc/sys/kernel/yama/ptrace_scope

ptrace_scope on Ubuntu Maverick and up
reptyr depends on the ptrace system call to attach to the remote program. On Ubuntu Maverick and higher, this ability is disabled by default for security reasons. You can enable it temporarily by doing

# echo 0 > /proc/sys/kernel/yama/ptrace_scope
as root, or permanently by editing the file /etc/sysctl.d/10-ptrace.conf, which also contains more information about exactly what this setting accomplishes.

14. Команда tee читает из стандартного ввода и записывает как в стандартный вывод, так и в один или несколько файлов одновременно. 
...почему в отличие от sudo echo команда с sudo tee будет работать. Она будет работать, т.к. tee запущена с повышением привилегий(sudo), а не как в предыдущем примере, где перенаправление > под обычным пользователем.