from io import BytesIO
from PIL import Image
import time
import os
import subprocess

def save_file_as_jpeg(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    image_bytes = BytesIO(file_data)
    image = Image.open(image_bytes)

    output_path = "./image/output_" + str(time.time()) + ".jpg"
    image.save(output_path, 'JPEG')

    print(f"Image saved as {output_path}")

folder_to_monitor = "./binary"

existing_files = set(os.listdir(folder_to_monitor))

print(f"Monitoring folder: {folder_to_monitor}...")
try:
    while True:
        current_files = set(os.listdir(folder_to_monitor))
        
        new_files = current_files - existing_files
        print(new_files)
        if new_files:
            for new_file in new_files:
                file_path = folder_to_monitor + "/" + str(new_file)
                save_file_as_jpeg(file_path)   
                os.remove(file_path)           
        
        existing_files = current_files
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")