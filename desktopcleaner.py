import os
import shutil

def create_subfolder(folder_path, subfolder_name):
    # Makes path to check for Subfolder ie. Users/danielgekonde/DEsktop/JPG\ Files
    subfolder_path = os.path.join(folder_path, subfolder_name)

    # Checks if Subfolder already exists and makes one if not
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(folder_path):

    # Searches through each file in directory
    for filename in os.listdir(folder_path): 

        # Finds file and grabs its extension (pdf, jpg, docx)
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split(".")[-1].lower()

            # Creates subfolder for files (PDF Files, JPG Files)
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files" 
                subfolder_path = create_subfolder(folder_path,subfolder_name)
                file_path = os.path.join(folder_path, filename)

                # Creates new path for current file to check if it has already moved
                new_location_path = os.path.join(subfolder_path,filename)
                
                # Moves file to Subfolder if it's not already there
                if not os.path.exists(new_location_path):
                    shutil.move(file_path,subfolder_path)
                    print(f"Moved {filename} -> {subfolder_name}")
                else:
                    print(f"Skipped: {filename} already exists in {subfolder_name}")
                
if __name__ == "__main__":
    print('Desktop Cleaner Script')
    folder_path = '/Users/danielgekonde/Desktop'
    if os.path.isdir(folder_path): #Checks if directory exists
        clean_folder(folder_path)
        print("Cleaning Complete")
    else:
        print('Invalid folder path. Please try again.')