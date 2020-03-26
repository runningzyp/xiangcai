import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING = {
    "version": 1,  # 保留字
    "disable_existing_loggers": False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    "formatters": {
        # 详细的日志格式
        "standard": {
            "format": "[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]"  # noqa:E501
            "[%(levelname)s][%(message)s]"
        },
        # 简单的日志格式
        "simple": {
            "format": "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s"  # noqa:E501
        },
        # 定义一个特殊的日志格式
        "collect": {"format": "%(message)s"},
    },
    # 过滤器
    "filters": {
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}
    },
    # 处理器
    "handlers": {
        "console": {  # 在终端打印
            "level": "DEBUG",
            "filters": ["require_debug_true"],  # 只有在Django debug为True时才在屏幕打印日志
            "class": "logging.StreamHandler",  #
            "formatter": "simple",
        },
        "default": {  # 默认的
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",  # 保存到文件，自动切
            "filename": os.path.join(BASE_DIR + "/logs/", "all.log"),  # 日志文件
            "maxBytes": 1024 * 1024 * 50,  # 日志大小 50M
            "backupCount": 3,  # 最多备份几个
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "error": {  # 专门用来记错误日志
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",  # 保存到文件，自动切
            "filename": os.path.join(BASE_DIR + "/logs/", "error.log"),  # 日志文件
            "maxBytes": 1024 * 1024 * 50,  # 日志大小 50M
            "backupCount": 5,
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "api": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR + "/logs/", "api.log"),
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "standard",
        },
    },
    "loggers": {
        "default": {  # 默认的logger应用如下配置
            "handlers": ["default", "console", "error"],  # 上线之后可以把'console'移除
            "level": "DEBUG",
            "propagate": True,  # 向不向更高级别的logger传递
        },
        "api": {  # 名为 'collect'的logger还单独处理
            "handlers": ["api"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
