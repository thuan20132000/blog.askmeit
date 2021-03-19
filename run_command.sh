#!/bin/bash

source /Users/truongthuan/Develop/python/blog/env/bin/activate

python /Users/truongthuan/Develop/python/blog/manage.py shell -c "from dictionary import search"


# /Users/truongthuan/Develop/python/blog/dictionary/schedule_cron.py