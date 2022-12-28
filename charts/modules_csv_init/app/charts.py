import matplotlib.pyplot as plt

def generate_bar_chart(dic):
  labels = []
  values = []
  for i, e in dic.items():
    labels.append(i)
    values.append(int(e))
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('.pie.png')
  plt.close()

def generate_pie_chart(dic):
  labels = []
  values = []
  for i, e in dic.items():
    labels.append(i)
    values.append(float(e))
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('.pie.png')
  plt.close()

if __name__ == '__main__':
  generate_bar_chart(dic2)