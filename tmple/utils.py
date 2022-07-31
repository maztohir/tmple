import os
import sys

from pathlib import Path

def read_file(file_path, allow_error=False):
    try:
        with open(file_path, 'r') as myfile:
            return myfile.read()
    except Exception as e:
        if not allow_error:
            print(str(e))
            raise ValueError(f"This following path {file_path} doesn't exist")
        return None


def write_file(file_path, content, allow_error=False, create_if_folder_not_found=False, skip_if_exists=False):
    try:
        if skip_if_exists:
            if Path(file_path).exists():
                print(f'file {file_path} already exists, skipping')
                return False

        if create_if_folder_not_found:
            dir_path = os.path.dirname(file_path)
            Path(dir_path).mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w') as myfile:
            myfile.write(content)
            return True

    except Exception as e:
        print(str(e))
        if not allow_error:
            sys.exit(0)
