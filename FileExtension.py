#Program to accept filename from the user and print extension of that file


def FileExt(filename):
    global ext
    ext = filename.split(".")
    return ext[-1]

filename = input("Input the filename")
print("Extension of the filename is ", FileExt(filename))