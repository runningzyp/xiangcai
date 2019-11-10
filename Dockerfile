FROM reg.xiangcaihua.com/python/python:base
ENV DJANGO_SETTINGS_MODULE=config.settings.production
ADD . /app
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r requirements/production.txt
# COPY ./utility/operations.py /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/operations.py
# COPY ./utility/base.py /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/base.py
RUN chmod 777 /app/utility/run.sh
CMD ["sh /app/utility/run.sh"]