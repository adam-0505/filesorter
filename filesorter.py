import os

location = "C:/Users/Adam/Desktop/Testdateie" #TODO: change to input()

if not os.path.exists(location):
    print("Location does not exist")
    quit()
    

files = os.listdir(location)
# filtering only the files
files = [f for f in files if os.path.isfile(location + "/" + f)]

file_types = {"IMAGE": ["png", "jpg"],
              "VIDEO": ["video"],
              "TEXT": ["txt"],
              "CSV": ["csv"],
              "JSON": ["json"]
              }

for file in files:
    parts = file.split(".")

    if parts[1] in file_types.get("IMAGE"):
        # print(f"{file} -> {parts[1]}")
        if os.path.exists(location + "/IMAGES"):
            # move file into folder
            pass        
        else:
            os.mkdir(location + "/IMAGES")
            # move file into new folder

    if parts[1] in file_types.get("VIDEO"):
        # print(f"{file} -> {parts[1]}")
        if os.path.exists(location + "/VIDEOS"):
            # move file into folder
            pass
        else:
            os.mkdir(location + "/VIDEOS")
            # move file into new folder

    if parts[1] in file_types.get("TEXT"):
        # print(f"{file} -> {parts[1]}")
        if os.path.exists(location + "/TEXT_FILES"):
            # move file into folder
            pass
        else:
            os.mkdir(location + "/TEXT_FILES")
            # move file into new folder

    if parts[1] in file_types.get("JSON"):
        # print(f"{file} -> {parts[1]}")
        if os.path.exists(location + "/JSON_FILES"):
            # move file into folder
            pass
        else:
            os.mkdir(location + "/JSON_FILES")
            # move file into new folder  
                      
    if parts[1] in file_types.get("CSV"):
        # print(f"{file} -> {parts[1]}")
        if os.path.exists(location + "/CSV_FILES"):
            # move file into folder
            pass
        else:
            os.mkdir(location + "/CSV_FILES")
            # move file into new folder