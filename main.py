import os
import sys
sys.path.append(os.path.abspath('.'))

from piclap import *
from bravia import tv_volume_up, hdmi_switch, tv_turn_on, tv_turn_off, tv_volume_up, tv_volume_down

class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        Settings.__init__(self)
        self.method.value = 10000

    def on1Claps(self):
        tv_turn_on()
    def on2Claps(self):
        tv_turn_off()
    def on3Claps(self):
        tv_volume_up()
    def on4Claps(self):
        tv_volume_down()
    def on5Claps(self):
        tv_volume_down()
    def on6Claps(self):
        tv_volume_down()

def main():
    config = Config()
    listener = Listener(config=config, calibrate=False)
    listener.start()


if __name__ == '__main__':
    main()
