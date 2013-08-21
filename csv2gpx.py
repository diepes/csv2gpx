#csv2gpx.py
# Convert all CSV files in a given (using command line argument) folder to XML.
# PES - 201308 convert, read csv, in dir, lat,lon,name,category produce gpx. 
# FB - 20120523
# First row of the csv files must be the header!

# example CSV file: myData.csv
# lat,lon,name,Category
# -26.147329,28.035179,Australian Passport Walters Avenue,Australia-JHB,


import sys
import os
import csv
if len(sys.argv) != 2:
    os._exit(1)
path=sys.argv[1] # get folder as a command line argument
os.chdir(path)
csvFiles = [f for f in os.listdir('.') if f.endswith('.csv') or f.endswith('.CSV')]
for csvFile in csvFiles:
    xmlFile = csvFile[:-4] + '.gpx'
    csvData = csv.reader(open(csvFile))
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlData.write('<gpx version="1.1" creator="pes">' + "\n")
    rowNum = 0
    xml_template = '<wpt lat="%s" lon="%s"><name>%s</name><category>%s</category></wpt>'
    for row in csvData:
        if rowNum == 0:
            tags = row
            # replace spaces w/ underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else: 
            #xmlData.write('<row>' + "\n")
            #for i in range(len(tags)):
            #    xmlData.write('    ' + '<' + tags[i] + '>' \
            #                  + row[i] + '</' + tags[i] + '>' + "\n")
            #xmlData.write('</row>' + "\n")                
	    xmlData.write(xml_template % (row[0],row[1],row[2],row[3]) )
        rowNum +=1
    xmlData.write('</gpx>' + "\n")
    xmlData.close()
