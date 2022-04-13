FROM centos:7

LABEL Maintainer="GithubArchitect"

RUN yum update -y

RUN yum install python3-pip -y

RUN pip3 install --upgrade pip

RUN mkdir -v /app

WORKDIR /app

COPY app.py .

COPY requirements.txt .

COPY start.sh .

RUN pip3 install -r requirements.txt

EXPOSE 5000-5099

ENTRYPOINT ["/bin/bash", "start.sh"]