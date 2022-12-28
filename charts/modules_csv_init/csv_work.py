import app
data = app.read_csv.read_csv1('./app/population.csv')
new_data = list(filter(lambda item: item['Continent'] == 'South America', data))
#data2 = app.read_csv.country(data)
#chart = app.charts.generate_bar_chart(data2)
data3 = app.read_csv.wordl_population(new_data)
chart = app.charts.generate_pie_chart(data3)