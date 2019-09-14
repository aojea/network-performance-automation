Install docker 

Install kvm

Install koko

go install github.com/redhat-nfvpe/koko

Launch trex

docker run -it --rm --privileged --cap-add=ALL -v /mnt/huge:/mnt/huge -v /sys/bus/pci/devices:/sys/bus/pci/devices -v /sys/devices/system/node:/sys/devices/system/node -v /dev:/dev aojea/trex

(optional) –net=host to use the host network

Create veth pair

 ip link add veth0 type veth peer name veth1
 ip addr add 10.1.0.1/24 dev veth0
 ip addr add 10.1.0.2/24 dev veth1
 ip link set veth0 up
 ip link set veth1 up

Configure Trex

cat > /etc/trex_cfg.yaml <<EOF
- port_limit    : 2
  version       : 2
  low_end       : true
  interfaces    : ["veth0", "veth1"]   # list of the interfaces to bind run ./dpdk_nic_bind.py --status
  port_info     :  # set eh mac addr

                 - ip         : 1.1.1.1
                   default_gw : 2.2.2.2
                 - ip         : 2.2.2.2
                   default_gw : 1.1.1.1
EOF


2.3. test commands
Run TRex stateless using: “./t-rex-64 -i -c 1”

In stateless console (“trex-console”) we do the following tests:
var1: start -f stl/bench.py -t size=64,vm=var1 -m <rate> --port 0 --force
cached: start -f stl/bench.py -t size=64,vm=cached -m <rate> --port 0 --force
latency: start -f stl/udp_1pkt_src_ip_split_latency.py -m <rate> --port 0 --force

