from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=chessimages;AccountKey=BVfdVF+YuBZzNd1qM+oel02RJuScISiwsa+dLstiEJKY0MhH6OD+rSSd/1Nl6iVwyRfai09lgJiO+ASt23PaWA==;EndpointSuffix=core.windows.net"
container_name = "chess"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob="test_upload.jpg")

image_path = "/home/cosmo/Desktop/Test/image.jpg"

with open(image_path, "rb") as data:
	blob_client.upload_blob(data)
	print("Upload successful")

