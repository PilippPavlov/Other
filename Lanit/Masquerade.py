def ReadData(FilleName='MasqueradeInput.txt'):
    FilleData = open(FilleName,'r').read()
    if len(FilleData) > 1:
        PriceStr,MetersStr = FilleData.split(' ')
        Price = int(PriceStr)
        Meters = int(MetersStr)
    else:
        return None,None
    if (Price >= 1 and Price <= 100) and (Meters >= 1 and Meters <= 100):
        return Price, Meters
    else:
        return None,None

def WriteData(Data,FilleName='MasqueradeOutput.txt'):
    FilleOutput = open(FilleName,'w')
    if Data != None:
        FilleOutput.write(str(Data))
    else:
        FilleOutput.write('Error!')
    FilleOutput.close()      

def CalculatorPrice(Price,Meters):
    if Price != None and Meters != None:
        return Price*Meters
    else:
        return None

if __name__ == '__main__':
    price, meters = ReadData()
    fullPrice = CalculatorPrice(price,meters)
    WriteData(fullPrice)

    