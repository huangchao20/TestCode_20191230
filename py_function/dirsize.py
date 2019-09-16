import os

file_size = 0
def getFileSize( ppath ):
    global file_size
    for p in os.listdir(os.path.abspath(ppath)):
        npath = os.path.join(ppath, p)
        if os.path.isfile( npath ):
            file_size += os.path.getsize(npath)
        else:
            try:
                getFileSize( npath )
            except RecursionError:
                print( "递归超界" )
    return file_size

if __name__ =="__main__":
    ppath = "G:\黄大宝python"
    dsize = getFileSize( ppath )
    print(dsize)
