import os

# Replace with your actual paths
source_folder = r"C:\Source\FilePath"
destination_folder = r"C:\Destination\FilePath"

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
  if "Participation Certificate" in filename:
    # Construct full paths for source and destination files
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    
    # Move the file
    try:
      os.replace(source_path, destination_path)
      print(f"Moved '{filename}' to destination folder.")
    except Exception as e:
      print(f"Error moving '{filename}': {e}")

print("Done!")
