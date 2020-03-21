# WIFI_Distance

Require math and rrsi 
rssi available via PiPy (Bugfix notwendig, siehe distance.py) 

Ergebniss 

>>> %Run distance.py
Static Test: 30.63 m
SSID:  SSID1  Distance: 13.68 m
SSID:  SSDI_Mesh  Distance: 38.57 m
SSID:  NOSSID   Distance: 8.63 m
SSID:  SSID2  Distance: 38.57 m
SSID:  SSDI_Mesh  Distance: 2.73 m
SSID:  NOSSID  Distance: 12.20 m
SSID:  SSID3  Distance: 153.54 m

Siehe: 
Berechnung der Distance auf Basis der Signalstärke
https://stackoverflow.com/questions/11217674/how-to-calculate-distance-from-wifi-router-using-signal-strength#11249007

Kanalabhängikeit (Frequenz) ist relativ schwach, kann bei Bedarf berücksichtigt werden. 

Weiter Quellen: 
Kurz erklärt: Positionsbestimmung im WLAN
https://www.heise.de/select/ix/2019/10/1923312203089947066

Nächst Schritte:

Überprüfen mit der in rssid enthaltenen Distancefunktion



