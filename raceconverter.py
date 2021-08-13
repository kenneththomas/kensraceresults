import pandas
import numpy

rdf = pandas.read_csv('raceresults.csv')
print(rdf)
rdf2 = rdf


ages = rdf2.Age.unique()
final = pandas.DataFrame(columns=['Age'])
displaycolumns = ['Age','100m','200m','400m','600m','800m','1000m','1 Mile','2 Mile','5K','4 Mile']

for age in ages:
    agedf = rdf2[rdf2['Age']==age]
    races = agedf.Distance.unique()

    seasonbests = {'Age' : age}

    for race in races:
        racedf = agedf[agedf['Distance']==race]
        seasonbest = racedf['Time'].min()
        seasonbests[race] = seasonbest
        for a in displaycolumns:
            if a not in seasonbests.keys():
                seasonbests[a] = '-'

    final = final.append(seasonbests,ignore_index=True)
    final = final.replace(numpy.nan, '', regex=True)
    final = final[displaycolumns]


    print(seasonbests)
print(final)

agebests = final.to_html(index=False)
html = rdf.to_html(index=False)
webpage = open('index.html','w')
webpage.write('<h1>PR by Age</h1>')
webpage.write(agebests)
webpage.write('<br/>')
webpage.write('<h1>All Results</h1>')
webpage.write(html)
webpage.close()