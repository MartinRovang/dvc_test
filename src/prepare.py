import nibabel as nib
import yaml
import sys
import random
import os

datapath = sys.argv[1]
params = yaml.safe_load(open("params.yaml"))["prepare"]
split = params["split"]
random.seed(params["seed"])
os.mkdir('data')
os.mkdir('data/prepared')