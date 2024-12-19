import os
import time
import subprocess

folder_to_monitor = "./image"

existing_files = set(os.listdir(folder_to_monitor))

print(f"Monitoring folder: {folder_to_monitor}...")
try:
    while True:
        current_files = set(os.listdir(folder_to_monitor))
        
        new_files = current_files - existing_files
        print(new_files)
        if new_files:
            for new_file in new_files:
                input_string = "--input=../image/" + str(new_file)
                output_string = "--output=../modified_images/" + str(new_file)
                subprocess.run(["python3.7", "main.py", "detect", input_string, output_string], cwd="neural-chessboard") 
                file_path = folder_to_monitor + "/" + str(new_file) 
                os.remove(file_path)
        
        existing_files = current_files
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
