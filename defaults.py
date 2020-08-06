import os

default_source_dir=os.path.join(os.environ['LOCALAPPDATA'], 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets', '')
default_destination_dir=os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Windows Spotlight Photos', '')

default_option = "--default"


def is_default_option(option):
    if option == default_option:
        return True
    else:
        return False