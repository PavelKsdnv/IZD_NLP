import csv
from itertools import permutations

streets_data = {}
cities_data = []

def CheckPerfectAddress(input):
    cityNameFound = None
    streetNameFound = None

    input = input.upper()
    inputSet = set(input.split())
    highestPercentage = 0.0

    # Generate all possible combinations of different lengths
    all_combinations = set()

    for r in range(1, len(inputSet) + 1):
        combinations_of_length_r = set(' '.join(combination) for combination in permutations(inputSet, r))
        all_combinations = all_combinations.union(combinations_of_length_r)

    # Now, all_combinations contains all unique combinations of different lengths with a space in between the strings
    print(all_combinations)
    
    all = inputSet.union(all_combinations)
    
    print(all)
    
    for city in cities_data:
        if (cityNameFound != None and highestPercentage == 100):
            break
        for inputElement in all:
            if (city == inputElement):
                cityNameFound = city
                highestPercentage = 100
                break
            currPercentage = similarity_percentage(city, inputElement)
            if (currPercentage > 30.0 and currPercentage > highestPercentage):
                print('Is the city', city, '?',inputElement, "looks a lot like it")
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
        if (streetNameFound != None and highestPercentage == 100):
            break
        for inputElement in all:
            if (street == inputElement):
                streetNameFound = street
                highestPercentage = 100
                break
            currPercentage = similarity_percentage(street, inputElement)
            if (currPercentage > 30.0 and currPercentage > highestPercentage):
                print('Is the street', street, '?', inputElement, "looks a lot like it")
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
    # Read the CSV file and structure the data
    with open("./data.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            street = row['street']
            city = row['city']
            streets_data[street] = {'city': city}
            if (city not in cities_data):
                cities_data.append(city)
    print(streets_data)
    print("\n", cities_data)

    while(True):
        inputAddress = input("Enter address: ")
        success = CheckPerfectAddress(inputAddress)

        print(success)



main()