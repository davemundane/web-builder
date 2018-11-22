import boto3
import json


class Buckets:
    
    def __init__(self,filename):
        with open(filename, "r") as file:
            self.infile = json.loads(file.read())
        self.client = boto3.client("s3")

    def createBucket(self): 
        bucketName = self.infile["Resources"]["ThisIsMyBucket"]["Properties"]["BucketName"]
        response = self.client.create_bucket(Bucket=bucketName)

        print(response)
        return bucketName

    def webHostBucket(self,bucketName):
        webConfig = self.infile["Resources"]["ThisIsMyBucket"]["Properties"]["WebsiteConfiguration"]
        response = self.client.put_bucket_website(Bucket=bucketName, WebsiteConfiguration=webConfig)
        print(response)

create = Buckets("bucket.json")
myname = create.createBucket()
create.webHostBucket(myname)

