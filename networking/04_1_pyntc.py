from pyntc import ntc_device as NTC
import json

sw1 = NTC(host='192.168.122.10', username='test', password='test', device_type="cisco_ios_ssh")
sw1.open()

ios_output = sw1.facts
print(json.dumps(ios_output, indent=4))