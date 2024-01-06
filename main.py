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
    inputSet = set(input.split())
    highestPercentage = 0.0
    
    for city in cities_data:
        if (cityNameFound != None):
            break
        for inputElement in inputSet:
            if (city == inputElement):
                cityNameFound = city
                break
            currPercentage = similarity_percentage(city, inputElement)
            if (currPercentage > 30.0 and currPercentage > highestPercentage):
                print('Is the city', city, '?')
                cityNameFound = city
                highestPercentage = currPercentage

    if (cityNameFound == None):
        print('No city found')
        return False

    print('city:', cityNameFound)

    availableStreets = {key: value for key, value in streets_data.items() if value['city'] == cityNameFound}
    
    # print('available streets:', availableStreets)
    highestPercentage = 0.0

    for street in availableStreets:
        if (streetNameFound != None):
            break
        for inputElement in inputSet:
            if (street == inputElement):
                streetNameFound = street
                break
            currPercentage = similarity_percentage(street, inputElement)
            if (currPercentage > 30.0 and currPercentage > highestPercentage):
                print('Is the street', street, '?')
                streetNameFound = street
                highestPercentage = currPercentage

    if (streetNameFound == None):
            print('No street found')
            return False
            
    print('street:', streetNameFound)
    return True

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances

    return distances[-1]

def jaccard_similarity_percentage(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    similarity = len(intersection) / len(union)
    return similarity * 100

def similarity_percentage(s1, s2):
    max_len = max(len(s1), len(s2))
    distance = levenshtein_distance(s1, s2)
    similarity1 = 1 - (distance / max_len)
    
    similarity2 = jaccard_similarity_percentage(s1,s2)
    # print('first percentage: ', similarity1, 'second percentage: ', similarity2)
    return max(similarity1, similarity2) * 100

def main():
    while(True):
        inputAddress = input("Enter address: ")
        success = CheckPerfectAddress(inputAddress)

        print(success)

main()