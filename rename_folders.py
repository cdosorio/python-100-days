import os

directory = os.getcwd()

""" fullpaths = [x[0] for x in os.walk(directory)]
for f in fullpaths:
    foldername = os.path.basename(f)
    
    newname = foldername.replace(" ", "-")
    print(f"{foldername} to {newname}")
    #os.rename(foldername, newname) """

dirlist = [ item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item)) ]
for foldername in dirlist: 
    if "git" in foldername:
        continue
    newname = foldername.replace("_", "-")
    #print(f"{foldername} to {newname}")
    os.rename(foldername, newname)
