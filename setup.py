import json
import defaults

def ask_question(question):
    response = input(question)
    print(response)
    if response.strip() == "":
        print("Default")
        response = defaults.default_option
    return response
    
def ask_for_output_dir():
    return ask_question("""What directory do you want to output the photos to?
(leave empty to output to a folder on your desktop) """)

def ask_for_input_dir():
    return ask_question("""Photo Source Directory: """)

def can_create_batch_file():
    create_batch = ask_question("Should I create a batch file to run this program? (Y/N): ")
    can_create_batch = user_confirmed(create_batch)
    
    run_on_startup = ask_question("Should WSPC run on computer Startup? (Y/N): ")
    can_run_on_startup = user_confirmed(run_on_startup)
    
    return can_create_batch, can_run_on_startup


def user_confirmed(response):
    if response.strip().lower() == 'y':
        return True
    else:
        return False
    

if __name__ == '__main__':
    print("\n" + "/" * 70)
    print("""Interactive Setup Program for Windows Spotlight Photo Copier (WSPC)""")
    print("""Answer the questions to configure the program""")
    print("""Leave your responses blank to for the program's default settings""")
    print("""Enter 'ask' to have WSPC ask you for that option each time it runs""")
    print("/" * 70 + "\n")

    properties = {}
    properties['output_dir'] = ask_for_output_dir()
    properties['source_dir'] = ask_for_input_dir()
    
    create_batch, run_at_startup = can_create_batch_file()

    with open("config.json", 'w') as config_file:
        config_file.write(json.dumps(properties, indent=4))
    
    if create_batch:
        with open("WindowsSpotlightPhotoCopier.bat", "w") as batch_file:
            batch_file.write("python WindowsSpotlightPhotoCopier.py")
    
    print("\n\n" + "/" * 70)
    print("Setup Complete, running program for the first time.")
    
    import WindowsSpotlightPhotoCopier
