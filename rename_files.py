import os

def rename_file():
    file_list = os.listdir("/Users/andretonelli/projects/fullstackUdacity/python/prank")
    # get files name for folder
    print (file_list)
    os.chdir("/Users/andretonelli/projects/fullstackUdacity/python/prank")
    # for each one rename it
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
rename_file()
