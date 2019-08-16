import os
import sys
from datetime import datetime

noOfFilesToCreate = int(sys.argv[1]) if len(sys.argv) > 1 else 1
fileSize = 1024*1024 # 1MB

for x in range(noOfFilesToCreate):
  fileName = str(datetime.timestamp(datetime.utcnow())) + "_" + str(x)
  with open(fileName, 'wb') as myFile: #wb for binary write
    myFile.write(os.urandom(fileSize))
