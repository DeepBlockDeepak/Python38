#! python3
#backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments

import zipfile,os

def backupToZip(folder, backup_location = 'C:\python_backup'):
	# Backup the entire contents of "folder" into a ZIP file.

	folder = os.path.abspath(folder)
	
	number = 1 #'number' used to create the name for the zip folders
	
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

		if not os.path.exists(os.path.join(backup_location, zipFilename)): #does the .exists() method require a full filepath? 
			break
		number += 1

	
	zip_folder = zipfile.ZipFile(os.path.join(backup_location, zipFilename), 'w')

	for folderName, subfolders, filenames in os.walk(folder):#returns, string of the basename of 'folder', a list of strings of subfolders, and a list of files in 'folder'
		
		#print (folderName, "======= THE FOLDERNAME")
		zip_folder.write(folderName)
		
		for filename in filenames:
			#print (os.path.join(folderName, filename), " = === filename full path")
			newBase = os.path.basename(folder) + '_'
			
			if filename.startswith(newBase) and filename.endswith('.zip'):
				continue
			
			zip_folder.write(os.path.join(folderName,filename))#Joining folderName to filename!!!!!!!!! Allows correct file paths
	zip_folder.close()

backupToZip(r'C:\Python38\Scripts\python38_practice')

