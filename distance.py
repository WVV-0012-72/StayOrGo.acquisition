'''
    Simple WIFI Distance calculator
    Proof of concept (running on Raspberry PI 3+)
    libraries requires math and rssi
    rssi need a path for Python3:
    Add raw_output = raw_output.decode('utf-8') before return
    
    # Returns all output in a dictionary for easy retrieval.
    raw_output = raw_output.decode('utf-8')
    return {'output':raw_output,'error':raw_error}
'''

import math
from rssi.rssi import *
interface  = 'wlan0'
rssi_scanner = RSSI_Scan(interface)

# static test 
freq = 2462 # Mhz 
signalLevel = -70 # dbm
distance = 10 ** ((27.55 - (20 * math.log10(freq)) + math.fabs(signalLevel))/20)
print("Static Test: %2.2f m" % distance)
# list of detectect networks
ssids = []
# not used
signalStrength = []
# gather network information 
ap_info = rssi_scanner.getAPinfo(networks=ssids,sudo=True)
# print information and calculate distance 
for k in ap_info:
    distance = 10 ** ((27.55 - (20 * math.log10(k['frequency']*1000)) + math.fabs(k['signal']))/20)
    print("SSID: ", k['ssid'] ," MAC: ", k['address'], " Frequency: ", int(k['frequency']*1000) , " Signal Level: ", k['signal']  , " Distance: %2.2f m" % distance) 



