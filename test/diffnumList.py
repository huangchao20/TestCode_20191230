pplist = []
def getList( plist ):
    p = []
    print( plist )
    for a in plist:
        for b in plist:
            if b != a:
                for c in plist:
                    if a != c and b != c:
                        p.append( (a, b, c) )
                        pplist.append( p )
    print(len(pplist))
    return pplist

if __name__ == "__main__":
    plist = [2, 3, 4, 5]
    pplist = getList(plist)
    print(pplist)
