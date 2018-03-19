# Host Scanner

## A Python implementation to scan ports on a host using Nmap

## Usage

Clone the repository with:

```
$ git clone https://github.com/marcelogdeandrade/HostScanner
```

```
$ cd HostScanner/
```

You need root to get OS scan with nmap. Write your target as a parameter when executing the script.

Example:

```
$ sudo python scanner.py 192.168.0.106
```

## Output:

Example:

```
----------------------------------------------------
Host : 192.168.0.106 ()
State : up
OS : Linux, 	ver: 3.X
OS : Linux, 	ver: 4.X
----------
Protocol : tcp
port : 139	state : open 	service: Samba smbd
port : 445	state : open 	service: Samba smbd
```
