from napalm import get_network_driver

driver = get_network_driver('ios')
sw1 = driver('192.168.122.10', 'test', 'test')
sw1.open()

print('Accessing 192.168.122.10...')
sw1.load_merge_candidate(filename='ACL1.cfg')
sw1.commit_config()
sw1.close()