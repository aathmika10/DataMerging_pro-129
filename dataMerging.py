import csv
dataSet1=[]
dataSet2=[]

with open ("BrightStars.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet1.append(row)

headers1=dataSet1[0]
planetData1=dataSet1[1:]

with open("BrightStars2.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataSet2.append(row)

headers2=dataSet2[0]
planetData2=dataSet2[1:]

headers=headers1+headers2
planetData=[]

for index,dataRow in enumerate(planetData1):
    planetData.append(planetData1[index]+planetData1[index])

with open("final.csv","a+")as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)