from datetime import datetime

with open("progress.txt", "a") as f:
    f.write("Update: " + str(datetime.now()) + "\n")