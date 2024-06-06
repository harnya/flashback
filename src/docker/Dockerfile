
# # 
# FROM python:3.11

# # 
# WORKDIR /src

# # 
# COPY ./requirements.txt /src/requirements.txt

# # 
# RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# # 
# COPY ./app /src/appaa
# COPY ./main.py /src/main.py
# COPY ./web /src/web
# # 
# EXPOSE 8000

# # CMD ["python", "main.py"]
# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["fastapi", "run", "main.py", "--port", "8000"]

FROM public.ecr.aws/lambda/python:3.12
COPY ./ ${LAMBDA_TASK_ROOT}
WORKDIR /src
COPY ./web ./web
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
CMD ["main.handler"]
