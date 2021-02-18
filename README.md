## CloudStore - Multi cloud store

A multi cloud storage API that can be used to upload and download contents.

## Supported clouds

- GCP
- AWS
- Azure

## Installation instructions

```bash
pip3 install cloudstore==0.1.0

```

## API usage

- Storing and downloading objects from GCP store

Download GCP store [credentials](https://console.cloud.google.com/apis/credentials/serviceaccountkey)

Set the credentials as an environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_creds.json> 
```

Create a storage [bucket](https://cloud.google.com/storage/docs/creating-buckets) in your gcp store, note: the bucketname has to be unique.

Once credential is set, you can use the API as below:


```bash
from cloudstore import store

gcp_store = store("gcp")
# a multithreaded upload, returns a future object
st.upload(<unique_bucket_name>, <file_name>)
# multithreaded download, returns a future object
st.download(<unique_bucket_name>, <remote_object_name>, <save_as_file_name>)
```
