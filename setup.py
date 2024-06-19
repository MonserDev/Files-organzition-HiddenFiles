import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Successfully installed packages from requirements.txt")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages. Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    install_requirements()