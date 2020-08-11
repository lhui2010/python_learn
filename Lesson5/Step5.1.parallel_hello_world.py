import os
from multiprocessing import Pool

genblast_cmd_list = ['ping -c 100 www.baidu.com',
                     'ping -c 100 www.sogou.com',
                     'ping -c 100 www.bing.com',
                     'ping -c 100 www.google.com']

threads = 4

with Pool(threads) as p:
    p.map(os.system, genblast_cmd_list)