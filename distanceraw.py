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

frequency = 2462 # Mhz 
signalLevel = -70 # dbm
distance = 10 ** ((27.55 - (20 * math.log10(frequency)) + math.fabs(signalLevel))/20)
print("Static Test: %2.2f m" % distance)
ssids = []
signalStrength = []  
ap_info = rssi_scanner.getAPinfo(sudo=True)
print(ap_info)
for k in ap_info:
    print(k)



