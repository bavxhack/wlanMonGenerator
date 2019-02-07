

<h3> A short script to create a number of monitor interfaces from an existing wlan-interface</h3>



# features:
  * choose number of monitor-interfaces<br>
  * select wlan-interface name<br>
  

# requirements:
  Kali Linux  with root privileges<br>
  the aireplay-ng to deauth the existing AP<br>


# downloading:
  <h3>"git clone https://github.com/bavxhack/wlanMonGenerator.git"</h3>

# starting:
## Autodeauth all WIFI-Hotspots with the same ESSID in the Area
  * Automatic Deauth the selected WIFI-Interface. The Script opens a new Window which collects all WIFI-NEtworks with the given ESSID. To stop the searching prozess press CTR+C in the window with the airmon-ng. This could be more than one BSSID. All found BSSIDs will be Deauthed in a circular Way.
  * kali Linux -> python3 autoDeauth.py "{ESSID}" {WLAN-interface}
  python3 autoDeauth.py "{ESSID}" {WLAN-interface}
  
## Create a new monitoring Interface
  * Kali Linux -> "bash monIface.sh<br>
 
# Possible Szenario
Find your target-WIFI-AP
autodeauth the target.

open your own MITM-AP so your BSSID is not in the autodeauth-list so, all clients connect to your AP and will be disconnected if they connect to the target BSSIDs

# disclaimer:
  I'm not responsible for anything you do with this program, so please only use it for good and educational purposes.
