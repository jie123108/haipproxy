
python3.6 crawler_booter.py --usage crawler common ajax
python3.6 crawler_booter.py --usage validator init douban

python3.6 scheduler_booter.py --usage crawler common ajax
python3.6 scheduler_booter.py --usage validator init douban

# 修改后, 简化启动了.
python3.6 booter.py --usage crawler common ajax
python3.6 booter.py --usage validator init douban

python3.6 squid_update.py