from Masquerade import ReadData,WriteData

def PartyCook(Aborigine,NumCookChildren):
    if Aborigine != None and NumCookChildren != None:
        if NumCookChildren % Aborigine == 0:
            return 'Party is coming'
        else:
            return 'It is a boring day'
    else:
        return 'Error!'
        
if __name__ == '__main__':
    aborigine, numcookchildren = ReadData('ConundrumInput.txt')
    result = PartyCook(aborigine,numcookchildren)
    WriteData(result,'ConundrumOutput.txt')