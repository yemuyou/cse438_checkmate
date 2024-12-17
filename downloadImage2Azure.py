from azure.storage.blob import BlobServiceClient

# Replace with your Azure Storage connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key"
container_name = "chess"  # Blob container name
blob_name = "chess.jpg"  # Name of the Blob file to download

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the Blob and save it to a local file
download_file_path = "./downloaded_chess.jpg"  # local file path to save the downloaded file
with open(download_file_path, "wb") as file:
    file.write(blob_client.download_blob().readall())

print(f"File downloaded to {download_file_path}")

