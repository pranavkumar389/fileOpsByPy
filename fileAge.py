import os
import glob
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

files = [f for f in glob.glob(dir_path + "**/*", recursive=True)]

for f in files:
    timeNow = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
    age = timeNow - datetime.fromtimestamp(os.path.getmtime(f))
    print("Age of file " + f + " is " + str(age))
