#!/bin/bash

cd ScriptRepo;

echo "Enter victim IP: "
read IP

sudo sed -i "s/127.0.0.1/$IP/g" * ;

cd .. ;

