FROM reg.xiangcaihua.com/python/python:base
ADD . /app
RUN mv utility/base.py /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/base.py
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r requirements/production.txt
RUN chmod 777 /app/utility/run.sh
CMD ["/app/utility/run.sh"]