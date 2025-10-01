import os

folder_original = '/Users/deepu.mukundan/Desktop'
folder_destination = '/Users/deepu.mukundan/Desktop/Cleanup'
os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    if os.path.isfile(entry):
        location_original = os.path.join(folder_original, entry.name)
        location_final = os.path.join(folder_destination, entry.name)
        os.rename(location_original, location_final)
