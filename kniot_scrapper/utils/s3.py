import boto3


class S3:

    @staticmethod
    def upload(file_source, file_destination):

        s3 = boto3.client('s3')

        s3.upload_file(file_source, 'kniot-scrapper', file_destination, ExtraArgs={'ACL':'public-read'})