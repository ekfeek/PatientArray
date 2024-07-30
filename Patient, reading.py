Patient = []
Readings = [
    [],
    []
]

TempLow = 31.6
TempHigh = 37.2
PulseLow = 55.0
PulseHigh = 100.0

def TempRange(Temperature):
    return Temperature >= TempLow and Temperature <= TempHigh

def PulseRange(Pulse):
    return Pulse >= PulseLow and Pulse <= PulseHigh



def VitalChecker(HospitalNumber):
    if HospitalNumber >= 1 and HospitalNumber <= 1000:
        PatientName = Patient[HospitalNumber-1]
        
        Temperature = Readings[HospitalNumber-1][0]
        Pulse = Readings[HospitalNumber-1][1]

        if TempRange(Temperature) and PulseRange(Pulse):
            print('Normal Readings')
        elif TempRange(Temperature) and not PulseRange(Pulse):
            print('Warning: Pulse out of range')
        elif not TempRange(Temperature) and PulseRange(Pulse):
            print('Warning, Temperature out of range')
        else:
            print('Severe Warning: Pulse and Temperature out of range')

        
    


    else: 
        print('Not Valid')
