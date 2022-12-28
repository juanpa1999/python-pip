import csv

def read_csv1(path):
    with open(path, 'r') as file_csv:
        reader = csv.reader(file_csv, delimiter= ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country = {key: v for key, v in iterable}
            data.append(country)
        return data


def country(data):
    user_value = input('Wich country would you like to graph: ').capitalize()
    new_data = list(filter(lambda item: item['Country/Territory'] == user_value, data))
    dic2 = {}
    for ii in new_data:
        for i, e in ii.items():
            if 'Percentage' in i:
                continue
            if 'Population' in i:
                dic2[i] = e
        print(dic2)
    return dic2


def wordl_population(data):
    countries = list(map(lambda a: a['Country/Territory'], data))
    population = list(map(lambda a: a['World Population Percentage'], data))
    dic_coun_popu = {country: popul for (country, popul) in zip(countries, population)}
    return dic_coun_popu

if __name__ == '__main__':
    data = read_csv1('./population.csv')
    print(data[0])