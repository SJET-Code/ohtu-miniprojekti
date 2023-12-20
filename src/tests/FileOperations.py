from robot.api.deco import keyword
import os
import time

@keyword("File Should Exist")
def file_should_exist(path):
    return os.path.isfile(path)

@keyword("Wait Until File Exists")
def wait_until_file_exists(path, timeout=3):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if os.path.isfile(path):
            return True
        time.sleep(1)
    return False
