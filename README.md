# Flash
Flashes a file (.iso, .img) to an SD-card or USB-stick.

# License
Licensed under the GNU General Public License 3.0.

# How to Use:
(FYI. THERE IS NO ACTUAL SOURCE CODE YET! THIS IS AN ESTIMATE OF HOW IT MIGHT WORK)

To install Flash, first clone the repository: ```git clone https://github.com/codingelephants-gpt/flash.git/```
After that, you can do one of the following two options:
1. Move to local PATH
2. Move to global PATH

If you chose to move to local PATH, follow the next steps:
1. First, make the script executable: `chmod +x ~/flash/src/flash.py`
2. If the script doesn't have `#!usr/bin/env python3` on top of it, add it using `nano` or any other text editor.
3. Move the script to the local PATH: `mv ~/flash/src/flash.py ~/.local/flash`.

If you chose to move to global PATH, follow the next steps:
1. First, make the script executable: `chmod +x ~/flash/src/flash.py`
2. If the script doesn't have `#!usr/bin/env python3` on top of it, add it using `nano` or any other text editor.
3. Move the script to the global PATH: `sudo mv ~/flash/src/flash.py /usr/bin/flash`.

To use Flash, use `flash yourimage.iso /media/yourusername/usb-or-sdcard`.
