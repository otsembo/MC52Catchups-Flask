
def readFile(handle):
    #  actual data
    data = handle.read()
    print(data)

    #  close file stream
    handle.close()



#  Read a single line
def readSingleLine(handle):
    # actual data
    data = handle.readline()

    print(data)

    #  close file stream
    handle.close()

if __name__ == '__main__':
    #  create file object by reading file
    handle = open("test.txt", "r")

    # option of choice
    readFile(handle)
    
