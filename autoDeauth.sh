#!/bin/bash
#hier werden die Monitor INterfaces erstellt
anzahl=$1
wlaninterface=$2
param=$#
	read -p "Please enter the name of the Network? " essid

echo "[i] I create an interface to listen to"
iw wlan0 interface add mon0 type monitor
sleep 2  		
	airmon-ng check kill
	
	ifconfig mon0 down
	macchanger -r mon0
	ifconfig mon0 up

	echo "------------mon0 created--------------"

( airodump-ng -w testdump -o csv --essid Maritim-Free-WIFI mon0 )
#sleep "${WAITSECS}"

input="testdump-01.csv"
# Set "," as the field separator using $IFS 
# and read line by line using while read combo 
bssidArr[0]=test
counter=0

while IFS=',' read -r f1 f2 f3 f4 f5 f6 f7 f8 f9
do 
echo "${counter}"
echo "${f1}"
if [[ $f1 == Station* ]]
then
	break
fi
  bssidArray[counter]=$f1
counter=$((counter+1))
done < "$input"
echo ${bssidArray[*]}


#killall airodump-ng
#rm testdump*
iw mon0 del

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
