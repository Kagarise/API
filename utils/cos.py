import requests

from qcloud_cos import CosConfig, CosS3Client

from config import cos_config

config = CosConfig(Region=cos_config['Region'], SecretId=cos_config['SecretId'], SecretKey=cos_config['SecretKey'])
client = CosS3Client(config)


def all_bucket_detail():
    try:
        response = client.list_buckets()
        return response
    except:
        return None


def create_bucket(bucket_name):
    try:
        client.create_bucket(
            Bucket=f'{bucket_name}-{cos_config["Id"]}'
        )
        return True
    except:
        return False


# {'Key': '1620533083236.jpg',
# 'LastModified': '2021-05-09T10:38:41.000Z',
# 'ETag': '"a65ec2be1c8d3f901c8fb37260fcb9c9"',
# 'Size': '3657399',
# 'Owner': {'ID': '1304519045', 'DisplayName': '1304519045'},
# 'StorageClass': 'STANDARD'}
def bucket_detail(bucket_name, prefix="", Delimiter="/"):
    try:
        marker = ""
        data = []
        while True:
            response = client.list_objects(
                Bucket=bucket_name,
                Prefix=prefix,
                Delimiter=Delimiter,
                Marker=marker
            )
            data += response['Contents']
            if response['IsTruncated'] == 'false':
                break
            marker = response['NextMarker']
        return data
    except:
        return None


def upload_url_file(bucket_name, url, file_path):
    try:
        stream = requests.get(url)
        client.put_object(
            Bucket=bucket_name,
            Body=stream,
            Key=file_path
        )
        return True
    except:
        return False


def upload_local_file(bucket_name, local_file_path, file_path):
    try:
        client.upload_file(
            Bucket=bucket_name,
            LocalFilePath=local_file_path,
            Key=file_path,
            PartSize=1,
            MAXThread=10,
            EnableMD5=False
        )
        return True
    except:
        return False


def download_file(bucket_name, file_path, save_path):
    try:
        client.download_file(
            Bucket=bucket_name,
            Key=file_path,
            DestFilePath=save_path
        )
        return True
    except:
        return False


def delete_file(bucket_name, file_path):
    try:
        client.delete_object(
            Bucket=bucket_name,
            Key=file_path
        )
        return True
    except:
        return False
