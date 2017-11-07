from pyntc import ntc_device as NTC

HOST = '192.168.122.10'
sw1 = NTC(host=HOST, username='test', password='test', device_type="cisco_ios_ssh")
sw1.open()

sw1_runningConfig = sw1.backup_running_config('SW_'+ HOST)
print("All Done! Browse the current directory to locate the backups!")