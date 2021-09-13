from zipfile import ZipFile, os 
os.chdir(r'C:')
exampleZip= ZipFile('example.zip')
exampleZip.namelist()


