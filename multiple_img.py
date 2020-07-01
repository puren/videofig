#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 bily     Huazhong University of Science and Technology
#
# Distributed under terms of the MIT license.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

import cv2 as cv
from matplotlib.pyplot import Rectangle

from videofig import videofig

 
import matplotlib

import sys
import glob

path_data=sys.argv[1]

path_list = sorted(glob.glob(path_data+'/test_rgb_*.png'))

NUM_IMAGES = len(path_list)
PLAY_FPS = 100  # set a large FPS (e.g. 100) to test the fastest speed our script can achieve
SAVE_PLOTS = False  # whether to save the plots in a directory



# Preload images and boxes
imgs, boxs = [], []
for idx in path_list:
    img = cv.imread(idx)
    #img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgs.append(img)


def redraw_fn(f, ax):
    img = imgs[f]
   
    if not redraw_fn.initialized:
        redraw_fn.img_handle = ax.imshow(img)
        redraw_fn.last_time = time.time()
        redraw_fn.text_handle = ax.text(0., 1 - 0.05,
                                        'Resolution {}x{}, FPS: {:.2f}'.format(img.shape[1], img.shape[0], 0),
                                        transform=ax.transAxes,
                                        color='yellow', size=12)
        redraw_fn.initialized = True
    else:
        redraw_fn.img_handle.set_array(img)
        current_time = time.time()
        redraw_fn.text_handle.set_text('Resolution {}x{}, FPS: {:.2f}'.format(img.shape[1], img.shape[0],
                                                                              1 / (current_time - redraw_fn.last_time)))
        redraw_fn.last_time = current_time


redraw_fn.initialized = False

if not SAVE_PLOTS:
    videofig(NUM_IMAGES, redraw_fn, play_fps=PLAY_FPS)
else:
    videofig(NUM_IMAGES, redraw_fn, play_fps=PLAY_FPS, save_dir='example2_save')
