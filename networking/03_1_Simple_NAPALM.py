'''
get_facts()
    Returns a dictionary containing the following information:
        uptime - Uptime of the device in seconds.
        vendor - Manufacturer of the device.
        model - Device model.
        hostname - Hostname of the device
        fqdn - Fqdn of the device
        os_version - String with the OS version running on the device.
        serial_number - Serial number of the device
        interface_list - List of the interfaces of the device


get_interfaces()
    Returns a dictionary of dictionaries. The keys for the first dictionary will be the interfaces in the devices.
    The inner dictionary will containing the following data for each interface:
        is_up (True/False)
        is_enabled (True/False)
        description (string)
        last_flapped (int in seconds)
        speed (int in Mbit)
        mac_address (string)

'''
from napalm import get_network_driver
import json


driver = get_network_driver('ios')
sw1 = driver('192.168.122.10', 'test', 'test')
sw1.open()

# See Getters support matrix:
# https://napalm.readthedocs.io/en/latest/support/index.html
sw_output = sw1.get_facts()
print(json.dumps(sw_output, sort_keys=True, indent=4))

sw_output = sw1.get_interfaces()
print(json.dumps(sw_output, sort_keys=True, indent=4))

sw_output = sw1.get_mac_address_table()
print(json.dumps(sw_output, sort_keys=True, indent=4))


sw_output = sw1.get_arp_table()
print(json.dumps(sw_output, sort_keys=True, indent=4))


sw_output = sw1.ping('192.168.122.1')
print(json.dumps(sw_output, sort_keys=True, indent=4))

sw1.close()