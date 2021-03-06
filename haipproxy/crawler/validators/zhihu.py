# coding=utf8
"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from haipproxy.config.settings import (QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class ZhiHuValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of zhihu proxy resources"""
    name = 'zhihu'
    urls = [
        'https://www.zhihu.com/question/47464143'
    ]
    task_queue = QUEUE('temp', name)
    score_queue =  QUEUE('validated', name)
    ttl_queue = QUEUE('ttl', name)
    speed_queue = QUEUE('speed', name)
    success_key = '安全验证'
