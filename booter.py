"""
This module is used to start multi spiders or validators from IDE or cmd.

All the startup args can be found in config/rules.py, including:
CRAWLER_TASK_MAPS, VALIDATOR_TASK_MAPS

You can start proxy spiders using the following cmd:
python booter.py --usage crawler

If you want to start only common spider and ajax proxy spider, run:
python booter.py --usage crawler common ajax

If you want to start all the validators, run:
python booter.py --usage validator

If you just want to start init and https validator, run:
python booter.py --usage validator init https
"""
from haipproxy.scheduler import crawler_start, scheduler_start
import threading

    

if __name__ == '__main__':
    thread = threading.Thread(target=scheduler_start)
    thread.start()
    crawler_start()
