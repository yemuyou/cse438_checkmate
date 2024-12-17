from azure.storage.blob import BlobServiceClient

# Replace with your Azure Storage connection string
connection_string = "your connection_string"
container_name = "chess"  # Blob container name

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="chess1.jpg")

# Upload image file
with open("./image/chess1.jpg", "rb") as data:  # Replace with your file path
    blob_client.upload_blob(data)  # blob_client.upload_blob(data, overwrite=True)
    print("File uploaded successfully")

