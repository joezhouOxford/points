import sys
def cat(files):
    output=""
    #loop through each file
    for file in files:
        # print file content
        with open(file,'r') as textfile:
            output+=textfile.read()
            textfile.close()
    return output
