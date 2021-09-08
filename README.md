# Ledshim-Off
This repo contains a simple script that uses a [Pimoroni Ledshim](https://shop.pimoroni.com/products/led-shim) to indicate when a Pi shutdowns/reboots

## Install
1. Slip the Ledshim on your Pi. 
2. Clone this repo to the Pi and rename it to `ledshim-off`. It's easiest if you clone it into your home directory of the `Pi` cause the paths in the scripts and service are hardcoded like so. 
3. Make a symlink from [`ledshim-off.sh`](https://github.com/UnsignedArduino/Ledshim-Off/blob/main/ledshim-off.sh) to `/usr/lib/systemd/system-shutdown` so that it is executed when the Pi shutdowns/reboots. 
