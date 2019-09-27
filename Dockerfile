FROM reg.xiangcaihua.com/base/django
ADD . /app
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r /requirements/production.txt
CMD ["/app/utility/run.sh"]