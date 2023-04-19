from braviarc import BraviaRC

ip_address = "192.168.0.108"

braviarc = BraviaRC(ip_address)

pin = "3007"

braviarc.connect(pin, ip_address, "bravia")

print(braviarc.load_source_list())

if braviarc.is_connected():
    print("connected")
    braviarc.select_source("HDMI 2")
else:
    print("could not connect")
