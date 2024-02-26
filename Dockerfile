FROM python:3.8-slim-buster

RUN mkdir /app

COPY ./*.txt ./*.py ./*.sh ./*.onnx /app/


RUN cd /app \
    && mkdir logs \
    && python3 -m pip install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf /tmp/* && rm -rf /root/.cache/* \
    && sed -i 's#http://deb.debian.org#http://mirrors.aliyun.com/#g' /etc/apt/sources.list\
    && apt-get --allow-releaseinfo-change update && apt install libgl1-mesa-glx libglib2.0-0 -y

WORKDIR /app

CMD ["gunicorn", "-c", "gunicorn.py" , "server:app"]
