#!/bin/bash
#hier werden die Monitor INterfaces erstellt
anzahl=$1
wlaninterface=$2
param=$#
	read -p "How many interfaces do you want to generate? " anzahl
	read -p "What`s the name of the pysical interface " wlanIface
	echo "--#########################################################################--"
	echo "we will create ${anzahl} of interfaces from the source ${wlanIface}          "
	echo "--#########################################################################--"

counter=0

for ((z=0;z<anzahl;z++))
do
 	
iw ${wlanIface} interface add mon${z} type monitor
sleep 2  		
	airmon-ng check kill
	
	ifconfig mon${z} down
	macchanger -r mon${z}
	ifconfig mon${z} up
	echo "--#######################################--"
	echo "------------mon${z} created--------------"
	echo "--#######################################--"
done

read -p "press enter to delete the interfaces" enter
for ((z=0;z<anzahl;z++))
do
iw mon${z} del
	echo "--#######################################--"
	echo "------------------mon${z} deleted---------"
	echo "--#######################################--"
done
