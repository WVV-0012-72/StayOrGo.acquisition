# WIFI_Distance

Dies ist nur ein Prrof on Concept um eine möglichst einfache Formel zur Bestimmung der Distanz 
ziswchen WLAN Devices zu ermitteln. 
Der Test läuft auf einem Raspberry PI 3+ mit Python 3.7 mit Thonny. 


Benötigt:  math and rrsi 
rssi kann in Thonny via PiPy instaliert werden (Bugfix notwendig, siehe distance.py) 

Ergebnisse  

>>> %Run distance.py

Static Test: 30.63 m <- nur statich 
Die SSID sind anonymsiert und Accesspoint in meiner Umgebung. 
SSID_Mesh ist mein Fritzbox Mesh WLAN. 

SSID:  SSID1  Distance: 13.68 m

SSID:  SSDI_Mesh  Distance: 38.57 m <- Ein Stockwerk unter mir 

SSID:  NOSSID   Distance: 8.63 m

SSID:  SSID2  Distance: 38.57 m

SSID:  SSDI_Mesh  Distance: 2.73 m <- In ca. 4 Meter Entfernung 

SSID:  NOSSID  Distance: 12.20 m 

SSID:  SSID3  Distance: 153.54 m

Ich schätze den Messfehler auf 2-3 Meter bei Verwendung der einfachen Formel. 

Siehe: 
Berechnung der Distance auf Basis der Signalstärke

https://stackoverflow.com/questions/11217674/how-to-calculate-distance-from-wifi-router-using-signal-strength#11249007

Kanalabhängigkeit (Frequenz) ist relativ schwach, kann bei Bedarf berücksichtigt werden. 

Weiter Quellen: 
Kurz erklärt: Positionsbestimmung im WLAN
https://www.heise.de/select/ix/2019/10/1923312203089947066

Nächst Schritte:

Überprüfen mit der in rssid enthaltenen Distanzfunktion



