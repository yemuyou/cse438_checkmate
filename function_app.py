import logging
import azure.functions as func
import subprocess
import time

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="chess",
                               connection="chessimages_STORAGE") 
    
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob "
                 f"Name: {myblob.name} "
                 f"Blob Size: {myblob.length} bytes")

    try:
        blob_data = myblob.read()
        output_path = "./binary/output_" + str(time.time()) + ".bin"
        with open(output_path, "wb") as file:
            file.write(blob_data)
    except Exception as e:
        error_file_path = "errors.txt"
        with open(error_file_path, "a") as file:
            file.write(str(time.time) + ": " + str(e) + "\n")
            
    logging.info("Blob byte stream saved as 'output_image_bytes.bin'")