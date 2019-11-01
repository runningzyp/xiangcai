FROM python:alpine
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN ls
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r requirements/production.txt
RUN mv /app/utility/base.py /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/
RUN chmod 777 /app/utility/run.sh
CMD ["/app/utility/run.sh"]