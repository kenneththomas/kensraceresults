import pandas
import numpy
from jinja2 import Environment, FileSystemLoader

rdf = pandas.read_csv('raceresults.csv')
print(rdf)
rdf2 = rdf


ages = rdf2.Age.unique()
final = pandas.DataFrame(columns=['Age'])
displaycolumns = ['Age','100m','200m','400m','600m','800m','1000m','1 Mile','3200m','5K','4 Mile','5 Mile','Half Marathon']
pr_races = []

for age in ages:
    agedf = rdf2[rdf2['Age']==age]
    races = agedf.Distance.unique()

    seasonbests = {'Age' : age}

    for race in races:
        racedf = agedf[agedf['Distance']==race]
        seasonbest = racedf['Time'].min()
        pr_races.append(racedf['Time'].min())
        seasonbests[race] = seasonbest
        for a in displaycolumns:
            if a not in seasonbests.keys():
                seasonbests[a] = '-'

    final = final.append(seasonbests,ignore_index=True)
    final = final.replace(numpy.nan, '', regex=True)
    final = final[displaycolumns]
    print(seasonbests)
print(final)

agebests = final.to_html(index=False, classes="table")
html = rdf.to_html(index=False, classes="table")

# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the data
rendered_html = template.render(agebests=agebests, html=html)

# Save the rendered HTML to a file
with open("index.html", "w") as webpage:
    webpage.write(rendered_html)