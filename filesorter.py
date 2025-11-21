import os
import shutil

def main():
    location = "C:/Users/Adam/Desktop/Testdateien" #TODO: change to input()

    if not os.path.exists(location):
        print(f"Location does not exist: {location}")
        quit()    

    files = os.listdir(location)
    # filtering only the files
    files = [f for f in files if os.path.isfile(location + "/" + f)]

    file_types = {"IMAGE": ["png", "jpg"],
                "VIDEO": ["mp4"],
                "TEXT": ["txt"],
                "CSV": ["csv"],
                "JSON": ["json"]
                }

    for file in files:
        parts = file.split(".")
        known = False

        if parts[1] in file_types.get("IMAGE"):
            # print(f"{file} -> {parts[1]}")
            if os.path.exists(f"{location}/IMAGES"):
                shutil.move(f"{location}/{file}", f"{location}/IMAGES") 
                print(f"Moved {file} to {location}/IMAGES")
                known = True
            else:
                os.mkdir(f"{location}/IMAGES")
                shutil.move(f"{location}/{file}", f"{location}/IMAGES")
                print(f"Moved {file} to {location}/IMAGES")
                known = True

        if parts[1] in file_types.get("VIDEO"):
            # print(f"{file} -> {parts[1]}")
            if os.path.exists(f"{location}/VIDEOS"):
                shutil.move(f"{location}/{file}", f"{location}/VIDEOS")
                print(f"Moved {file} to {location}/VIDEOS")
                known = True
            else:
                os.mkdir(f"{location}/VIDEOS")
                shutil.move(f"{location}/{file}", f"{location}/VIDEOS")
                print(f"Moved {file} to {location}/VIDEOS")
                known = True

        if parts[1] in file_types.get("TEXT"):
            # print(f"{file} -> {parts[1]}")
            if os.path.exists(f"{location}/TEXT_FILES"):
                shutil.move(f"{location}/{file}", f"{location}/TEXT_FILES")
                print(f"Moved {file} to {location}/TEXT_FILES")
                known = True
            else:
                os.mkdir(f"{location}/TEXT_FILES")
                shutil.move(f"{location}/{file}", f"{location}/TEXT_FILES")
                print(f"Moved {file} to {location}/TEXT_FILES")
                known = True

        if parts[1] in file_types.get("JSON"):
            # print(f"{file} -> {parts[1]}")
            if os.path.exists(f"{location}/JSON_FILES"):
                shutil.move(f"{location}/{file}", f"{location}/JSON_FILES")
                print(f"Moved {file} to {location}/JSON_FILES")
                known = True
            else:
                os.mkdir(f"{location}/JSON_FILES")
                shutil.move(f"{location}/{file}", f"{location}/JSON_FILES")  
                print(f"Moved {file} to {location}/JSON_FILES")
                known = True
                        
        if parts[1] in file_types.get("CSV"):
            # print(f"{file} -> {parts[1]}")
            if os.path.exists(f"{location}/CSV_FILES"):
                shutil.move(f"{location}/{file}", f"{location}/CSV_FILES")
                print(f"Moved {file} to {location}/CSV_FILES")
                known = True
            else:
                os.mkdir(f"{location}/CSV_FILES")
                shutil.move(f"{location}/{file}", f"{location}/CSV_FILES")
                print(f"Moved {file} to {location}/CSV_FILES")
                known = True

        if not known:
            print(f"Unknown '{file}'")


if __name__ == '__main__':
    main()