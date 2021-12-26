from __future__ import print_function
import cv2
from bak.cache import Metric_Cache#, Grid_Cache
import bak.fastmatch as fastmatch
import figures
import cProfile

# Open images and create cache
target_path = "C:/Data/Datasets/UW_matching/000224_224_left.jpg"
query_path = "C:/Data/Datasets/UW_matching/000230_230_left.jpg"
query_cache = Metric_Cache(query_path)
target_img = cv2.imread(target_path)
query_img = cv2.imread(query_path)

# Match using Fast-Match with a ratio threshold of 0.7
log = []
match_fun = fastmatch.match(query_cache, target_img, options = {'log' : log})
from time import time
t1 = time()
matches = list(match_fun(0.7, 1))
t2 = time()
print("Total time:", t2 - t2, "secs.")
# Visualize results
# The [:,:,::-1] inverses the color channels so the images are printed correctly
figures.visualize_log(log, query_img[:,:,::-1], target_img[:,:,::-1], stop_at = None) # stop_at = 100


