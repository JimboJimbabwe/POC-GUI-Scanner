#!/bin/bash

nmap -p80 --script http-csrf.nse 127.0.0.1;
