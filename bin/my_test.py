from __future__ import absolute_import

import os
from got10k.experiments import *

from siamfc import SiamFCTracker

import argparse
if __name__ == '__main__':




    tracker = SiamFCTracker(net_path='/home/airlab/PycharmProjects/pythonProject5/SiamDW-FC/bin/models/siamfcres22_200_16.pth')

    e = ExperimentGOT10k('/home/airlab/PycharmProjects/pythonProject5/data/GOT-10K',subset='test')



    e.run(tracker,visualize=False)#默认不开启可视化
    e.report([tracker.name])
