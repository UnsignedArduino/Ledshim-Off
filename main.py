import time

import ledshim

ledshim.set_clear_on_exit()

ledshim.set_all(0, 0, 255)
ledshim.show()

time.sleep(1)

for left_pos in range(round(ledshim.NUM_PIXELS / 2)):
    ledshim.set_pixel(left_pos, 0, 0, 0)
    ledshim.set_pixel(ledshim.NUM_PIXELS - left_pos - 1, 0, 0, 0)
    ledshim.show()
    time.sleep(0.005)
