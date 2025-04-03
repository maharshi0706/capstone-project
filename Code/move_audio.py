import os
import shutil

def move_mp4_files(source_folder, destination_folder):
    # Check if destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over all files in the source folder
    for file_name in os.listdir(source_folder):
        # Construct the full file path
        source_file = os.path.join(source_folder, file_name)

        # Check if it's a file and has a .mp4 extension
        if os.path.isfile(source_file) and file_name.endswith('.mp4'):
            # Define the destination file path
            destination_file = os.path.join(destination_folder, file_name)

            try:
                # Move the file
                shutil.move(source_file, destination_file)
                print(f'Moved: {file_name}')
            except Exception as e:
                print(f'Error moving {file_name}: {e}')

# Example usage
source_folder = 'E:/Capstone Project/Code'
destination_folder = 'E:/Capstone Project/audio'

move_mp4_files(source_folder, destination_folder)

# \\\