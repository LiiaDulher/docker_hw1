FROM python:3.8-slim

COPY ./introduce_me.py /opt/app/

ENTRYPOINT ["python", "/opt/app/introduce_me.py"]
