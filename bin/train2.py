from __future__ import absolute_import #??

import os

from got10k.datasets import *
from siamfc import SiamFCTracker

# import multiprocessing
# multiprocessing.set_start_method('spawn',True)


seqs = GOT10k('/home/airlab/PycharmProjects/pythonProject5/data/GOT-10K', subset='train', return_meta=True)

tracker = SiamFCTracker() #优化器，GPU，损失函数，网络模型

tracker.train_over(seqs)
