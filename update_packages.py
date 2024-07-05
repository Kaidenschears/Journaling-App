import subprocess
import re
# Use this script to easily update python packages

def check_and_update_packages():
    # Check for outdated packages
    result = subprocess.run(['pip', 'list', '--outdated'], stdout=subprocess.PIPE, text=True)
    outdated_packages = result.stdout.splitlines()
    
    # Skip the first two lines of the pip list output
    outdated_packages = outdated_packages[2:]

    if not outdated_packages:
        print("All packages are up-to-date.")
        return

    # Update each outdated package
    for package in outdated_packages:
        match = re.match(r'^(\S+)', package)
        if match:
            package_name = match.group(1)
            print(f"Updating {package_name}...")
            subprocess.run(['pip', 'install', '--upgrade', package_name])

if __name__ == "__main__":
    check_and_update_packages()