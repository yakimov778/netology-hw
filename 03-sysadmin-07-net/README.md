# Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

1) Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?

Linux - `ip link` \

Windows - `ipconfig /all`

```bash
vagrant@ubuntu:~$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
```

2) Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?

LLDP – протокол для обмена информацией между соседними устройствами, позволяет определить к какому порту коммутатора подключен сервер.
```bash
sudo apt install lldpd - установка
lldpctl

```

3) Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.

Для разделения L2 коммутатора на несколько виртуальных сетей используется технология VLAN (Virtual Local Area Network).

В Linux можно проверить наличие модуля 8021q. Если он не подгружен, то выполнить команду `sudo modprobe 8021q`
```bash
vagrant@ubuntu:~$ lsmod | grep 8021q
vagrant@ubuntu:~$ sudo modprobe 8021q
vagrant@ubuntu:~$ lsmod | grep 8021q
8021q                  45056  0
garp                   24576  1 8021q
mrp                    24576  1 8021q
```

```bash
vagrant@ubuntu:~$ sudo apt install vlan
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  vlan
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 11.3 kB of archives.
After this operation, 50.2 kB of additional disk space will be used.
Get:1 http://us.ports.ubuntu.com/ubuntu-ports focal-updates/universe arm64 vlan all 2.0.4ubuntu1.20.04.1 [11.3 kB]
Fetched 11.3 kB in 0s (22.9 kB/s)
Selecting previously unselected package vlan.
(Reading database ... 124292 files and directories currently installed.)
Preparing to unpack .../vlan_2.0.4ubuntu1.20.04.1_all.deb ...
Unpacking vlan (2.0.4ubuntu1.20.04.1) ...
Setting up vlan (2.0.4ubuntu1.20.04.1) ...
Processing triggers for man-db (2.9.1-1) ...
vagrant@ubuntu:~$ sudo vconfig add eth0 400

Warning: vconfig is deprecated and might be removed in the future, please migrate to ip(route2) as soon as possible!

vagrant@ubuntu:~$ sudo ip link set eth0.400 up
vagrant@ubuntu:~$ sudo ip a add 192.168.5.5/255.255.255.0 dev eth0.400
vagrant@ubuntu:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 10.211.55.17/24 brd 10.211.55.255 scope global dynamic eth0
       valid_lft 1683sec preferred_lft 1683sec
    inet6 fdb2:2c26:f4e4:0:21c:42ff:fe10:7bf8/64 scope global dynamic mngtmpaddr noprefixroute
       valid_lft 2591560sec preferred_lft 604360sec
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
3: eth0.400@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.5/24 scope global eth0.400
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
```

```bash
vagrant@ubuntu:~$ sudo ip link add link eth0 name eth0.401 type vlan id 401
vagrant@ubuntu:~$ sudo ip link set eth0.401 up
vagrant@ubuntu:~$ sudo ip a add 192.168.6.5/255.255.255.0 dev eth0.401
vagrant@ubuntu:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 10.211.55.17/24 brd 10.211.55.255 scope global dynamic eth0
       valid_lft 1527sec preferred_lft 1527sec
    inet6 fdb2:2c26:f4e4:0:21c:42ff:fe10:7bf8/64 scope global dynamic mngtmpaddr noprefixroute
       valid_lft 2591976sec preferred_lft 604776sec
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
3: eth0.400@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.5/24 scope global eth0.400
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
4: eth0.401@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.6.5/24 scope global eth0.401
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
```
После перезагрузки виртуальные интерфейсы удалятся. Для постоянной конфигурации придется использовать конфигурационные файлы в зависимости от версии  дистрибутива Linux пример:  `/etc/network/interfaces` - устаревшее.

или
/etc/netplan/01-netcfg.yaml
```bash
vagrant@ubuntu:~$ sudo vim /etc/netplan/01-netcfg.yaml
"/etc/netplan/01-netcfg.yaml" 5L, 63C                                               1,1           All
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
  vlans:
    eth0.500:
      id: 500
      link: eth0
      addresses: [192.168.7.5/24]
~
~
vagrant@vagrant:~$ sudo netplan apply
vagrant@ubuntu:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 10.211.55.17/24 brd 10.211.55.255 scope global dynamic eth0
       valid_lft 1796sec preferred_lft 1796sec
    inet6 fdb2:2c26:f4e4:0:21c:42ff:fe10:7bf8/64 scope global dynamic mngtmpaddr noprefixroute
       valid_lft 2591997sec preferred_lft 604797sec
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
3: eth0.400@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.5.5/24 scope global eth0.400
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
4: eth0.401@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.6.5/24 scope global eth0.401
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
5: eth0.500@eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:1c:42:10:7b:f8 brd ff:ff:ff:ff:ff:ff
    inet 192.168.7.5/24 brd 192.168.7.255 scope global eth0.500
       valid_lft forever preferred_lft forever
    inet6 fe80::21c:42ff:fe10:7bf8/64 scope link
       valid_lft forever preferred_lft forever
```

4) Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.
 
В Linux существуют Team и Bonding. Балансировка нагрузки осуществляется в следующих режимах
```
0 - balance-rr - (round-robin)

1 - active-backup

2 - balance-xor

3 - broadcast

4 - 802.3ad - (dynamic link aggregation)

5 - balance-tlb - (adaptive transmit load balancing)

6 - balance-alb - (adaptive load balancing)
```
Конфиг

```bash
vagrant@vagrant:~$ sudo cat /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
    eth1:
      dhcp4: no
    eth2:
      dhcp4: no
  bonds:
   bond0:
    addresses: [192.168.7.5/24]
    interfaces: [eth1, eth2]
    parameters:
      mode: balance-rr
vagrant@vagrant:~$ sudo netplan apply
vagrant@vagrant:~$ ip a show bond0
5: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 16:77:21:70:b2:49 brd ff:ff:ff:ff:ff:ff
    inet 192.168.7.5/24 brd 192.168.70.255 scope global bond0
       valid_lft forever preferred_lft forever
    inet6 fe80::820:6cff:fe5c:1443/64 scope link
       valid_lft forever preferred_lft forever
```
5) Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.

В сети с маской `/29` - `8` IP адресов. Из них доступны для устройств - `6`. Один адрес используется для сети и еще один для широковещательного запроса.

Из сети `/24` можно получить `32` подсети `/29`. Например,
```
10.10.10.0/29
10.10.10.8/29
10.10.10.16/29
10.10.10.24/29
10.10.10.32/29
10.10.10.40/29
10.10.10.48/29
10.10.10.56/29
10.10.10.64/29
10.10.10.72/29
10.10.10.80/29
10.10.10.88/29
10.10.10.96/29
```
6) Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.

`100.64.0.0/26`

7) Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?

Ubuntu \
`ip neighbour show` - показать ARP таблицу \
`arp -a` - показать ARP таблицу \
`ip neighbour del [ip address] dev [interface]` - удалить из ARP таблицы конкретный адрес \
`arp -d <host> ` - удалить из ARP таблицы конкретный адрес \
`ip neighbour flush all` - очищает таблицу ARP
`arp -d -a` -  очищает таблицу ARP

Windows \
`arp -a` - показать ARP таблицу \
`arp -d *` - очистить таблицу ARP \
`arp -d [ip address]` - удалить из ARP таблицы конкретный адрес \

