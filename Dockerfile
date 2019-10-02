FROM reg.xiangcaihua.com/python/python:alpine
ADD . /app
RUN rm -rf /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/base.py
COPY utility/base.py /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r requirements/production.txt
RUN chmod 777 /app/utility/run.sh
CMD ["/app/utility/run.sh"]