# Atom Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 16 18:21:01 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.237
Nmap scan report for 10.10.10.237
Host is up, received echo-reply ttl 127 (0.18s latency).
Scanned at 2021-06-16 18:21:01 EDT for 217s
Not shown: 65529 filtered ports
Reason: 65529 no-responses
PORT     STATE SERVICE      REASON
80/tcp   open  http         syn-ack
135/tcp  open  msrpc        syn-ack
443/tcp  open  https        syn-ack
445/tcp  open  microsoft-ds syn-ack
5985/tcp open  wsman        syn-ack
6379/tcp open  redis        syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Wed Jun 16 18:24:38 2021 -- 1 IP address (1 host up) scanned in 216.78 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Wed Jun 16 18:25:41 2021 as: nmap -T4 -sT -sV -sC -A -vv -p80,135,443,445,5985,6379 -oA nmap/complete 10.10.10.237
Nmap scan report for 10.10.10.237
Host is up, received echo-reply ttl 127 (0.35s latency).
Scanned at 2021-06-16 18:25:42 EDT for 67s

PORT     STATE SERVICE      REASON  VERSION
80/tcp   open  http         syn-ack Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)
| http-methods: 
|   Supported Methods: HEAD GET POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Heed Solutions
135/tcp  open  msrpc        syn-ack Microsoft Windows RPC
443/tcp  open  ssl/http     syn-ack Apache httpd 2.4.46 ((Win64) OpenSSL/1.1.1j PHP/7.3.27)
| http-methods: 
|   Supported Methods: HEAD GET POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-title: Heed Solutions
| ssl-cert: Subject: commonName=localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2009-11-10T23:48:47
| Not valid after:  2019-11-08T23:48:47
| MD5:   a0a4 4cc9 9e84 b26f 9e63 9f9e d229 dee0
| SHA-1: b023 8c54 7a90 5bfa 119c 4e8b acca eacf 3649 1ff6
| -----BEGIN CERTIFICATE-----
| MIIBnzCCAQgCCQC1x1LJh4G1AzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDEwls
| b2NhbGhvc3QwHhcNMDkxMTEwMjM0ODQ3WhcNMTkxMTA4MjM0ODQ3WjAUMRIwEAYD
| VQQDEwlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMEl0yfj
| 7K0Ng2pt51+adRAj4pCdoGOVjx1BmljVnGOMW3OGkHnMw9ajibh1vB6UfHxu463o
| J1wLxgxq+Q8y/rPEehAjBCspKNSq+bMvZhD4p8HNYMRrKFfjZzv3ns1IItw46kgT
| gDpAl1cMRzVGPXFimu5TnWMOZ3ooyaQ0/xntAgMBAAEwDQYJKoZIhvcNAQEFBQAD
| gYEAavHzSWz5umhfb/MnBMa5DL2VNzS+9whmmpsDGEG+uR0kM1W2GQIdVHHJTyFd
| aHXzgVJBQcWTwhp84nvHSiQTDBSaT6cQNQpvag/TaED/SEQpm0VqDFwpfFYuufBL
| vVNbLkKxbK2XwUvu0RxoLdBMC/89HqrZ0ppiONuQ+X2MtxE=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds syn-ack Windows 10 Pro 19042 microsoft-ds (workgroup: WORKGROUP)
5985/tcp open  http         syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
6379/tcp open  redis        syn-ack Redis key-value store
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows XP|7 (89%)
OS CPE: cpe:/o:microsoft:windows_xp::sp3 cpe:/o:microsoft:windows_7
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows XP SP3 (89%), Microsoft Windows XP SP2 (86%), Microsoft Windows 7 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/16%OT=80%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=60CA7AA9%P=x86_64-pc-linux-gnu)
SEQ(SP=101%GCD=1%ISR=109%TI=I%II=I%SS=S%TS=U)
OPS(O1=M54DNW8NNS%O2=M54DNW8NNS%O3=M54DNW8%O4=M54DNW8NNS%O5=M54DNW8NNS%O6=M54DNNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%TG=80%W=FFFF%O=M54DNW8NNS%CC=N%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: ATOM; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -7h10m03s, deviation: 4h02m30s, median: -9h30m04s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 40777/tcp): CLEAN (Timeout)
|   Check 2 (port 38781/tcp): CLEAN (Timeout)
|   Check 3 (port 39922/udp): CLEAN (Timeout)
|   Check 4 (port 58281/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 10 Pro 19042 (Windows 10 Pro 6.3)
|   OS CPE: cpe:/o:microsoft:windows_10::-
|   Computer name: ATOM
|   NetBIOS computer name: ATOM\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2021-06-16T05:56:06-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-06-16T12:56:09
|_  start_date: N/A

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   400.40 ms 10.10.14.1
2   400.65 ms 10.10.10.237

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Jun 16 18:26:49 2021 -- 1 IP address (1 host up) scanned in 68.15 seconds
```

![[Pasted image 20210616183224.png]]

![[Pasted image 20210616183346.png]]