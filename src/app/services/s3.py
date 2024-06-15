import os
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from boto3 import client
from botocore.client import BaseClient
from fastapi import UploadFile


class S3Media:

    def __init__(self) -> None:
        self.s3_client: BaseClient = client('s3')
        self.bucket = "memorymain-339713056590-media"

    def save_upload_file_tmp(self, file: UploadFile):
        try:
            suffix = Path(str(file.filename)).suffix
            with NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
                shutil.copyfileobj(file.file, tmp)
                tmp_path = Path(tmp.name)
        except Exception as e:
            print("error", e)
        finally:
            file.file.close()
        return tmp_path
    
    def upload_file(self, file: UploadFile) :
        try:
            tmp_path = self.save_upload_file_tmp(file)
            self.s3_client.upload_file(tmp_path, self.bucket, f"memory_files/{file.filename}")
        except Exception as e:
            print("---------------->", e)
        finally:
            tmp_path.unlink()
        return f"https://{self.bucket}.s3.amazonaws.com/memory_files/{file.filename}"
        
        





