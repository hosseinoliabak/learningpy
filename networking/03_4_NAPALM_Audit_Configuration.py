from napalm import get_network_driver

driver = get_network_driver('ios')
sw1 = driver('192.168.122.10', 'test', 'test')
sw1.open()

print('Accessing 192.168.122.10...')
sw1.load_merge_candidate(filename='ACL1.cfg')

diffs = sw1.compare_config()
print(diffs)

sw1.close()