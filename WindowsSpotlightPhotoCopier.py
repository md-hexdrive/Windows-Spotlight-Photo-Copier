"""
WindowsSpotlightPhotoCopier.py is a Python3 program/script designed to copy all the pictures used by Windows Spotlight,
convert those files into JPG files (by adding the '.jpg' file extension,
and paste them to the user's Desktop in a folder named "Windows Spotlight Photos".

To run it call:

python3 WindowsSpotlightPhotoCopier.py

in the directory this source code file is in.
The above command is included in Windows Batch file for user convenience.
Put a link to the Batch file in the startup folder to cause this program to automatically run this at startup.
"""
import os
import os.path
import fnmatch
import shutil

#import cv2
import setup
import load_config
default_source_dir=os.path.join(os.environ['LOCALAPPDATA'], 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets', '')
default_destination_dir=os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Windows Spotlight Photos', '')

config_options = load_config.import_options("config.json")

if config_options['output_dir'] == "--default":
    destination_dir = default_destination_dir
elif config_options['output_dir'] == "ask":
    destination_dir = setup.ask_for_output_dir()
else:
    destination_dir = config_options['output_dir']

if config_options['input_dir'] == "--default":
    source_dir = default_source_dir
elif config_options['input_dir'] == "ask":
    source_dir = setup.ask_for_input_dir()
else:
    source_dir = config_options['input_dir']





if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

source_file_list = os.listdir(source_dir)
destination_file_list = os.listdir(destination_dir)


#print(os.environ)
#for var in os.environ:
#    print(var)
#    print(os.environ[var])
for file in source_file_list:
    if(os.path.getsize(os.path.join(source_dir,file)) >= 200000):
        shutil.copy2(os.path.join(source_dir, file), os.path.join(destination_dir, file+".jpg"))
    #print(os.path.getsize(os.path.join(source_dir,file)))

