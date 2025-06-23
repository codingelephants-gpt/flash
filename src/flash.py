import os
import sys
import psutil
from tqdm import tqdm

def list_removable_devices():
    print("Status: Detecting removable devices...")
    partitions = psutil.disk_partitions(all=True)
    devices = []
    for p in partitions:
        if 'media' in p.mountpoint or 'run/media' in p.mountpoint:
            devices.append(p.device)
    return devices

def flash_image(image_path, device_path):
    block_size = 4096

    image_size = os.path.getsize(image_path)
    print(f"Status: Flashing {image_path} ({image_size} bytes) to {device_path}...")

    with open(image_path, 'rb') as img, open(device_path, 'wb') as dev:
        with tqdm(total=image_size, unit='B', unit_scale=True, desc='Flashing') as pbar:
            while True:
                data = img.read(block_size)
                if not data:
                    break
                dev.write(data)
                pbar.update(len(data))
        dev.flush()
        os.sync()
    print("Status: Flash complete!")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Status Error: This tool must be run as root.")
        sys.exit(1)

    if len(sys.argv) != 3:
        print("Usage: sudo flash <image.img> <device> (e.g., /dev/sdX)")
        sys.exit(1)

    image_file = sys.argv[1]
    target_device = sys.argv[2]

    if not os.path.exists(image_file):
        print("Status Error: Image file not found.")
        sys.exit(1)

    confirm = input(f"STATUS WARNING: This will erase all data on {target_device}. Continue? (y/N): ")
    if confirm.lower() != 'y':
        print("Aborted.")
        sys.exit(0)

    flash_image(image_file, target_device)
