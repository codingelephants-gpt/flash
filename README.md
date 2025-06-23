# Flash
Flashes a file (.iso, .img) to an SD-card or USB-stick.

# License
Licensed under the GNU General Public License 3.0.

# Requirements:
Requirements are found in requirements.txt.

# How to Use:
(FYI. THERE IS NO ACTUAL SOURCE CODE YET! THIS IS AN ESTIMATE OF HOW IT MIGHT WORK)

**IMPORTANT**: I haven't tested this yet, as i dont have an SD-card or USB-stick. So if someone want to sacrifice their stick/card for my terrible program: go for it!

To install Flash, first clone the repository: ```git clone https://github.com/codingelephants-gpt/flash.git/```
Then, run `python3 -m pip install -r requirements.txt`.
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

To use Flash, use `sudo flash <image.img (I DONT MEAN AN .png OR .jpg WITH THIS)> </dev/yourdevice>`.

**Note**: Sudo is needed for device writing, if your not admin: sorry not sorry!
