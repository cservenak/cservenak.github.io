FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 8000

WORKDIR /repo/webes_tananyag/okt-sed-hu

ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
