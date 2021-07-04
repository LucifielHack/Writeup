# Agent Sudo TryHackMe Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 28 14:57:10 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.92.85
Warning: 10.10.92.85 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.92.85
Host is up, received echo-reply ttl 63 (0.19s latency).
Scanned at 2021-06-28 14:57:10 EDT for 702s
Not shown: 65492 closed ports
Reason: 65492 conn-refused
PORT      STATE    SERVICE REASON
21/tcp    open     ftp     syn-ack
22/tcp    open     ssh     syn-ack
80/tcp    open     http    syn-ack
Read data files from: /usr/bin/../share/nmap
# Nmap done at Mon Jun 28 15:08:52 2021 -- 1 IP address (1 host up) scanned in 701.57 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 28 14:58:15 2021 as: nmap -T4 -sT -sV -sC -A -vv -p21,22,80 -oA nmap/complete 10.10.92.85
WARNING: RST from 10.10.92.85 port 21 -- is this port really open?
Nmap scan report for 10.10.92.85
Host is up, received echo-reply ttl 63 (0.18s latency).
Scanned at 2021-06-28 14:58:15 EDT for 21s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ef:1f:5d:04:d4:77:95:06:60:72:ec:f0:58:f2:cc:07 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5hdrxDB30IcSGobuBxhwKJ8g+DJcUO5xzoaZP/vJBtWoSf4nWDqaqlJdEF0Vu7Sw7i0R3aHRKGc5mKmjRuhSEtuKKjKdZqzL3xNTI2cItmyKsMgZz+lbMnc3DouIHqlh748nQknD/28+RXREsNtQZtd0VmBZcY1TD0U4XJXPiwleilnsbwWA7pg26cAv9B7CcaqvMgldjSTdkT1QNgrx51g4IFxtMIFGeJDh2oJkfPcX6KDcYo6c9W1l+SCSivAQsJ1dXgA2bLFkG/wPaJaBgCzb8IOZOfxQjnIqBdUNFQPlwshX/nq26BMhNGKMENXJUpvUTshoJ/rFGgZ9Nj31r
|   256 5e:02:d1:9a:c4:e7:43:06:62:c1:9e:25:84:8a:e7:ea (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHdSVnnzMMv6VBLmga/Wpb94C9M2nOXyu36FCwzHtLB4S4lGXa2LzB5jqnAQa0ihI6IDtQUimgvooZCLNl6ob68=
|   256 2d:00:5c:b9:fd:a8:c8:d8:80:e3:92:4f:8b:4f:18:e2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOL3wRjJ5kmGs/hI4aXEwEndh81Pm/fvo8EvcpDHR5nt
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Annoucement
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Linux 3.10 (92%), Linux 3.12 (92%), Linux 3.19 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/28%OT=21%CT=%CU=38760%PV=Y%DS=2%DC=T%G=N%TM=60DA1BDC%P=x86_64-pc-linux-gnu)
SEQ(SP=107%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=A)
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

Uptime guess: 40.686 days (since Tue May 18 22:30:55 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=263 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   148.65 ms 10.8.0.1
2   211.26 ms 10.10.92.85

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 28 14:58:36 2021 -- 1 IP address (1 host up) scanned in 21.37 seconds
```

## Enumeration Port 80

![](Images/Pasted%20image%2020210628152243.png)

```java
┌─[R4hn1]─[10.8.199.231]─[root@V0ld3rm0rt]─[~/Walkthrough/TryHackMe/AgentSudo]
└────╼ # wfuzz -u http://10.10.92.85/ -w alpha.txt -H "User-Agent: FUZZ"
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.92.85/
Total requests: 26

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                   
=====================================================================

000000001:   200        18 L     28 W       218 Ch      "A"                                                                                                       
000000003:   302        18 L     28 W       218 Ch      "C"                                                                                                       
000000007:   200        18 L     28 W       218 Ch      "G"                                                                                                       
000000006:   200        18 L     28 W       218 Ch      "F"                                                                                                       
000000009:   200        18 L     28 W       218 Ch      "I"                                                                                                       
000000008:   200        18 L     28 W       218 Ch      "H"                                                                                                       
000000005:   200        18 L     28 W       218 Ch      "E"                                                                                                       
000000002:   200        18 L     28 W       218 Ch      "B"                                                                                                       
000000004:   200        18 L     28 W       218 Ch      "D"                                                                                                       
000000010:   200        18 L     28 W       218 Ch      "J"                                                                                                       
000000012:   200        18 L     28 W       218 Ch      "L"                                                                                                       
000000016:   200        18 L     28 W       218 Ch      "P"                                                                                                       
000000022:   200        18 L     28 W       218 Ch      "V"                                                                                                       
000000021:   200        18 L     28 W       218 Ch      "U"                                                                                                       
000000020:   200        18 L     28 W       218 Ch      "T"                                                                                                       
000000019:   200        18 L     28 W       218 Ch      "S"                                                                                                       
000000018:   200        18 L     47 W       310 Ch      "R"                                                                                                       
000000015:   200        18 L     28 W       218 Ch      "O"                                                                                                       
000000017:   200        18 L     28 W       218 Ch      "Q"                                                                                                       
000000014:   200        18 L     28 W       218 Ch      "N"                                                                                                       
000000011:   200        18 L     28 W       218 Ch      "K"                                                                                                       
000000013:   200        18 L     28 W       218 Ch      "M"                                                                                                       
000000023:   200        18 L     28 W       218 Ch      "W"                                                                                                       
000000025:   200        18 L     28 W       218 Ch      "Y"                                                                                                       
000000024:   200        18 L     28 W       218 Ch      "X"                                                                                                       
000000026:   200        18 L     28 W       218 Ch      "Z"
```

```java
┌─[R4hn1]─[10.8.199.231]─[root@V0ld3rm0rt]─[~/Walkthrough/TryHackMe/AgentSudo]
└────╼ # curl -A "C" -L 10.10.92.85
Attention chris, <br><br>

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>

From,<br>
Agent R 
```

```bash
Credentials : 
chris:crystal
james:hackerrules!
User : R
User : J
```

## FTP Enumeration

![](Images/Pasted%20image%2020210628153432.png)

![](Images/Pasted%20image%2020210628161529.png)

![](Images/Pasted%20image%2020210628161601.png)

![](Images/Pasted%20image%2020210628161655.png)

![](Images/Pasted%20image%2020210628161856.png)

![](Images/Pasted%20image%2020210628161921.png)