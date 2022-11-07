# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"

1. `vagrant@vagrant:~$ cat /etc/systemd/system/node_exporter.service`
```bash
[Unit]
Description=Node Exporter

[Service]
User=node_exporter
EnvironmentFile=/etc/sysconfig/node_exporter
ExecStart=/usr/sbin/node_exporter $OPTIONS

[Install]
WantedBy=multi-user.target

vagrant@vagrant:~$ sudo ss -pnltu | grep 9100
tcp    LISTEN  0       4096                       *:9100                *:*      users:(("node_exporter",pid=720,fd=3))

vagrant@vagrant:~$ sudo systemctl status node_exporter
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-11-07 20:13:29 UTC; 17s ago
   Main PID: 720 (node_exporter)
      Tasks: 4 (limit: 1060)
     Memory: 13.2M
     CGroup: /system.slice/node_exporter.service
             └─720 /usr/sbin/node_exporter --collector.textfile.directory /var/lib/node_exporter/textfile_collector

Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=thermal_zone
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=time
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=timex
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=udp_queues
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=uname
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=vmstat
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=xfs
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:115 level=info collector=zfs
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=node_exporter.go:199 level=info msg="Listening on" address=:9100
Nov 07 20:13:29 vagrant node_exporter[720]: ts=2022-11-07T20:13:29.515Z caller=tls_config.go:195 level=info msg="TLS is disabled." http2=false
```