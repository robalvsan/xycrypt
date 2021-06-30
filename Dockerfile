ARG VERSION=3.8-slim
FROM python:${VERSION}

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --no-cache-dir

WORKDIR /opt
COPY . .

CMD ["python", "main.py"]