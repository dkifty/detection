#!/usr/bin/env python

import os
import sys

os.chdir('setup')

install_env = 'pip install -qr requirements.txt'
os.system(install_env)

install_torch = 'pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113'
os.system(install_torch)

install_ultralytics = 'pip install ultralytics'
os.system(install_ultralytics)

os.chdir('./..')
