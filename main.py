import os

def setup_environment():
    directories = ['data', 'outputs', 'figures']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    print("Data Science Ecosystem Environment is ready.")

if __name__ == "__main__":
    setup_environment()