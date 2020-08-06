import json

def import_options(config_file):
    with open(config_file, "r") as config_file:
        config_options = json.loads(config_file.read())
        #print(config_options)
        #print(config_options['output_dir'])
        
        return config_options

if __name__ == "__main__":
    print(import_options("config.json"))