from pyntc import ntc_device as NTC
import json

sw1 = NTC(host='192.168.122.10', username='test', password='test', device_type="cisco_ios_ssh")
sw1.open()

ios_output = sw1.facts

sw1.config_list(['router ospf 1',
                 'network 0.0.0.0 255.255.255.255 area 0'])