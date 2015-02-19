__author__ = 'theopavlakou'

#Parses data file.
import os
# directory_name = "bla"app.config['DATA_FILES']
directory_name= "/data/"

def parse(file_name):
    tweets={}
    tweets["-1"] =[]
    tweets["1"] =[]
    current_path = os.path.dirname(os.path.realpath(__file__)) + directory_name
    path=os.path.join(current_path, file_name)
    # path = file_name

    print(path)
    if not os.path.isfile(path):
        print("  Path does not exists: {0}".format(path))
        return {}
    f=open(path, "r")
    for line in f.readlines():
        line=line.strip()
        if len(line)==0:
            continue
        line=line.split("\t")
        print(line)
        print(line[2])
        tweet={"latitude":line[2],
               "longitude":line[1]}
        print("here")
        tweets[line[0]].append(tweet)
    f.close()
    return tweets

