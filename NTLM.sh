#!/bin/bash
nmap -p 80 --script http-ntlm-info --script-args http-ntlm-info.root=/root/ 127.0.0.1
