import os
import shutil

def organize_files(folder_path):
    # Dictionary to store file extensions and their corresponding folder names
    extensions = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Music': ['.mp3', '.wav', '.flac', '.aac']
        # Add more categories and corresponding extensions as you need
    }

    # Create folders for each category if they don't already exist
    for folder_name in extensions.keys():
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Move files into corresponding folders based on their extensions
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            for folder_name, extension_list in extensions.items():
                for extension in extension_list:
                    if file_name.endswith(extension):
                        src = os.path.join(folder_path, file_name)
                        dst = os.path.join(folder_path, folder_name, file_name)
                        shutil.move(src, dst)
                        print(f"Moved {file_name} to {folder_name} folder.")
                        break

if __name__ == "__main__":
    folder_path = input("Enter the path of the directory to organize: ")
    organize_files(folder_path)
