#!/bin/bash
#hier werden die Monitor INterfaces erstellt
anzahl=$1
wlaninterface=$2
param=$#

	read -p "Wie viele Mon Interfaces sollen erstellt werden?" anzahl
	read -p "Wie heisst das WLAN-interface: " wlanIface
	echo "--#########################################################################--"
	echo "es werden ${anzahl} an interfaces erstellt vom Ursprung ${wlanIface} erstellt"
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
	echo "------------mon${z} erstellt"--------------
	echo "--#######################################--"
done

read -p "Enter drücken um alle mons wieder zu löschen" enter
for ((z=0;z<anzahl;z++))
do
iw mon${z} del
	echo "--#######################################--"
	echo "------------------mon${z} gelöscht---------"
	echo "--#######################################--"
done
