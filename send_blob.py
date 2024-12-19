from azure.storage.blob import BlobServiceClient
import time

CONTAINER_NAME = "chess"
BLOB_NAME = "new_blob.jpeg"
IMAGE_PATH = "pookie.jpeg"

def upload_image_to_blob():
    try:
        blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=chessimages;AccountKey=BVfdVF+YuBZzNd1qM+oel02RJuScISiwsa+dLstiEJKY0MhH6OD+rSSd/1Nl6iVwyRfai09lgJiO+ASt23PaWA==;EndpointSuffix=core.windows.net")

        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        with open(IMAGE_PATH, "rb") as image_file:
            blob_client.upload_blob(image_file, overwrite=True)
        
        print(f"Image successfully uploaded to Blob Storage at: {blob_client.url}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        error_file_path = "errors.txt"
        with open(error_file_path, "a") as file:
            file.write(str(time.time) + ": " + str(e) + "\n")

upload_image_to_blob()
