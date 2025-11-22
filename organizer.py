import os
import shutil

# --- Configuration ---
# The folder path I want to organize.
# NOTE: I should change this path to my own test folder before running.
target_dir = r"C:\Users\MOZAHID HOSSEN\Downloads"

# Defining categories for my files
# I can add more extensions here if I need to.
extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar']
}


def start_cleaning():
    # Check if the directory actually exists
    if not os.path.exists(target_dir):
        print("Error: Folder not found!")
        return

    print(f"Scanning folder: {target_dir} ...")

    # Loop through all items in the directory
    for item in os.listdir(target_dir):

        # Create full path for the item
        item_path = os.path.join(target_dir, item)

        # Use logic only if it is a file (skip folders)
        if os.path.isfile(item_path):

            # Get file extension (e.g., .jpg) and make it lowercase
            # os.path.splitext splits filename and extension
            file_ext = os.path.splitext(item)[1].lower()

            # Flag to check if file is moved
            moved = False

            # Check which category this file belongs to
            for folder_name, ext_list in extensions.items():
                if file_ext in ext_list:

                    # Define the new folder path
                    new_folder_path = os.path.join(target_dir, folder_name)

                    # Create the folder if it doesn't exist
                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)

                    # Move the file
                    # Using shutil to move files safely
                    try:
                        shutil.move(item_path, os.path.join(new_folder_path, item))
                        print(f"Moved: {item} -> {folder_name}")
                        moved = True
                    except Exception as e:
                        print(f"Could not move {item}: {e}")

                    break  # Stop checking other categories if found

            # If file type is not in my list, I can move it to 'Others' (Optional)
            if not moved:
                print(f"Skipped: {item} (Unknown type)")


if __name__ == "__main__":
    start_cleaning()