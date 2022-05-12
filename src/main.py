#! /usr/bin/python3.9
from .constant import GLOBS
import glob
import os
from tqdm import tqdm
from itertools import chain
import shutil
import subprocess


print(f"WORKING IN {os.getcwd()}")


if __name__ == '__main__':
    iters = [glob.glob(g) for g in GLOBS]   
    for f in tqdm(chain(*iters)):
        if os.path.isfile(f):  
            os.remove(f)
        else:
            shutil.rmtree(f)






