# Shocker Hackthebox Writeup

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 08:15:00 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.56
Warning: 10.10.10.56 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.56
Host is up, received timestamp-reply ttl 63 (0.15s latency).
Scanned at 2021-07-02 08:15:00 -06 for 903s
Not shown: 65522 closed ports
Reason: 65522 conn-refused
PORT      STATE    SERVICE      REASON
80/tcp    open     http         syn-ack
2222/tcp  open     EtherNetIP-1 syn-ack
Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Jul  2 08:30:03 2021 -- 1 IP address (1 host up) scanned in 903.45 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 08:30:26 2021 as: nmap -T4 -sT -sV -sC -A -vv -p80,2222 -oA nmap/complete 10.10.10.56
Nmap scan report for 10.10.10.56
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-07-02 08:30:27 -06 for 17s

PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
2222/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD8ArTOHWzqhwcyAZWc2CmxfLmVVTwfLZf0zhCBREGCpS2WC3NhAKQ2zefCHCU8XTC8hY9ta5ocU+p7S52OGHlaG7HuA5Xlnihl1INNsMX7gpNcfQEYnyby+hjHWPLo4++fAyO/lB8NammyA13MzvJy8pxvB9gmCJhVPaFzG5yX6Ly8OIsvVDk+qVa5eLCIua1E7WGACUlmkEGljDvzOaBdogMQZ8TGBTqNZbShnFH1WsUxBtJNRtYfeeGjztKTQqqj4WD5atU8dqV/iwmTylpE7wdHZ+38ckuYL9dmUPLh4Li2ZgdY6XniVOBGthY5a2uJ2OFp2xe1WS9KvbYjJ/tH
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiFJd2F35NPKIQxKMHrgPzVzoNHOJtTtM+zlwVfxzvcXPFFuQrOL7X6Mi9YQF9QRVJpwtmV9KAtWltmk3qm4oc=
|   256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC/RjKhT/2YPlCgFQLx+gOXhC6W3A3raTzjlXQMT8Msk
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.12 (95%), Linux 3.13 (95%), Linux 3.16 (95%), Linux 3.2 - 4.9 (95%), Linux 3.8 - 3.11 (95%), Linux 4.8 (95%), Linux 4.4 (95%), Linux 4.9 (95%), Linux 3.18 (95%), Linux 4.2 (95%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/2%OT=80%CT=%CU=38529%PV=Y%DS=2%DC=T%G=N%TM=60DF2314%P=x86_64-pc-linux-gnu)
SEQ(SP=106%GCD=1%ISR=108%TI=Z%CI=I%II=I%TS=8)
OPS(O1=M54DST11NW6%O2=M54DST11NW6%O3=M54DNNT11NW6%O4=M54DST11NW6%O5=M54DST11NW6%O6=M54DST11)
WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)
ECN(R=Y%DF=Y%T=40%W=7210%O=M54DNNSNW6%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.008 days (since Fri Jul  2 08:19:28 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   147.98 ms 10.10.14.1
2   148.04 ms 10.10.10.56

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul  2 08:30:44 2021 -- 1 IP address (1 host up) scanned in 18.07 seconds
```
 
## Port 80 Enumeration

![](Images/Pasted%20image%2020210702194630.png)

![](Images/Pasted%20image%2020210702203637.png)


Becuase we have a access of cgi-bin content so i firts tried for Shelshock.

While searching for executables in cgi-bin.

My dirsearch is not working for the extensions so i used gobuster.

```java
┌─[R4hn1]─[10.10.14.137]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Shocker]
└────╼ # gobuster dir -u http://10.10.10.56/cgi-bin/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -x .php,.sh,.pl,.rb,.py
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.56/cgi-bin/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php,sh,pl,rb,py
[+] Timeout:                 10s
===============================================================
2021/07/02 09:53:28 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess.sh         (Status: 403) [Size: 306]
/user.sh              (Status: 200) [Size: 118]
                                               
===============================================================
2021/07/02 10:00:35 Finished
===============================================================
```

While looking for user.sh its a simple contentent nothing more

![](Images/Pasted%20image%2020210702213210.png)

![](Images/Pasted%20image%2020210702204436.png)

And now we got a shell.

![](Images/Pasted%20image%2020210702204834.png)

And its rooted.

![](Images/Pasted%20image%2020210702204819.png)