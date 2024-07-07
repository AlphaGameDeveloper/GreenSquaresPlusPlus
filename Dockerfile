FROM python:3.12

WORKDIR /docker

COPY requirements.txt .

RUN pip install -r /docker/requirements.txt

COPY . .

COPY ssh-config /root/.ssh/config

CMD ["bash", "/docker/start.sh"]
