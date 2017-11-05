from napalm import get_network_driver
import json

def print_bgp_neighbors(ip):
    driver = get_network_driver('ios')
    iosv = driver(ip, 'test', 'test')
    iosv.open()
    bgp_neighbors = iosv.get_bgp_neighbors()
    print(json.dumps(bgp_neighbors, sort_keys=True, indent=4))
    iosv.close()


bgplist= ['192.168.122.10', '192.168.122.30']

for ip in bgplist:
    print("Gathering the BGP neighbor information of: "+ ip)
    print_bgp_neighbors(ip)
