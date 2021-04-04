from google.cloud import storage
def download_blob(bucket_name, source_blob_name):
    """Downloads a blob from the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob_ = bucket.blob(source_blob_name)

    return blob_