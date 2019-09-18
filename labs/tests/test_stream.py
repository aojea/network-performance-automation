import pytest
import time
import stl_path
from trex_stl_lib.api import *
"""
An example on how to use TRex for functional tests

"""


def test_single_continuous_stream(trex):
    tx_port, rx_port = trex.get_all_ports()
    trex.reset(ports=[tx_port, rx_port])
     # create a base pkt
    base_pkt = Ether()/IP(src="16.0.0.1",dst="48.0.0.1")/UDP(dport=12,sport=1025)

    # create a stream with 100 packets and 5 pps
    s1 = STLStream(packet = STLPktBuilder(base_pkt),
                   mode   = STLTXSingleBurst(pps = 5, total_pkts = 20))

    # add the streams
    trex.add_streams(s1, ports = tx_port)

    # start traffic with limit of 10 seconds (otherwise it will continue forever)
    trex.start(ports = tx_port, duration = 10)

    # hold until traffic ends
    trex.wait_on_traffic()
    stats = trex.get_stats()
    ipackets  = stats[rx_port]['ipackets']
    assert(ipackets == 20 )


def test_bidirectional_continuous_stream(trex):
    burst_size = 10
    packets_sec = 2
    port_0, port_1 = trex.get_all_ports()
    # create a base pkts
    base_pkt_dir_a = Ether()/IP(src="16.0.1.1",dst="48.0.1.1")/TCP(dport=8812,sport=1025)
    base_pkt_dir_b = Ether()/IP(src="48.0.1.1",dst="16.0.1.1")/TCP(dport=1025,sport=8812)

    # let's pad to 300 bytes
    pad = (300 - len(base_pkt_dir_a)) * 'x'

    # create a stream with burst_size packets
    s1 = STLStream(packet = STLPktBuilder(base_pkt_dir_a/pad),
                   mode   = STLTXSingleBurst(pps = packets_sec, total_pkts = burst_size))

    # create a stream with burst_size packets
    s2 = STLStream(packet = STLPktBuilder(base_pkt_dir_b/pad),
                   mode   = STLTXSingleBurst(pps = packets_sec, total_pkts = burst_size))

    # prepare the ports
    trex.reset(ports = [port_0, port_1])

    # add the streams
    trex.add_streams(s1, ports = port_0)
    trex.add_streams(s2, ports = port_1)

    # start traffic with limit of 10 seconds (otherwise it will continue forever)
    trex.start(ports = [port_0, port_1], duration = 20)

    # hold until traffic ends
    trex.wait_on_traffic()
    stats = trex.get_stats()
    print stats
    ipackets  = stats['total']['ipackets']

    print(" Packets Received: {0} ".format(ipackets))
    # two streams X 2 ports
    assert(ipackets == (burst_size*2) )

