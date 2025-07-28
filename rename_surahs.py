import os

# Set the directory containing the MP3 files
directory = "./"  # Change this to your folder if needed

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        name, ext = os.path.splitext(filename)

        # Remove leading zeros (only from numeric part)
        if name.isdigit():
            new_name = str(int(name)) + ext
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")
