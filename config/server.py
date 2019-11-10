# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import environ

env = environ.Env()
env.read_env()


def elist(key, default=None):
    return env(key) and env.list(key) or (default or [])


def ejson(key, default=None):
    return env(key) and env.json(key) or (default or {})
