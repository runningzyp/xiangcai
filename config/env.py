import json
import os
from . import server
import pymysql

REDIS_HOST = server.env("REDIS_HOST") or "redis://localhost/5"

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": REDIS_HOST,
#         "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
#     }
# }

DATABASES = {
    "default": server.env.db()
    or {
        "ENGINE": "django.db.backends.mysql",  # 选择mysql引擎
        "NAME": "xiangcai",  # 数据库名
        "USER": "xiangcai",  # 用户
        "PASSWORD": "xiangcai",  # 密码
        "HOST": "xiangcai",  # 连接IP地址，默认本地
        "PORT": "3306",  # 端口，默认3306
    }
}
print()


pymysql.install_as_MySQLdb()


try:
    sz = os.get_terminal_size()
except Exception:
    pass
else:
    height = sz.lines
    txt = [x for x in json.dumps(DATABASES["default"], indent=1).split("\n")]
    screen_width = sz.columns
    txt_width = 50
    box_width = 3
    left_margin = (screen_width - txt_width) // 2

    print()
    print(" " * left_margin + "+" + "-" * (txt_width) + "+")
    print(" " * left_margin + "|" + " " * (txt_width) + "|")
    for t in txt:
        print(
            " " * left_margin + "|" + " " * (box_width) + t + " " * (box_width)
        )  # noqa E501
    print(" " * left_margin + "|" + " " * (txt_width) + "|")  # noqa E501
    print(" " * left_margin + "+" + "-" * (txt_width) + "+")
    print()
