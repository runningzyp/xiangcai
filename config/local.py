from .settings import *  # noqa:F403 F401
from .settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["builtins"] += [
    "debugtools.templatetags.debugtools_tags"
]
