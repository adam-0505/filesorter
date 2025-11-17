import os

location = "C:/Users/Adam/Desktop/Testdateien" #TODO: change to input()

#if os.path.exists(location):
#     os.mkdir(location + "/IMAGES")
#     os.mkdir(location + "/VIDEOS")
#     os.mkdir(location + "/TEXT_FILES")
#     os.mkdir(location + "/JSON_FILES")
#     os.mkdir(location + "/CSV_FILES")
# else:
#     print("That location doesn't exist")

files = os.listdir(location)
# filtering only the files
files = [f for f in files if os.path.isfile(location + "/" + f)]

for file in files:
    parts = file.split(".")

    if parts[1] == "png" or parts[1] == "jpg":
        pass
    if parts[1] == "mp4":
        pass
    if parts[1] == "txt":
        pass
    if parts[1] == "json":
        pass
    if parts[1] == "csv":
        pass