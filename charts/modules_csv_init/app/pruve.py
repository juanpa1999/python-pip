import csv

def unit(tt):
  with open(tt, 'r') as file3:
    reader = csv.reader(file3, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = unit('./population.csv')
  print(data[0])