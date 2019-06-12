import os
path = "/home/kriti/Downloads/stanford-dogs-dataset/Annotation"
folders = os.listdir(path)
for folder in folders:
	new_path = path + '/' + str(folder)
	files = os.listdir(new_path)
	for file in files:
		os.rename(os.path.join(new_path,file),os.path.join(new_path,file+'.xml'))
