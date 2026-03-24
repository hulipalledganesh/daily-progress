import datetime

with open("progress.txt","a") as f:
    f.write("Cybersecurity learning " + str(datetime.date.today()) + "\n")