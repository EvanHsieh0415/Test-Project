import time

string = r"-\|/"
n = 0

for i in range(25):
    for i in string:
        print(f"{i}\b", end="", flush=True)
        time.sleep(0.15)