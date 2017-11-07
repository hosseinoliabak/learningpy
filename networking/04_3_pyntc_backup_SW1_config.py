from pyntc import ntc_device as NTC

HOST = '192.168.122.10'
sw1 = NTC(host=HOST, username='test', password='test', device_type="cisco_ios_ssh")
sw1.open()

sw1_runningConfig = sw1.running_config

with open("Switch_"+ HOST+ ".conf", "w") as saveOutput:
    print("Saving the configuration of "+ HOST+ "...")
    saveOutput.write(sw1_runningConfig)
print("All Done! Browse the current directory to locate the backups!")