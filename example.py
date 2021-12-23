from __future__ import print_function
import cv2
from bak.cache import Metric_Cache#, Grid_Cache
import bak.fastmatch as fastmatch
import figures


# Open images and create cache
target_path = "images/graf/img1.ppm"
query_path = "images/graf/img4.ppm"
query_cache = Metric_Cache(query_path)
target_img = cv2.imread(target_path)
query_img = cv2.imread(query_path)

# Match using Fast-Match with a ratio threshold of 0.7
log = []
match_fun = fastmatch.match(query_cache, target_img, options = {'log' : log})
matches = list(match_fun(0.7))

# Visualize results
# The [:,:,::-1] inverses the color channels so the images are printed correctly
figures.visualize_log(log, query_img[:,:,::-1], target_img[:,:,::-1], stop_at = None) # stop_at = 100


