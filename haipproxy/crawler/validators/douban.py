# coding=utf8
"""
We use this validator to filter ip that can access mobile zhihu website.
"""
from haipproxy.config.settings import (QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class DoubanValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of douban proxy resources"""
    name = 'douban'
    urls = [
        'https://movie.douban.com/subject/26752088/'
    ]
    task_queue = QUEUE('temp', name)
    score_queue =  QUEUE('validated', name)
    ttl_queue = QUEUE('ttl', name)
    speed_queue = QUEUE('speed', name)
    success_key = '我不是药神'
