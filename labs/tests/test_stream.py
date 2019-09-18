import pytest
import time
import stl_path
from trex_stl_lib.api import *
"""
An example on how to use TRex for functional tests

"""


@pytest.mark.parametrize("protocol", ["TCP", "UDP", "ICMP"])
def test_single_continuous_stream(trex, protocol):
    tx_port, rx_port = trex.get_all_ports()
    trex.reset(ports=[tx_port, rx_port])
     # create a base pkt
    base_pkt = Ether()/IP(src="16.0.0.1",dst="48.0.0.1")/UDP(dport=12,sport=1025)

    # later on we will use the packet builder to provide more properties
    pkt = STLPktBuilder(base_pkt)

    # create a stream with a rate of 1000 PPS and continuous
    s1 = STLStream(packet = pkt, mode = STLTXCont(pps = 1000))

    # add the streams
    trex.add_streams(s1, ports = tx_port)

    # start traffic with limit of 3 seconds (otherwise it will continue forever)
    trex.start(ports = tx_port, duration = 3)

    # hold until traffic ends
    trex.wait_on_traffic()
