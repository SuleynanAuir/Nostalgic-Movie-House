import os
#create folders
folders1 = "train path"
folders2 = "image path"
os.makedirs(folders1,exist_ok=True)
os.makedirs(folders2,exist_ok=True)

#get path
def getpath(folderpath):
    file_paths=[]
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

trainpath = getpath(folders1)
tpath = trainpath[0]
imagepath = getpath(folders2)
ipath = imagepath[0]