import re, os, glob

pathForConfig = input('Enter absolute path for Files: ')
os.chdir(pathForConfig)
filesList = glob.glob("*.txt")
userSearch = input('Enter the regex expression')
userSearchRegex = re.compile(userSearch)
noMatch=1
for files in filesList:
    file1 = open(files)
    match = userSearchRegex.findall(file1.read()) 
    if match:
        for item in match:
            print(item + " match in: " + str(files)) 
        noMatch=0
if noMatch:
    print('No match found')