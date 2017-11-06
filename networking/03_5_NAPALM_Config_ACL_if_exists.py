from napalm import get_network_driver

driver = get_network_driver('ios')
sw1 = driver('192.168.122.10', 'test', 'test')
sw1.open()

print('Accessing 192.168.122.10...')
sw1.load_merge_candidate(filename='ACL1.cfg')

diffs = sw1.compare_config()
print(diffs)
if len(diffs) > 0:
    sw1.commit_config()
else:
    print('No changes required!')
    sw1.discard_config()

sw1.close()