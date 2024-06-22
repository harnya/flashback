import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
import boto3
from botocore.client import BaseClient
from fastapi import UploadFile
from starlette.datastructures import UploadFile as StarletteUploadFile
import json 

class S3Media:

    def __init__(self) -> None:
        self.s3_client: BaseClient = boto3.client('s3')
        self.bucket = "memorymainv-339713056590-media"

    def upload_file(self, file: UploadFile) -> str:
        try:
            print("----------->", type(file))
            import base64
            # if isinstance(file, StarletteUploadFile):
            #     contents = file.read()
            # else:
                # In some setups, FastAPI may directly provide bytes, so handle accordingly

            contents = file.file.read()
            image_base64 = base64.b64encode(contents).decode('utf-8')
            try:
                image_data = base64.b64decode(image_base64)
            except Exception as e:
                print("0-------------->", e)
            
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=file.filename,
                Body=image_data,
                ContentType=file.content_type
            )
            return f"https://{self.bucket}.s3.amazonaws.com/memory_files/{file.filename}"

        except Exception as e:
            print("0000000>3", e)
            return "ok"


    # def save_upload_file_tmp(self, file: UploadFile) -> Path:
    #     try:
    #         suffix = Path(file.filename).suffix
    #         tmp_path = Path('/tmp') / f"{file.filename}{suffix}"
    #         with open(tmp_path, 'wb') as tmp:
    #             shutil.copyfileobj(file.file, tmp)
    #         return tmp_path
    #     except Exception as e:
    #         print("Error in save_upload_file_tmp:", e)
    #         raise

    # def upload_file(self, file: UploadFile) -> str:
    #     tmp_path = None
    #     try:
    #         tmp_path = self.save_upload_file_tmp(file)
    #         if not tmp_path or not tmp_path.exists() or tmp_path.stat().st_size == 0:
    #             raise Exception("Temporary file creation failed or file is empty")

    #         print(f"Uploading file from {tmp_path}, size: {tmp_path.stat().st_size} bytes")
            
    #         self.s3_client.upload_file(str(tmp_path), self.bucket, f"memory_files/{file.filename}")
    #     except Exception as e:
    #         print("Error in upload_file:", e)
    #         raise
    #     finally:
    #         if tmp_path and tmp_path.exists():
    #             tmp_path.unlink()
    #     return f"https://{self.bucket}.s3.amazonaws.com/memory_files/{file.filename}"

# Example usage (outside of AWS Lambda)
# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import JSONResponse

# app = FastAPI()

# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     s3_media = S3Media()
#     try:
#         url = s3_media.upload_file(file)
#         return JSONResponse(content={"url": url})
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)
