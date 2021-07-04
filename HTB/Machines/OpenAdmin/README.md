# OpenAdmin Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 10:10:26 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.171
Warning: 10.10.10.171 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.171
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-07-02 10:10:26 -06 for 1072s
Not shown: 65273 closed ports, 260 filtered ports
Reason: 65273 conn-refused and 260 no-responses
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Jul  2 10:28:18 2021 -- 1 IP address (1 host up) scanned in 1071.87 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Fri Jul  2 10:19:17 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.10.171
Nmap scan report for 10.10.10.171
Host is up, received echo-reply ttl 63 (0.16s latency).
Scanned at 2021-07-02 10:19:18 -06 for 20s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b:98:df:85:d1:7e:f0:3d:da:48:cd:bc:92:00:b7:54 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcVHOWV8MC41kgTdwiBIBmUrM8vGHUM2Q7+a0LCl9jfH3bIpmuWnzwev97wpc8pRHPuKfKm0c3iHGII+cKSsVgzVtJfQdQ0j/GyDcBQ9s1VGHiYIjbpX30eM2P2N5g2hy9ZWsF36WMoo5Fr+mPNycf6Mf0QOODMVqbmE3VVZE1VlX3pNW4ZkMIpDSUR89JhH+PHz/miZ1OhBdSoNWYJIuWyn8DWLCGBQ7THxxYOfN1bwhfYRCRTv46tiayuF2NNKWaDqDq/DXZxSYjwpSVelFV+vybL6nU0f28PzpQsmvPab4PtMUb0epaj4ZFcB1VVITVCdBsiu4SpZDdElxkuQJz
|   256 dc:eb:3d:c9:44:d1:18:b1:22:b4:cf:de:bd:6c:7a:54 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHqbD5jGewKxd8heN452cfS5LS/VdUroTScThdV8IiZdTxgSaXN1Qga4audhlYIGSyDdTEL8x2tPAFPpvipRrLE=
|   256 dc:ad:ca:3c:11:31:5b:6f:e6:a4:89:34:7c:9b:e5:50 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBcV0sVI0yWfjKsl7++B9FGfOVeWAIWZ4YGEMROPxxk4
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.2 - 4.9 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.18 (94%), Linux 3.16 (93%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 5.1 (93%), Oracle VM Server 3.4.2 (Linux 4.1) (93%), Android 4.1.1 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=7/2%OT=22%CT=%CU=32861%PV=Y%DS=2%DC=T%G=N%TM=60DF3C9A%P=x86_64-pc-linux-gnu)
SEQ(SP=105%GCD=1%ISR=107%TI=Z%CI=Z%II=I%TS=A)
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

Uptime guess: 16.020 days (since Wed Jun 16 09:51:22 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   156.18 ms 10.10.14.1
2   156.23 ms 10.10.10.171

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul  2 10:19:38 2021 -- 1 IP address (1 host up) scanned in 20.63 seconds
```

## Port 80 Enumeration

Nothing more default webpage

![](Images/Pasted%20image%2020210702214302.png)

So i move forward for directory bruteforce.

![](Images/Pasted%20image%2020210702224323.png)

And while surfing that directory on webpage shows it is static webpage.

![](Images/Pasted%20image%2020210702224432.png)

But while searching on webpage, 
Its login tab is redirect to other directory and from where we got the version.

![](Images/Pasted%20image%2020210702224553.png)

While searching for exploit found it is vulnerable to RCE.

![](Images/Pasted%20image%2020210702225005.png)

```bash
Exploit : 
https://github.com/amriunix/ona-rce
https://www.exploit-db.com/exploits/47691
```

So here we got a shell.

![](Images/Pasted%20image%2020210702225102.png)

Let's take persistance

![](Images/Pasted%20image%2020210702225414.png)

## Previlege Escalation

```php
<?php

$ona_contexts=array (
  'DEFAULT' => 
  array (
    'databases' => 
    array (
      0 => 
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
);
```

```bash
Credentials SSH: 
jimmy:n1nj4W4rri0R!
```

While enumerating for the other user got the folder called internal and while enumerating more shows it is running on internal port 52846

![](Images/Pasted%20image%2020210702231733.png)

![](Images/Pasted%20image%2020210702231613.png)

So i did the tunneling

![](Images/Pasted%20image%2020210702231818.png)

And now we have a access of internal panel.

 ![](Images/Pasted%20image%2020210702231831.png)
 
 But we don't have a password and while looking to the internal folder we got the password hash, 
 And i cracked it using the 
 
 ```bash
Hash: 00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758eebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1

Credentials Web:
jimmy:Revealed
```

After login we got the SSH key

![](Images/Pasted%20image%2020210702232344.png)

But the id_rsa is password protected.

So Let's crack its password. 

![](Images/Pasted%20image%2020210702232623.png)

![](Images/Pasted%20image%2020210702232645.png)

And here we got id_rsa key password.

```bash
Credentials SSH id_rsa: bloodninjas
```

## Privelege Escalation Root 

![](Images/Pasted%20image%2020210702232750.png)

![](Images/Pasted%20image%2020210702233004.png)

Rooted.