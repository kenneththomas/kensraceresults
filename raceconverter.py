import pandas

rdf = pandas.read_csv('raceresults.csv')
print(rdf)
html = rdf.to_html(index=False)
webpage = open('index.html','w')
webpage.write(html)
webpage.close()