from config import cos_config
from cos import bucket_detail, download_file, upload_local_file, upload_url_file

if __name__ == "__main__":
    name = "api"
    bucket_name = f'{name}-{cos_config["Id"]}'

    # print(upload_file(bucket_name=bucket_name, local_file_path="E:\\pixiv\\1620384002305.jpg", key="1620384002305.jpg"))

    # data = bucket_detail(bucket_name=bucket_name)
    # key = data[0]['Key']
    # download_file(bucket_name=bucket_name, key=key)

    # print(upload_url_file(bucket_name=bucket_name,
    #                       url="https://pixiv-1304519045.cos.ap-nanjing.myqcloud.com/61782be166c826c8-653ea5468e5789eb-0ea02919c351974.jpg",
    #                       key="0ea02919c351974.jpg"))
    # print(download_file(bucket_name=bucket_name, file_path="img/1620533083236.jpg", save_path="../img/1620533083236.jpg"))
