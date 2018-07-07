# coding=utf8

"""
We use this validator to filter ip that can access mobile weibo website.
"""
from haipproxy.config.settings import (QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class WeiBoValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of weibo proxy resources"""
    name = 'weibo'
    urls = [
        'https://weibo.cn/'
    ]
    task_queue = QUEUE('temp', name)
    score_queue =  QUEUE('validated', name)
    ttl_queue = QUEUE('ttl', name)
    speed_queue = QUEUE('speed', name)
    success_key = '微博广场'
