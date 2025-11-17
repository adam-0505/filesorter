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

file_types = {"IMAGE": ["png", "jpg"],
              "VIDEO": "video",
              "TEXT": "txt",
              "CSV": "csv",
              "JSON": "json"
              }

for file in files:
    parts = file.split(".")

    if parts[1] in file_types.get("IMAGE"):
        print(f"{file} -> {parts[1]}")
    # if parts[1] == file_types.get("VIDEO"):
    #     print(f"{file} -> {parts[1]}")
    # if parts[1] == file_types.get("TEXT"):
    #     print(f"{file} -> {parts[1]}")
    # if parts[1] == file_types.get("JSON"):
    #     print(f"{file} -> {parts[1]}")
    # if parts[1] == file_types.get("CSV"):
    #     print(f"{file} -> {parts[1]}")