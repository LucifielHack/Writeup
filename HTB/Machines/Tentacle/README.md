# Tentacle Hackthebox Walkthrough

## ALL Ports Scan
```bash
# Nmap 7.91 scan initiated Thu Jun 10 20:20:54 2021 as: nmap -sT -vv -p- -oA nmap/allports 10.10.10.224
Nmap scan report for 10.10.10.224
Host is up, received admin-prohibited ttl 63 (0.68s latency).
Scanned at 2021-06-10 20:20:54 EDT for 1745s
Not shown: 65530 filtered ports
Reason: 63770 no-responses and 1760 host-unreaches
PORT     STATE  SERVICE      REASON
22/tcp   open   ssh          syn-ack
53/tcp   open   domain       syn-ack
88/tcp   open   kerberos-sec syn-ack
3128/tcp open   squid-http   syn-ack
9090/tcp closed zeus-admin   conn-refused

Read data files from: /usr/bin/../share/nmap
# Nmap done at Thu Jun 10 20:49:59 2021 -- 1 IP address (1 host up) scanned in 1745.87 seconds
```

## Complete Scan
```bash
# Nmap 7.91 scan initiated Thu Jun 10 20:53:00 2021 as: nmap -vv -sT -sC -sV -A -p22,53,88,3128,9090 -oA nmap/complete 10.10.10.224
Nmap scan report for 10.10.10.224
Host is up, received echo-reply ttl 63 (0.29s latency).
Scanned at 2021-06-10 20:53:01 EDT for 36s

PORT     STATE  SERVICE      REASON       VERSION
22/tcp   open   ssh          syn-ack      OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 8d:dd:18:10:e5:7b:b0:da:a3:fa:14:37:a7:52:7a:9c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC+kAz7g80bfMUdNCm4e54eIGFeFFwEIUvieBfBq/B4pm1NCa2XPPCs0hHL1S7myYvcxmlM3TW2oE0p4Y5lScvISBljVQSXvIWxPreotbiBYSJ8hnmXKpc1KAjiyA9fAEPYCypL4/yHyMDl4m0GIElshzKZClxQBF9Qgt9eI+hAmB1b4iz6h3zOcFNzgtsqki1KqbkHhrlFxRko0P4boCa5qzQDeHXSyG/7Eg6b4i5JEJhowqjRjmHs5pvbHJBJagqHgUesFuwgvp0/pxwvK1FD1GvfhGlNwMnr8TWA5VNXQ+ZIaOFfftKPjfBBwwUxgIRbCLJSEt0YTIc2mr0HRQi+yHFxBkC6OLPqzpXP57lXyRXEWXefvqkRrVtz7EgqfyV5aZVGobE8tgmypiYYvFMfXYH14jXFYoVts6+R0qeGJ0PA3FygWQpDDthIA1ok/6dlb2xPz6ktSOvCp/f5LLHGLSMfpjTwadeTpu2g3DWpCozUTol/wFWLH2y/wqUTiak=
|   256 f6:a9:2e:57:f8:18:b6:f4:ee:03:41:27:1e:1f:93:99 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDEUXStQR+Skq5wAn4zjO2SSm45o1cMxUeh+gFslfEaKWNGF+hTyXzv/AeTZ2ggp3dySOGudrTD4FzvW9/mTnxM=
|   256 04:74:dd:68:79:f4:22:78:d8:ce:dd:8b:3e:8c:76:3b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGaEuqAyutfTuj3KR9B6qEaIZAc2oszJPVDC1JEGv36y
53/tcp   open   domain       syn-ack      ISC BIND 9.11.20 (RedHat Enterprise Linux 8)
| dns-nsid: 
|_  bind.version: 9.11.20-RedHat-9.11.20-5.el8
88/tcp   open   kerberos-sec syn-ack      MIT Kerberos (server time: 2021-06-10 15:26:50Z)
3128/tcp open   http-proxy   syn-ack      Squid http proxy 4.11
|_http-server-header: squid/4.11
|_http-title: ERROR: The requested URL could not be retrieved
9090/tcp closed zeus-admin   conn-refused
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
Aggressive OS guesses: Linux 5.1 (94%), Linux 3.10 - 4.11 (92%), HP P2000 G3 NAS device (91%), Linux 3.2 - 4.9 (91%), Linux 3.16 - 4.6 (90%), Linux 2.6.32 (90%), Infomir MAG-250 set-top box (90%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (90%), Linux 3.7 (90%), Linux 5.0 (90%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/10%OT=22%CT=9090%CU=%PV=Y%DS=2%DC=T%G=N%TM=60C2B411%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=2%ISR=10C%TI=Z%CI=Z%II=I%TS=A)
SEQ(SP=105%GCD=1%ISR=10C%TI=Z%CI=Z%TS=A)
OPS(O1=M54DST11NW7%O2=M54DST11NW7%O3=M54DNNT11NW7%O4=M54DST11NW7%O5=M54DST11NW7%O6=M54DST11)
WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)
ECN(R=Y%DF=Y%TG=40%W=7210%O=M54DNNSNW7%CC=Y%Q=)
T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=40%CD=S)

Uptime guess: 22.390 days (since Wed May 19 11:31:59 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: REALCORP.HTB; OS: Linux; CPE: cpe:/o:redhat:enterprise_linux:8

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   277.08 ms 10.10.14.1
2   277.23 ms 10.10.10.224

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 10 20:53:37 2021 -- 1 IP address (1 host up) scanned in 37.60 seconds
```

## Enumerating Port 3128
Hitting port to browser got a domain connected to server.

```bash
Domian : realcorp.htb
Subdomain  : srv01.realcorp.htb

Email : j.nakazawa@realcorp.htb
Username : j.nakazawa
```
![](Images/Pasted%20image%2020210610205937.png)

When calling the domain with port got one active

![](Images/Pasted%20image%2020210610210515.png)

![](Images/Pasted%20image%2020210610210800.png)

```bash
http://realcorp.htb:88/
���\`~^0\\ ˇ¤20210610154105ZĄ…6¦=©REALCORP.HTBŞ!0 �ˇ0krbtgtREALCORP.HTB

http://srv01.realcorp.htb:88/
���\`~^0\\ Ą¤20210610153908ZĽĎ+Ś=ŠREALCORP.HTBŞ!0 �Ą0krbtgtREALCORP.HTB
```

Nothing More.
So the server has 53 DNS port open so i look forward for another subdomains.

```java
Subdomain Search : 
# dnsenum --enum --dnsserver 10.10.10.224 -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 160 realcorp.htb
```
![](Images/Pasted%20image%2020210610220525.png)

Find 2 more connected domains.

```java
# dnsenum --noreverse no-ip.htb --dnsserver 10.129.158.196
```

![[Pasted image 20210614140717.png]]