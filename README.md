# StayOrGo Wifi_Distance Measurement


Dies ist lediglich ein Proof of Concept mit einem möglichst einfachen Ansatz die Abstände zwischen 
WLAN Devices zu ermitteln.

Der Test läuft auf einem Raspberry PI 3+ mit Python 3.7 und Thonny. 

Die Frequenz / Kanal sollte berücksichtigt werden. Die Verwendung von 2.4 und 5 Ghz WLAN erhebliche Unterschiede. 
Die rssi Bibliothek wurde ertüchtigt die Senedfrequenz mit auszugeben. 
 
# Requirements
* Linux/Raspberry 
* Python3
  * math
  * rssi (https://pypi.org/project/rssi/ mit kleine Anpassungen / Biugfix und Ausgabe der Kanalfrequenz )

# Usage
## start measurement
$ python3 distance.py


# Test Ergebnisse  
>>> %Run distance.py

Static Test: 30.63 m <- nur statisch 
Die SSIDs sind anonymsiert, es sind Accesspoint in meiner direkten Umgebung. 
SSID_Mesh ist mein Fritzbox Mesh WLAN. 

SSID:  SSID1  Distance: 14 m

SSID:  SSDI_Mesh  Distance: 39 m <- Ein Stockwerk unter mir 

SSID:  NOSSID   Distance: 9 m

SSID:  SSID2  Distance: 39 m

SSID:  SSDI_Mesh  Distance: 3 m <- In ca. 4 Meter Entfernung 

SSID:  NOSSID  Distance: 12 m 

SSID:  SSID3  Distance: 153 m


Die Berechnung basiert auf einer einfachen Formel: 

`distance = 10 ** ((27.55 - (20 * math.log10(freq)) + math.fabs(signalLevel))/20)`

Dieser relativ einfache Ansatz geht allerdings von zwei isotropischen Antennen zwischen Sender und Empfänger aus. 
Das führt, da auch Dämpfung, Reflektionen, usw... überhaupt nicht berücksichtigt werden 
zu stark verfälschten Ergebnissen. Die so ermittelten Ergebnisse sind daher für eine sichere 
Distanzmessung nicht geeignet.  

Daher wird dieser Ansatz nicht weiterverfolgt und auf die Abstandmessung verzichtet. 

### Weiterführende Informationen 
 
Berechnung der Distance auf Basis der Signalstärke

https://stackoverflow.com/questions/11217674/how-to-calculate-distance-from-wifi-router-using-signal-strength#11249007

Kurz erklärt: Positionsbestimmung im WLAN
So könnte es in Zukunft besser funktioniern:
https://www.heise.de/select/ix/2019/10/1923312203089947066






