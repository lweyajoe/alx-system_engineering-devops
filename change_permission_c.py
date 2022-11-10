#!/usr/bin/python3

import subprocess
import time
import sys

directory = sys.argv[1]
command = "chmod +x"; check_interval = 5; extensions = ("")

def current_files():
    read = subprocess.check_output(["ls", directory]).decode("utf-8").strip()
    return [item for item in read.split("\n") if item[item.rfind("."):] in extensions]

initial_files = current_files()
for file in initial_files:
    subprocess.call(["/bin/bash", "-c", command+" "+directory+"/"+file])

while True:
    update = current_files()
    for file in update:
        if not file in initial_files:
            subprocess.call(["/bin/bash", "-c", command+" "+directory+"/"+file])  
    initial_files = update
    time.sleep(check_interval)
