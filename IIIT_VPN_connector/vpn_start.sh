#!/bin/bash

#VPN
echo "Enter Username : "
read uname
echo "Enter Password : "
stty -echo
read pass
stty echo
echo ""


vpnurl="https://vpn.iiit.ac.in/secure/linux.ovpn"
wget  --user="$uname" --password="$pass" "$vpnurl"
#echo 'nameserver 10.4.20.204' | cat - linux.ovpn > temp && mv temp linux.ovpn
sudo sed -i '1s/.*/nameserver 10.4.20.204/' /etc/resolv.conf
sed -i '15s/.*/group nogroup/' linux.ovpn
sudo mv linux.ovpn /etc/openvpn/iiithvpn.conf
sudo openvpn --config /etc/openvpn/iiithvpn.conf

service openvpn start
