from cloudstore.cloud_store import store

gcs_store = store("gcp")
print(
    gcs_store.upload(
        bucket="new_test_bucket_unrahul", file="data/test_file.txt"
    ).result()
)
print(
    gcs_store.download(
        "new_test_bucket_unrahul", "data/test_file.txt", "sds.txt"
    ).result()
)
