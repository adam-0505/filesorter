import os
import shutil

def move_file(location, file, file_type):

    if os.path.exists(f"{location}/{file_type}"):
        shutil.move(f"{location}/{file}", f"{location}/{file_type}") 
        print(f"Moved {file} to {location}/{file_type}")
    else:                
        os.mkdir(f"{location}/{file_type}")
        shutil.move(f"{location}/{file}", f"{location}/{file_type}")
        print(f"Moved {file} to {location}/{file_type}")


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
        parts = file.rsplit(".", 1)
        known = False

        if len(parts) == 1:
            print("Unknown file type")
            continue

        if parts[1].lower() in file_types.get("IMAGE"):
            # print(f"{file} -> {parts[1]}")
            move_file(location, file, "IMAGES")
            known = True

        if parts[1].lower() in file_types.get("VIDEO"):
            # print(f"{file} -> {parts[1]}")
            move_file(location, file, "VIDEOS")
            known = True

        if parts[1].lower() in file_types.get("TEXT"):
            # print(f"{file} -> {parts[1]}")
            move_file(location, file, "TEXT_FILES")
            known = True

        if parts[1].lower() in file_types.get("JSON"):
            # print(f"{file} -> {parts[1]}")
            move_file(location, file, "JSON_FILES")
            known = True
                        
        if parts[1].lower() in file_types.get("CSV"):
            # print(f"{file} -> {parts[1]}")
            move_file(location, file, "CSV_FILES")
            known = True

        if not known:
            print(f"Unknown '{file}'")


if __name__ == '__main__':
    main()