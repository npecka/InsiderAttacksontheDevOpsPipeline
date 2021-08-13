FROM python:3.8-slim
MAINTAINER Nicholas Pecka "npecka107@gmail.com"
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
CMD [ "python", "./f_pc.py"]