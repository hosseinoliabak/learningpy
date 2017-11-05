from napalm import get_network_driver
import json

driver = get_network_driver('ios')
sw1 = driver('192.168.122.10', 'test', 'test')
sw1.open()

sw_output = sw1.get_mac_address_table()
print(json.dumps(sw_output, sort_keys=True, indent=4))


sw_output = sw1.get_mac_address_table()
print(json.dumps(sw_output, sort_keys=True, indent=4))