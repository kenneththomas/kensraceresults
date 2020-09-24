import pandas
import numpy

rdf = pandas.read_csv('raceresults.csv')
print(rdf)
rdf2 = rdf


ages = rdf2.Age.unique()
final = pandas.DataFrame(columns=['Age'])

for age in ages:
    agedf = rdf2[rdf2['Age']==age]
    races = agedf.Distance.unique()

    seasonbests = {'Age' : age}

    for race in races:
        racedf = agedf[agedf['Distance']==race]
        seasonbest = racedf['Time'].min()
        seasonbests[race] = seasonbest

    final = final.append(seasonbests,ignore_index=True)
    final = final.replace(numpy.nan, '', regex=True)


    print(seasonbests)
print(final)

agebests = final.to_html(index=False)
html = rdf.to_html(index=False)
webpage = open('index.html','w')
webpage.write('<h1>PB by Age</h1>')
webpage.write(agebests)
webpage.write('<br/>')
webpage.write('<h1>All Results</h1>')
webpage.write(html)
webpage.close()