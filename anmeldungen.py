import os

destFile="anmeldungen.csv"

lines=[]
files=os.listdir("./")
for f in files:
    if os.path.isfile(f) and f.endswith(".csv") and not f ==destFile :
        #print (f + " ist eine CSV-Datei")
        with open(f) as fp:
            for line in fp:
                lines.append(line)

with open(destFile,"w+") as dest:
    dest.write("sep=,\n")
    for l in lines:
        fields=l.split(",")

        if fields[2].replace("\"","").isnumeric():
            dest.write(l+"\n")
        else:
            fields.insert(2,"na")
            dest.write(",".join(fields))
