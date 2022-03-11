import csv 
import requests
import os


MY_RDS_DB_URL = ""

def csv_to_lisdic(csv_name):
    dic_list = []
    with open(csv_name, mode='r') as infile:
        reader = csv.reader(infile)
        for row in csv.reader(infile):
            mydict = {}
            conv = lambda i : i or 'NULL'
            row = [conv(i) for i in row]
            row[4] = row[4].replace('-', '.')
            mydict['name'] = row[0].split('\\')[0].strip()
            mydict['position'] = row[1]
            mydict['college'] = row[2]
            mydict['height'] = row[4]
            mydict['weight'] = row[5]
            mydict['fourty'] = row[6]
            mydict['vertical'] = row[7]
            mydict['bench'] = row[8]
            mydict['broadjmp'] = row[9]
            mydict['threecone'] = row[10]
            mydict['shuttle'] = row[11]

            dic_list.append(mydict)
        return(dic_list)

if __name__ == "__main__":
    

    directory = os.fsencode("raw_csv/")
    
    for entry in os.scandir(directory):       
        list = csv_to_lisdic((entry.path.decode("utf-8") ))
        print(list)
        URL = MY_RDS_DB_URL
        
        for entry in list:
            r = requests.post(url = URL, params = entry)
