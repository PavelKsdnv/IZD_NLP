streets_data = {
    '8-MI DEKEMVRI': {'city': 'SOFIA'},
    'ALEKSANDAR MALINOV': {'city': 'SOFIA'},
    'TSARIGRADSKO SHOSE': {'city': 'SOFIA'},
    'HRISTO BOTEV': {'city': 'VARNA'},
    '3-TI MART': {'city': 'SVISHTOV'},
    'PATRIARH EVTIMIJ': {'city': 'SVISHTOV'},
    'TSAR OSVOBODITEL': {'city': 'SVISHTOV'},
    'DUNAVSKA': {'city': 'VIDIN'},
    'BOJCHO ZHELEV': {'city': 'PROVADIA'},
}

cities_data = {
    'VARNA',
    'SOFIA',
    'SVISHTOV',
    'PROVADIA',
    'VIDIN'
}

def CheckPerfectAddress(input):
    cityNameFound = None
    streetNameFound = None

    input = input.upper()
    for city in cities_data:
        if (city in input):
            cityNameFound = city

    if (cityNameFound == None):
        print('No city found')
        return False

    print('city:', cityNameFound)

    availableStreets = {key: value for key, value in streets_data.items() if value['city'] == cityNameFound}
    
    # print('available streets:', availableStreets)

    for street in availableStreets:
        if (street in input):
            streetNameFound = street

    if (streetNameFound == None):
            print('No street found')
            return False
            
    print('street:', streetNameFound)
    return True

def main():
    while(True):
        inputAddress = input("Enter address: ")
        success = CheckPerfectAddress(inputAddress)
        print(success)

main()