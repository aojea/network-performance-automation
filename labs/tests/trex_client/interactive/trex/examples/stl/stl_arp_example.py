import stl_path
from trex.stl.api import *
import pprint

import time

def simple ():

    # create client
    #verbose_level = 'high'
    c = STLClient(verbose_level = 'error',server='csi-kiwi-02')
    passed = True
    
    try:
        # connect to server
        c.connect()

        my_ports=[0,1]

        # prepare our ports
        c.reset(ports = my_ports)
        c.set_service_mode([0,1])
        c.set_l3_mode(port=0, src_ipv4='1.1.5.2', dst_ipv4='1.1.5.1', vlan=100)

        pprint.pprint(c.get_port_info(my_ports))

        print((" is connected {0}".format(c.is_connected())))

        print((" number of ports {0}".format(c.get_port_count())))
        print((" acquired_ports {0}".format(c.get_acquired_ports())))
        # port stats


    except STLError as e:
        passed = False
        print(e)

    finally:
        c.disconnect()

    if passed:
        print("\nTest has passed :-)\n")
    else:
        print("\nTest has failed :-(\n")


# run the tests
simple()

