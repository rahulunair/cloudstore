from cloudstore.cloud_store import store

# store = store("gcp")
#store = store("aws")
store = store("azure")
store.upload(bucket="test3bucketunrahul", file_name="data/test_file.txt")
store.download("test3bucketunrahul", "data/test_file.txt", "sds.txt")
