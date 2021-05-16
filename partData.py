# генератор описания для комплектующих
def cpuData(c):
    mes = ''
    mes += f'{c[1]}'
    mes += f'\nSocket: {c[2]}'
    mes += f'\nCore: {c[3]}'
    mes += f'\nThread: {c[4]}'
    mes += f'\nFrequency: {c[5]} MHz'
    mes += f'\nCahe: {c[7]} mb'
    mes += f'\nPrice: {c[8]} '
    mes += f'\n{c[10]}'
    return mes

def motherboardData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nSocket: {m[2]}'
    mes += f'\nChipset: {m[3]}'
    mes += f'\nPrice: {m[4]}'
    mes += f'\n{m[6]}'
    return mes

def coolingData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nPropeller diameter: {m[2]}'
    mes += f'\nTdp: {m[3]}'
    mes += f'\nPrice: {m[4]}'
    mes += f'\n{m[6]}'
    return mes

def ramData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nLatency: {m[2]}'
    mes += f'\nPrice: {m[3]}'
    mes += f'\n{m[5]}'
    return mes

def videocardData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nFrequency: {m[2]}'
    mes += f'\nVideo memory: {m[3]}'
    mes += f'\nPrice: {m[4]}'
    mes += f'\n{m[6]}'
    return mes

def powersupplyData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nPower: {m[2]}'
    mes += f'\nPrice: {m[3]}'
    mes += f'\n{m[5]}'
    return mes

def ssdData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nInterface: {m[2]}'
    mes += f'\nSpeed: {m[3]}'
    mes += f'\nPrice: {m[4]}'
    mes += f'\n{m[6]}'
    return mes

def hddData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nStorage: {m[2]}'
    mes += f'\nInterface: {m[3]}'
    mes += f'\nBuffer: {m[4]}'
    mes += f'\nSpeed: {m[5]}'
    mes += f'\nPrice: {m[6]}'
    mes += f'\n{m[8]}'
    return mes

def caseData(m):
    mes = ''
    mes += f'{m[1]}'
    mes += f'\nType: {m[2]}'
    mes += f'\nPrice: {m[4]}'
    mes += f'\n{m[6]}'
    return mes
