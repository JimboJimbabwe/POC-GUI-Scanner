#!/bin/bash

nmap -p80 --script=http-security-headers 127.0.0.1;
