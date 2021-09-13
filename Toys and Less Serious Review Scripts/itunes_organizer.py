#! python3

# itunes_organizer.py - do something to send all purchased Itunes songs to a different folder or something


import os

music_path = r'C:\Users\rick_\Music\iTunes\iTunes Media\Music'

itunes_songs = []


for folder_name, subfolders, filenames in os.walk(music_path):
	print("\nThe current folder is " + os.path.basename(folder_name), end= '\n')

	for subfolder in subfolders:
		print("SUBFOLDER of " + os.path.basename(folder_name) + ": " + os.path.basename(subfolder))

	for file in filenames:
		if file.endswith(".m4p"):
			itunes_songs.append(str(file))