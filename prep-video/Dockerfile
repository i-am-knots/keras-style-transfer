FROM python:3.8.5-slim-buster

COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r /requirements.txt

CMD [ "python", "./prep.py" ] 
