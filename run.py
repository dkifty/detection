#!/usr/bin/env python

import os
import glob
import subprocess

def select_last_img(formats='jpg'):
	images = glob.glob(os.path.join(os.getcwd(), 'images/*.'+formats))
	images.sort()
	last_image = images[-1]
	
	with open('./yolov5/detect.py', 'r') as detect_py:
		detect_py_line = detect_py.readlines()
	
	detect_py_line[23] = "        source=ROOT / "+f"'{last_image}'"+", # file/dir/URL/glob/screen/0(webcam)\n"
	detect_py_line[50] = "    source = "+f"'{last_image}'"+"\n"
	detect_py_line[140] = "    parser.add_argument('--source', type=str, default=ROOT / "+f"'{last_image}'"+", help='file/dir/URL/glob/screen/0(webcam)')\n"
	
	with open('./yolov5/detect.py', 'w') as f:
		for line in detect_py_line:
			f.write(line)
select_last_img()
os.chdir('./yolov5')
os.system('python detect.py')

os.chdir('./..')
