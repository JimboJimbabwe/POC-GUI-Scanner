#!/bin/bash

nmap --script smb-os-discovery.nse -p445 -oN /home/kali/Desktop/TestFolder/SMB.txt 127.0.0.1;
cat /home/kali/Desktop/TestFolder/SMB.txt;
