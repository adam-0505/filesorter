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
    moved_files = 0
    unknown_files = 0

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
    
    folder_names = {"IMAGE": "IMAGES",
                    "VIDEO": "VIDEOS",
                    "TEXT": "TEXT_FILES",
                    "CSV": "CSV_FILES",
                    "JSON": "JSON_FILES"}

    for file in files:
        parts = file.rsplit(".", 1)
        extension = parts[1].lower()
        known = False

        if len(parts) == 1:
            print("Unknown file type")
            continue

        for category, extensions in file_types.items():
            if extension in extensions:
                folder_name = folder_names[category]
                move_file(location, file, folder_name)
                moved_files += 1
                known = True                
                break

        if not known:
            print(f"Unknown '{file}'")
            unknown_files += 1
        
        print(f"Moved {moved_files} files, {unknown_files} unknown")


if __name__ == '__main__':
    main()