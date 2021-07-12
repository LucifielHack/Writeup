# Archetype Hackthebox Writeup

## All Ports Scan

```bash
# Nmap 7.91 scan initiated Mon Jul  5 19:08:48 2021 as: nmap -T4 -sT -vv -p- -oA nmap/allports 10.10.10.27
Warning: 10.10.10.27 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.10.10.27
Host is up, received echo-reply ttl 127 (0.15s latency).
Scanned at 2021-07-05 19:08:48 -06 for 1320s
Not shown: 65071 closed ports, 452 filtered ports
Reason: 65071 conn-refused and 452 no-responses
PORT      STATE SERVICE      REASON
135/tcp   open  msrpc        syn-ack
139/tcp   open  netbios-ssn  syn-ack
445/tcp   open  microsoft-ds syn-ack
1433/tcp  open  ms-sql-s     syn-ack
5985/tcp  open  wsman        syn-ack
47001/tcp open  winrm        syn-ack
49664/tcp open  unknown      syn-ack
49665/tcp open  unknown      syn-ack
49666/tcp open  unknown      syn-ack
49667/tcp open  unknown      syn-ack
49668/tcp open  unknown      syn-ack
49669/tcp open  unknown      syn-ack

Read data files from: /usr/bin/../share/nmap
# Nmap done at Mon Jul  5 19:30:48 2021 -- 1 IP address (1 host up) scanned in 1319.86 seconds
```

## Complete Scan

```bash

```

## SMB Enumeration

![[Pasted image 20210706054155.png]]

```xls
<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration>
```