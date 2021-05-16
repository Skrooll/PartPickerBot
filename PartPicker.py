import pandas as pd


# чтение бд
cooling = pd.read_csv('cooling.csv')
cpu = pd.read_csv('cpu.csv')
hdd = pd.read_csv('hdd.csv')
motherboard = pd.read_csv('motherboard.csv')
power_supply = pd.read_csv('power_supply.csv')
ram = pd.read_csv('ram.csv')
ssd = pd.read_csv('ssd.csv')
videocard = pd.read_csv('videocard.csv')
case = pd.read_csv('case.csv', encoding='utf-8')

# выбор частей из базы
def getCPU(n=10, rec=None):
    if rec:
        return cpu[cpu["Recommended"]==int(rec)].head(n).values
    return cpu.head(n).values

def getCPUbyId(i):
    return cpu[cpu["Id"]==int(i)].values[0]

def getMotherboard(n=10, socket=None, rec=None):
    if socket == None:
        if rec:
            return motherboard[motherboard["Recommended"]==int(rec)].values
        return motherboard.head(n).values
    if rec:
        return motherboard[(motherboard["Recommended"]==int(rec)) and (motherboard["Socket"]==socket)].head(n).values
    return motherboard[motherboard["Socket"]==socket].head(n).values

def getMotherboardById(i):
    return motherboard[motherboard["Id"]==int(i)].values[0]

def getCooling(n=10, rec=None):
    if rec:
        return cooling[cooling["Recommended"]==int(rec)].head(n).values
    return cooling.head(n).values 

def getCoolingById(i):
    return cooling[cooling["Id"]==int(i)].values[0]

def getRAM(n=10, rec=None):
    if rec:
        return ram[ram["Recommended"]==int(rec)].head(n).values
    return ram.head(n).values

def getRAMById(i):
    return ram[ram["Id"]==int(i)].values[0]

def getVideocard(n=10, rec=None):
    if rec:
        return videocard[videocard["Recommended"]==int(rec)].head(n).values
    return videocard.head(n).values

def getVideocardById(i):
    return videocard[videocard["Id"]==int(i)].values[0]

def getPowersupply(n=10, rec=None):
    if rec:
        return power_supply[power_supply["Recommended"]==int(rec)].head(n).values
    return power_supply.head(n).values

def getPowersupplyById(i):
    return power_supply[power_supply["Id"]==int(i)].values[0]

def getSSD(n=10, rec=None):
    if rec:
        return ssd[ssd["Recommended"]==int(rec)].head(n).values
    return ssd.head(n).values

def getSSDById(i):
    return ssd[ssd["Id"]==int(i)].values[0]

def getHDD(n=10, rec=None):
    if rec:
        return hdd[hdd["Recommended"]==int(rec)].head(n).values
    return hdd.head(n).values

def getHDDById(i):
    return hdd[hdd["Id"]==int(i)].values[0]

def getCase(n=10, rec=None):
    if rec:
        return case[case["Recommended"]==int(rec)].head(n).values
    return case.head(n).values

def getCaseById(i):
    return case[case["Id"]==int(i)].values[0]


if __name__ == "__main__":
    print(cpu[cpu["Id"]==8].values[0])