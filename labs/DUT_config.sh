

sysctl -w net.ipv4.conf.all.forwarding=1
sysctl -w net.ipv6.conf.all.forwarding=1

ip addr add 1.1.1.1/28 dev eth4
ip link set up dev eth4
ip addr add 2.2.2.1/28 dev eth1
ip link set up dev eth1

ip route add 16.0.0.0/16 via 1.1.1.2
ip route add 48.0.0.0/16 via 2.2.2.2
