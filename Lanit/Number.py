def ReadData(FilleName='NumberInput.txt'):
    FilleData = open(FilleName,'r').read()
    if len(FilleData) <= 1:
        return None,None
    FerstStr,SecondStr = FilleData.split('\n')
    SequenceStr = SecondStr.split(' ')
    Number = int(FerstStr)
    Sequence = [int(item) for item in SequenceStr]
    for item in Sequence:
        if item < 1 or item > 10**9:
            return None,None
    if Number >= 1 and Number <= 1000:
        return Number, Sequence
    else:
        return None,None

        
def WriteData(SourceSequence,FilleName='NumberOutput.txt'):
    FilleOut = open(FilleName,'w')
    if SourceSequence != [] and SourceSequence != None:
        DataStr = ''
        for item in SourceSequence:
            DataStr += str(item) + ' ' 
        FilleOut.write(DataStr)
    else:
        FilleOut.write('Error!')
    FilleOut.close()

def FindSequence(ConvertedSequence, Number):
    if ConvertedSequence != None and Number != 0:
        ConvertedSequence.sort()
        SourceSequence = [ConvertedSequence[index] - ConvertedSequence[index - 1] for index in range(Number) if index != 0]
        SourceSequence.insert(0,ConvertedSequence[0])
        return SourceSequence
    else:
        return None
if __name__ == '__main__':
    number, sequence = ReadData()
    source = FindSequence(sequence, number)
    WriteData(source)
