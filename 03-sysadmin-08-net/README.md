# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

1) Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP
```bash
route-views>show ip route 89.22.237.169
Routing entry for 89.22.237.0/24
  Known via "bgp 6447", distance 20, metric 0
  Tag 8283, type external
  Last update from 94.142.247.3 5d03h ago
  Routing Descriptor Blocks:
  * 94.142.247.3, from 94.142.247.3, 5d03h ago
      Route metric is 0, traffic share count is 1
      AS Hops 3
      Route tag 8283
      MPLS label: none
route-views>show bgp 89.22.237.169
BGP routing table entry for 89.22.237.0/24, version 2712911480
Paths: (19 available, best #12, table default)
  Not advertised to any peer
  Refresh Epoch 1
  3257 28917 207651 207651
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin IGP, metric 10, localpref 100, valid, external
      Community: 3257:4000 3257:8092 3257:50001 3257:50111 3257:54800 3257:54801
      path 7FE0FCDACB90 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  2497 174 52000 207651
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin IGP, localpref 100, valid, external
      path 7FE028116FD0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 209 3356 9002 207651
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE07E0EDD08 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 3356 9002 207651
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin IGP, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE13848C140 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 9002 207651
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE01D903968 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 9002 207651
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:3 3356:22 3356:100 3356:123 3356:575 3356:903 3356:2056
      path 7FE0DCE58228 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  57866 28917 207651 207651
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 0:6939 0:16276 0:31500 0:49981 28917:2000 57866:200 65102:41441 65103:1 65104:31
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x30
        value 0000 E20A 0000 0065 0000 00C8 0000 E20A
              0000 0066 0000 A1E1 0000 E20A 0000 0067
              0000 0001 0000 E20A 0000 0068 0000 001F

      path 7FE0DE372228 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  852 33891 50673 52000 207651
    154.11.12.212 from 154.11.12.212 (96.1.209.43)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE02BE9F728 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3267 31500 207651 207651
    194.85.40.15 from 194.85.40.15 (185.141.126.1)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE12150FE98 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 9002 207651
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external
      path 7FE13D3BB050 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 9002 207651
    64.71.137.241 from 64.71.137.241 (216.218.253.53)
      Origin IGP, localpref 100, valid, external
      path 7FE132B550E8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  8283 207651 207651
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin IGP, metric 0, localpref 100, valid, external, best
      Community: 8283:1 8283:101
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x24
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 0000 205B 0000 0008
              0000 0732
      path 7FE0FFE6D9B0 RPKI State not found
      rx pathid: 0, tx pathid: 0x0
  Refresh Epoch 1
  20912 3257 28917 207651 207651
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin IGP, localpref 100, valid, external
      Community: 3257:4000 3257:8092 3257:50001 3257:50111 3257:54800 3257:54801 20912:65004
      path 7FE1163B58B0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 12552 9002 207651
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin IGP, localpref 100, valid, external
      Community: 12552:10000 12552:14000 12552:14100 12552:14101 12552:24000
      Extended Community: 0x43:100:1
      path 7FE104783948 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3549 3356 9002 207651
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:3 3356:22 3356:100 3356:123 3356:575 3356:903 3356:2056 3549:2581 3549:30840
      path 7FE12FFF67E8 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 9002 207651
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin IGP, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE0C2BF0188 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  101 3356 9002 207651
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20100 101:20110 101:22100 3356:3 3356:22 3356:100 3356:123 3356:575 3356:903 3356:2056
      Extended Community: RT:101:22100
      path 7FE165D83AD0 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3303 9002 207651
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1004 3303:1006 3303:1030 3303:3077 9002:64657
      path 7FE0DD59FC88 RPKI State not found
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 9002 207651
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE0C1316500 RPKI State not found
      rx pathid: 0, tx pathid: 0
route-views>
```

2) Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

```bash
vagrant@ubuntu:~$ sudo modprobe dummy
vagrant@ubuntu:~$ sudo ip link add eth_dummy type dummy
vagrant@ubuntu:~$ ip a sh type dummy
4: eth_dummy: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 3a:fa:12:83:ea:1c brd ff:ff:ff:ff:ff:ff
vagrant@ubuntu:~$ sudo ip addr add 172.16.1.1/24 dev eth_dummy
vagrant@ubuntu:~$ sudo ip link set eth_dummy up
vagrant@ubuntu:~$ ip a sh type dummy
4: eth_dummy: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether 3a:fa:12:83:ea:1c brd ff:ff:ff:ff:ff:ff
    inet 172.16.1.1/24 scope global eth_dummy
       valid_lft forever preferred_lft forever
    inet6 fe80::38fa:12ff:fe83:ea1c/64 scope link
       valid_lft forever preferred_lft forever
vagrant@ubuntu:~$ sudo ip route add 172.16.10.0/24 via 10.211.55.1
vagrant@ubuntu:~$ sudo ip route add 172.16.50.0/24 dev eth0
vagrant@ubuntu:~$ sudo ip route add 172.16.20.0/24 via 10.211.55.1
vagrant@ubuntu:~$ ip -br route
default via 10.211.55.1 dev eth0 proto dhcp src 10.211.55.17 metric 100
10.211.55.0/24 dev eth0 proto kernel scope link src 10.211.55.17
10.211.55.1 dev eth0 proto dhcp scope link src 10.211.55.17 metric 100
172.16.1.0/24 dev eth_dummy proto kernel scope link src 172.16.1.1
172.16.10.0/24 via 10.211.55.1 dev eth0
172.16.20.0/24 via 10.211.55.1 dev eth0
172.16.50.0/24 dev eth0 scope link
```
3) Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.
```bash
vagrant@ubuntu:~$ sudo ss -ltpn
State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port    Process
LISTEN     0          4096               127.0.0.1:8125               0.0.0.0:*        users:(("netdata",pid=735,fd=52))
LISTEN     0          4096                 0.0.0.0:19999              0.0.0.0:*        users:(("netdata",pid=735,fd=4))
LISTEN     0          4096           127.0.0.53%lo:53                 0.0.0.0:*        users:(("systemd-resolve",pid=712,fd=13))
LISTEN     0          128                  0.0.0.0:22                 0.0.0.0:*        users:(("sshd",pid=804,fd=3))
LISTEN     0          4096                       *:9100                     *:*        users:(("node_exporter",pid=737,fd=3))
LISTEN     0          128                     [::]:22                    [::]:*        users:(("sshd",pid=804,fd=4))
```
`53` - DNS \
`22` - SSH

4) Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

```bash
vagrant@ubuntu:~$ sudo ss -lupn
State     Recv-Q    Send-Q            Local Address:Port         Peer Address:Port    Process
UNCONN    0         0                     127.0.0.1:8125              0.0.0.0:*        users:(("netdata",pid=735,fd=35))
UNCONN    0         0                 127.0.0.53%lo:53                0.0.0.0:*        users:(("systemd-resolve",pid=712,fd=12))
UNCONN    0         0             10.211.55.17%eth0:68                0.0.0.0:*        users:(("systemd-network",pid=706,fd=15))
```

5) Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

https://drive.google.com/file/d/1d2zeQGoLmGKHdyY2XXnbkEN3vGhI5ps7/view?usp=sharing
