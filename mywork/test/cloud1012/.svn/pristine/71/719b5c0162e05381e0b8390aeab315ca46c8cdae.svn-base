import os
import logging
import datetime

if not os.path.exists('log'):
    os.makedirs('log')
logfile = 'log/subintaskservice_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d thread:%(thread)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logfile,
                    filemode='w')
