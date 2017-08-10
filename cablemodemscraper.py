#!/usr/bin/python
import requests
import json
from bs4 import BeautifulSoup

def makejson(dataList):
    json_data = json.dumps({"Cable Modem": {"Downstream Channel ID": {"Channel 1": dataList[1], "Channel 2": dataList[2], "Channel 3": dataList[3],"Channel 4": dataList[4]},
        "Downstream Channel Frequency": {"Channel 1": dataList[6], "Channel 2": dataList[7], "Channel 3": dataList[8], "Channel 4": dataList[9]},
        "Downstream SNR": {"Channel 1": dataList[11], "Channel 2": dataList[12], "Channel 3": dataList[13], "Channel 4": dataList[14]},
        "Downstream Power Level": {"Channel 1": dataList[21], "Channel 2": dataList[22], "Channel 3": dataList[23], "Channel 4": dataList[24]},
        "Upstream Channel ID": {"Channel 1": dataList[26], "Channel 2": dataList[27], "Channel 3": dataList[28], "Channel 4": dataList[29]},
        "Upstream Channel Frequency": {"Channel 1": dataList[31], "Channel 2": dataList[32], "Channel 3": dataList[33], "Channel 4": dataList[34]},
        "Upstream Ranging Service ID": {"Channel 1": dataList[36], "Channel 2": dataList[37], "Channel 3": dataList[38], "Channel 4": dataList[39]},
        "Upstream Symbol Rate": {"Channel 1": dataList[41], "Channel 2": dataList[42],  "Channel 3": dataList[43],  "Channel 4": dataList[44]},
        "Upstream Power Level": { "Channel 1": dataList[46],  "Channel 2": dataList[47],  "Channel 3": dataList[48],  "Channel 4": dataList[49]},
        "Upstream Ranging Status": {"Channel 1": dataList[56], "Channel 2": dataList[57], "Channel 3": dataList[58], "Channel 4": dataList[59]},
        "Signal Stats Unerrored Codewords": {"Channel 1": dataList[66], "Channel 2": dataList[67],  "Channel 3": dataList[68],  "Channel 4": dataList[69]},
        "Signal Stats Correctable Codewords": {"Channel 1": dataList[71], "Channel 2": dataList[72],  "Channel 3": dataList[73],  "Channel 4": dataList[74]},
        "Signal Stats Uncorrectable Codewords": {"Channel 1": dataList[76],  "Channel 2": dataList[77], "Channel 3": dataList[78], "Channel 4": dataList[79]}}},
            sort_keys=True, indent =4, separators=(',', ': '))

    return json_data

#Prep some variables
url = 'http://192.168.100.1/cmSignalData.htm'  # change to whatever your url is
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
tablecount = 1
dataList = []

#Find all table definitions and then loop through the table rows
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')

    i=0

    while i < tds.__len__() + 1:
        if i <> 1:
            try:
                dataList.append(tr.contents[i].text.encode('ascii','ignore'))
            except:
                pass
        i = i + 1

#Clean up some ugliness
dataList[0] = 'Downstream Channel ID'
dataList[5] = 'Downstream Channel Frequency'
dataList[10] = 'Downstream SNR'
dataList[15] = 'Downstream Modulation'
dataList[20] = 'Downstream Power Level'
dataList[21] = str(int(dataList[21].replace('dBmV','')))
dataList[22] = str(int(dataList[22].replace('dBmV','')))
dataList[23] = str(int(dataList[23].replace('dBmV','')))
dataList[24] = str(int(dataList[24].replace('dBmV','')))
dataList[25] = 'Upstream Channel ID'
dataList[30] = 'Downstream Channel Frequency'
dataList[35] = 'Upstream Ranging Service ID'
dataList[40] = 'Upstream Symbol Rate'
dataList[45] = 'Upstream Power Level'
dataList[46] = str(int(dataList[46].replace('dBmV','')))
dataList[47] = str(int(dataList[47].replace('dBmV','')))
dataList[48] = str(int(dataList[48].replace('dBmV','')))
dataList[49] = str(int(dataList[49].replace('dBmV','')))
dataList[50] = 'Upstream Modulation'
dataList[55] = 'Upstream Ranging Status'
dataList[60] = 'Downstream Channel Id'
dataList[65] = 'Total Unerrored Codewords'
dataList[70] = 'Total Correctable Codewords'
dataList[75] = 'Total Uncorrectable Codewords'

#Debug for printing all items within dataList[]
#attribCount = 0
#while attribCount < dataList.__len__():
#    print attribCount, dataList[attribCount]
#    attribCount = attribCount +1

print makejson(dataList)