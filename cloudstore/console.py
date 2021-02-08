from cloud_store import GCStore

gcs_store = GCStore()
print(gcs_store.upload("new_test_bucket_unrahul", "data/test_file.txt").result())
print(gcs_store.download("new_test_bucket_unrahul", "data/test_file.txt", "sds.txt").result())
