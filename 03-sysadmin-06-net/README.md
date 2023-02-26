# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

1) Работа c HTTP через телнет
```bash
vagrant@ubuntu:~$ telnet stackoverflow.com 80
Trying 151.101.193.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 403 Forbidden
Connection: close
Content-Length: 1920
Server: Varnish
Retry-After: 0
Content-Type: text/html
Accept-Ranges: bytes
Date: Sun, 26 Feb 2023 16:05:57 GMT
Via: 1.1 varnish
X-Served-By: cache-bma1647-BMA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1677427558.557143,VS0,VE1
X-DNS-Prefetch-Control: off

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Forbidden - Stack Exchange</title>
    <style type="text/css">
		body
		{
			color: #333;
			font-family: 'Helvetica Neue', Arial, sans-serif;
			font-size: 14px;
			background: #fff url('img/bg-noise.png') repeat left top;
			line-height: 1.4;
		}
		h1
		{
			font-size: 170%;
			line-height: 34px;
			font-weight: normal;
		}
		a { color: #366fb3; }
		a:visited { color: #12457c; }
		.wrapper {
			width:960px;
			margin: 100px auto;
			text-align:left;
		}
		.msg {
			float: left;
			width: 700px;
			padding-top: 18px;
			margin-left: 18px;
		}
    </style>
</head>
<body>
    <div class="wrapper">
		<div style="float: left;">
			<img src="https://cdn.sstatic.net/stackexchange/img/apple-touch-icon.png" alt="Stack Exchange" />
		</div>
		<div class="msg">
			<h1>Access Denied</h1>
                        <p>This IP address (37.144.35.152) has been blocked from access to our services. If you believe this to be in error, please contact us at <a href="mailto:team@stackexchange.com?Subject=Blocked%2037.144.35.152%20(Request%20ID%3A%203302231147-BMA)">team@stackexchange.com</a>.</p>
                        <p>When contacting us, please include the following information in the email:</p>
                        <p>Method: block</p>
                        <p>XID: 3302231147-BMA</p>
                        <p>IP: 37.144.35.152</p>
                        <p>X-Forwarded-For: </p>
                        <p>User-Agent: </p>

                        <p>Time: Sun, 26 Feb 2023 16:05:57 GMT</p>
                        <p>URL: stackoverflow.com/questions</p>
                        <p>Browser Location: <span id="jslocation">(not loaded)</span></p>
		</div>
	</div>
	<script>document.getElementById('jslocation').innerHTML = window.location.href;</script>
</body>vagrant@ubuntu:~$ telnet stackoverflow.com 80
Trying 151.101.129.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 403 Forbidden
Connection: close
Content-Length: 1920
Server: Varnish
Retry-After: 0
Content-Type: text/html
Accept-Ranges: bytes
Date: Sun, 26 Feb 2023 16:31:08 GMT
Via: 1.1 varnish
X-Served-By: cache-bma1625-BMA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1677429068.070995,VS0,VE1
X-DNS-Prefetch-Control: off

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Forbidden - Stack Exchange</title>
    <style type="text/css">
		body
		{
			color: #333;
			font-family: 'Helvetica Neue', Arial, sans-serif;
			font-size: 14px;
			background: #fff url('img/bg-noise.png') repeat left top;
			line-height: 1.4;
		}
		h1
		{
			font-size: 170%;
			line-height: 34px;
			font-weight: normal;
		}
		a { color: #366fb3; }
		a:visited { color: #12457c; }
		.wrapper {
			width:960px;
			margin: 100px auto;
			text-align:left;
		}
		.msg {
			float: left;
			width: 700px;
			padding-top: 18px;
			margin-left: 18px;
		}
    </style>
</head>
<body>
    <div class="wrapper">
		<div style="float: left;">
			<img src="https://cdn.sstatic.net/stackexchange/img/apple-touch-icon.png" alt="Stack Exchange" />
		</div>
		<div class="msg">
			<h1>Access Denied</h1>
                        <p>This IP address (37.144.35.152) has been blocked from access to our services. If you believe this to be in error, please contact us at <a href="mailto:team@stackexchange.com?Subject=Blocked%2037.144.35.152%20(Request%20ID%3A%202557505001-BMA)">team@stackexchange.com</a>.</p>
                        <p>When contacting us, please include the following information in the email:</p>
                        <p>Method: block</p>
                        <p>XID: 2557505001-BMA</p>
                        <p>IP: 37.144.35.152</p>
                        <p>X-Forwarded-For: </p>
                        <p>User-Agent: </p>

                        <p>Time: Sun, 26 Feb 2023 16:31:08 GMT</p>
                        <p>URL: stackoverflow.com/questions</p>
                        <p>Browser Location: <span id="jslocation">(not loaded)</span></p>
		</div>
	</div>
	<script>document.getElementById('jslocation').innerHTML = window.location.href;</script>
</body>
</html>Connection closed by foreign host.
```
HTTP 403 Forbidden — стандартный код ответа HTTP, означающий, что доступ к запрошенному ресурсу запрещен. Сервер понял запрос, но не выполнит его.
2) Повторите задание 1 в браузере, используя консоль разработчика F12

HTTP 301 или Moved Permanently (с англ. — «Перемещено навсегда») — стандартный код ответа HTTP, получаемый в ответ от сервера в ситуации, когда запрошенный ресурс был на постоянной основе перемещён в новое месторасположение
- перемещен на https://stackoverflow.com/
```
Request URL: http://stackoverflow.com/
Request Method: GET
Status Code: 301 Moved Permanently
Remote Address: 151.101.1.69:80
Referrer Policy: strict-origin-when-cross-origin
Accept-Ranges: bytes
cache-control: no-cache, no-store, must-revalidate
Connection: keep-alive
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Date: Sun, 26 Feb 2023 16:37:28 GMT
feature-policy: microphone 'none'; speaker 'none'
location: https://stackoverflow.com/
Set-Cookie: prov=113af45d-ed54-fb3e-a06c-a6123fb6a7a1; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly
set-cookie: prov_tgt=; expires=Fri, 24 Feb 2023 16:37:28 GMT; domain=.stackoverflow.com; path=/; secure; samesite=none; httponly
transfer-encoding: chunked
Vary: Fastly-SSL
Via: 1.1 varnish
X-Cache: MISS
X-Cache-Hits: 0
X-DNS-Prefetch-Control: off
x-request-guid: 910263ef-4ac3-47cf-9f8c-1ea9d22f5c25
X-Served-By: cache-bma1620-BMA
X-Timer: S1677429448.311549,VS0,VE104
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en;q=0.9
Connection: keep-alive
DNT: 1
Host: stackoverflow.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36
```

Страница http://stackoverflow.com/ была загружена за 165.77 ms
Страница https://stackoverflow.com/ была загружена за 594.15 ms

![Screenshot 2023-02-26 at 19.51.16.png](..%2F..%2F..%2F..%2F..%2FDesktop%2FScreenshot%202023-02-26%20at%2019.51.16.png)

3) Какой IP адрес у вас в интернете?

37.144.35.152

4) Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS?

BEELINE
```bash
 ~  whois -h whois.radb.net 37.144.35.152
route:          37.144.35.0/24
descr:          RU-BEELINE-BROADBAND-GLOBAL
origin:         AS8402
mnt-by:         RU-CORBINA-MNT
notify:         noc@corbina.net
created:        2012-03-27T11:27:51Z
last-modified:  2012-03-27T11:27:51Z
source:         RIPE
remarks:        ****************************
remarks:        * THIS OBJECT IS MODIFIED
remarks:        * Please note that all data that is generally regarded as personal
remarks:        * data has been removed from this object.
remarks:        * To view the original object, please query the RIPE Database at:
remarks:        * http://www.ripe.net/whois
remarks:        ****************************
```

5) Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute

```bash
✘  ~  traceroute -An 8.8.8.8

traceroute to 8.8.8.8 (8.8.8.8), 64 hops max, 52 byte packets
 1  192.168.1.1 (192.168.1.1)  4.929 ms  2.396 ms  1.993 ms
 2  * * *
 3  * * *
 4  85.21.224.191 (85.21.224.191)  8.379 ms  4.459 ms  4.673 ms
 5  108.170.250.83 (108.170.250.83)  5.578 ms
    108.170.250.113 (108.170.250.113)  5.320 ms  5.282 ms
 6  172.253.66.116 (172.253.66.116)  22.820 ms
    142.251.49.158 (142.251.49.158)  17.939 ms
    142.250.238.214 (142.250.238.214)  23.499 ms
 7  142.250.235.74 (142.250.235.74)  20.018 ms
    142.250.233.0 (142.250.233.0)  22.904 ms
    74.125.253.109 (74.125.253.109)  48.013 ms
 8  216.239.62.15 (216.239.62.15)  20.106 ms
    142.250.236.77 (142.250.236.77)  21.914 ms
    142.250.56.221 (142.250.56.221)  22.488 ms
 9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  dns.google (8.8.8.8)  24.273 ms *  21.405 ms
```
6) Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?

```bash
My traceroute  [v0.95]
MacBook778.local (192.168.1.104) -> 8.8.8.8 (8.8.8.8)                        2023-02-26T20:31:41+0300
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                             Packets               Pings
 Host                                                      Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. AS???    192.168.1.1                                    0.0%    43    2.2   2.5   1.8   9.4   1.1
 2. AS???    100.117.0.1                                   50.0%    43    4.8   4.4   4.0   4.9   0.3
 3. (waiting for reply)
 4. AS8402   85.21.224.191                                  0.0%    43    5.5   8.8   4.2 144.7  21.3
 5. AS15169  108.170.250.130                                0.0%    43    5.9   5.7   5.0   7.4   0.5
 6. AS15169  142.250.238.214                                0.0%    43   23.0  23.0  22.4  24.3   0.4
 7. AS15169  142.250.233.0                                  0.0%    43   37.5  25.5  21.8  59.1   8.1
 8. AS15169  216.239.47.167                                 0.0%    42   23.6  23.9  23.2  26.8   0.6
 9. (waiting for reply)
10. (waiting for reply)
11. (waiting for reply)
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. AS15169  dns.google                                     0.0%    42   20.1  20.2  19.7  21.1   0.4

```
Наибольшая задержка на `AS8402   85.21.224.191 ` Wrst - 144.7

7) Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig

```bash
~  dig +short NS dns.google
ns3.zdns.google.
ns2.zdns.google.
ns4.zdns.google.
ns1.zdns.google.
```
8) Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig

```bash
 ~  dig +noall +answer -x 8.8.8.8
8.8.8.8.in-addr.arpa.	48343	IN	PTR	dns.google.
 ~  dig +noall +answer -x 8.8.4.4
4.4.8.8.in-addr.arpa.	85889	IN	PTR	dns.google.
```
