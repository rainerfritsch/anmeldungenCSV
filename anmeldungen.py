import os
from exchangelib import *
# from sqlalchemy import create_engine
# from sqlalchemy.orm import *

# SUPPLY REGISTRATION INFORMATION FOR EXCHANGE SERVER
credentials = Credentials("")
account = Account("", credentials=credentials, autodiscover=True)

# determine db / sheet for registrations (BUILD IN POSTGRES?)
destFile = "anmeldungen.csv"

# determine path in which the csv files are located
path = "./"

# CREATE CLASS FOR STUDENTS

# SET UP DB FOR REGISTRANTS

# pick original reg csvs, read original and add to list
lines = []
files = os.listdir(path)
for f in files:
    if os.path.isfile(f) and f.endswith(".csv") and not f == destFile:
        #print (f + " ist eine CSV-Datei")
        with open(f) as fp:  # what is fp?
            for line in fp:
                lines.append(line.strip())

# TRANSFORM ENTRIES TO STUDENT CLASS

# add elements from list to destination file (BUILD IN POSTGRES?)
with open(destFile, "w+") as dest:
    # dest.write("sep=,\n") | what was that for?
    for l in lines:
        fields = l.split(",")

        # replace missing student ids with n.a.
        if fields[2].replace("\"", "").isnumeric():
            dest.write(l+"\n")
        else:
            fields.insert(2, "na")
            dest.write(",".join(fields))

# WRITE CLASS ELEMENTS TO DB
