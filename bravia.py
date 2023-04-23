from braviarc import BraviaRC
import subprocess

ip_address = "192.168.0.121"

braviarc = BraviaRC(ip_address)

pin = "0075"

def hdmi_switch():
    if braviarc.get_playing_info()["title"] == "HDMI 1/MHL":
        print("Switching to HDMI 4")
        braviarc.select_source("HDMI 4")
    elif braviarc.get_playing_info()["title"] == "HDMI 4":
        print("Switching to HDMI 1: PC")
        braviarc.select_source("HDMI 1/MHL")
    else:
        print("Switching to HDMI 1: PC")
        braviarc.select_source("HDMI 1/MHL")
    #braviarc.select_source("HDMI 4")

def tv_volume_up():
    if braviarc.get_power_status() == "active":
        braviarc.volume_up()
    elif braviarc.get_power_status() == "standby":
        braviarc.turn_on()
    elif braviarc.get_power_status() == "off":
        braviarc.turn_on()

def tv_volume_down():
    if braviarc.get_power_status() == "active":
        braviarc.volume_down()
    elif braviarc.get_power_status() == "standby":
        braviarc.turn_on()
    elif braviarc.get_power_status() == "off":
        braviarc.turn_on()

def tv_turn_on():
    braviarc.setWolMode(True)
    if braviarc.get_power_status() == "active":
        subprocess.run("playerctl play-pause", shell=True)
    elif braviarc.get_power_status() == "standby":
        braviarc.turn_on()
    elif braviarc.get_power_status() == "off":
        braviarc.turn_on()

def tv_turn_off():
    if braviarc.get_power_status() == "active":
        print("TV is on")
        braviarc.turn_off()
        print("Turned off TV")
    elif braviarc.get_power_status() == "standby":
        print("TV is off")
        braviarc.turn_on()
        print("Turned on TV")
    elif braviarc.get_power_status() == "off":
        print("TV is off")
        braviarc.turn_on()
        print("Turned on TV")
    else:
        print("Could not get TV power status")
        braviarc.turn_off()
        print("Turned off TV")

braviarc.connect(None, ip_address, "genesis2")

#print(braviarc.load_source_list())

#if braviarc.is_connected():
#    print("connected")
#    braviarc.select_source("HDMI 2")
#else:
#    print("could not connect")
