import os,shutil
dir = "H:/11785project/data/trainA"
i = 0
for files in os.listdir(dir):
    if i <= 10000:
        shutil.copy(dir + '/' + files,r'H:/11785project/data/subtrain')
        i += 1