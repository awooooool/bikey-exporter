import os
import shutil
import re
import configparser

config = configparser.ConfigParser()
config.read('.env')
walk_dir = config['DEFAULT']['ARMA3_WORKSHOP_DIR']

for root, subdirs, files in os.walk(walk_dir):
    if re.search('keys$', root):
        for file in files:
            if re.search('.bikey$', file):
                print("Copying " + file)
                shutil.copyfile(os.path.join(root, file), './keys/' + file)
