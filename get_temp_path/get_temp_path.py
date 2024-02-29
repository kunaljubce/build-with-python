# python3 get_temp_path.py
# Program to create a temp dir with auto-assigned name, return the dir name, and clean it

import tempfile
import shutil
from pathlib import Path

##########################
####    APPROACH 1    ####
##########################
def temp_path_provider(func):
    print("OUTPUT OF APPROACH 1: ")
    temp_path = Path(tempfile.mkdtemp())
    result = func(temp_path)
    shutil.rmtree(temp_path)
    return result

def some_func(temp_path):
    print(f"I was provided with {temp_path}")
    assert temp_path.exists()
    return temp_path

temp_path = temp_path_provider(some_func)
print(temp_path)
print(temp_path.exists())

##########################
####    APPROACH 2    ####
##########################
def temp_path_provider_with_ctx_manager(func):
    print("OUTPUT OF APPROACH 2: ")
    with tempfile.TemporaryDirectory() as temp_path:
        return func(Path(temp_path))
    
temp_path = temp_path_provider_with_ctx_manager(some_func)
print(temp_path)
print(temp_path.exists())

##########################
####    APPROACH 3    ####
##########################
