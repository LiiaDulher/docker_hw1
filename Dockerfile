FROM python:3.8-slim

COPY ./introduce_me.py /opt/app/

RUN pip install pytz

ENTRYPOINT ["python", "/opt/app/introduce_me.py"]
