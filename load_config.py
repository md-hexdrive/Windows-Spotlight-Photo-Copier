import os
import json
from defaults import *


def import_options(config_file):
    if os.path.exists(config_file):
        with open(config_file, "r") as config_file:
            config_options = json.loads(config_file.read())
            #print(config_options)
            #print(config_options['output_dir'])
            output_dir = config_options['output_dir']
            source_dir = config_options['source_dir']
            
            if is_default_option(output_dir):
                output_dir = default_destination_dir
            if is_default_option(source_dir):
                source_dir = default_source_dir
            return source_dir, output_dir
    else:
        print("Configuration file doesn't exist, using default options instead\n")
        return default_source_dir, default_destination_dir
    

if __name__ == "__main__":
    print(import_options("config.json"))