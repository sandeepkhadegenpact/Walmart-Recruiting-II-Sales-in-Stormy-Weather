import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sys
import csv
from sklearn import datasets, linear_model
from sklearn import svm

path = 'C:\\Users\\ziaullhaq.s\\Desktop\\01042017\\Algebra\\ML\\Walmart\\Wallmart_ML\\Wallmart_ML\\'
csv_database = create_engine('sqlite:///csv_database.db')

#pd.read_sql_query('SELECT * FROM train', csv_database, chunksize=100000)                
                                   
#tarinData = pd.read_sql_query('SELECT * FROM train', csv_database)
#           index        date(dd-mm-yyyy)  store_nbr  item_nbr  units


#keyData = pd.read_sql_query('SELECT * FROM key', csv_database)
 #  index  store_nbr  station_nbr
 
#weatherData = pd.read_sql_query('SELECT * FROM weather', csv_database)
#index  station_number       datee(yyyy-mm--dd)       tmax       tmin       tavg depart   dewpoint    wetbulb 
#heat    ...      sunrise  sunset codesum  snowfall  preciptotal  stnpressure  sealevel resultspeed  resultdir   avgspeed
#print(weatherData)								Distinct station_nbr


# Columns: [index, station_number, datee, tmax, tmin, tavg, depart, dewpoint, wetbulb, heat, cool, sunrise, sunset, 
# codesum, snowfall, preciptotal, stnpressure, sealevel, resultspeed, resultdir, avgspeed]


"""
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w',newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("Error occurred with")
    return


trainWeatherData = []
trainData = pd.read_sql_query('SELECT * FROM train limit 20', csv_database)
for index,trainRow in trainData.iterrows():
	storeNumber = trainRow['store_nbr']
	dateAry		= trainRow['date'].split("-")
	date = dateAry[2]+"-"+dateAry[1]+"-"+dateAry[0]
	stationNumberResult = pd.read_sql_query('SELECT station_nbr FROM key where store_nbr='+str(storeNumber), csv_database)
	stationNumber = None
	for index,keyRow in stationNumberResult.iterrows():
		stationNumber= keyRow['station_nbr']
	weatherDetails = pd.read_sql_query('SELECT * FROM weather where station_number='+str(stationNumber)+' and datee="'+str(date)+'"', csv_database)
	for index,weatherRow in weatherDetails.iterrows():
		weatherRow['date'] 			= trainRow['date']
		weatherRow['store_nbr'] 	= storeNumber
		weatherRow['item_nbr'] 		= trainRow['item_nbr'] 	
		weatherRow['units']			= trainRow['units']
		row2dict = dict(weatherRow)
		trainWeatherData.append(row2dict);

columns = []
for key in trainWeatherData[0]:
	columns.append(key)
	
trainDataDF = pd.DataFrame(trainWeatherData,columns=['tmax', 'tmin','tavg','wetbulb','heat','cool','sealevel','station_number','store_nbr','item_nbr','stnpressure','resultspeed','sunrise', 'sunset','depart', 'dewpoint', 'wetbulb','snowfall', 'preciptotal']);
print(trainDataDF)
	
#trainDataDF = pd.DataFrame(trainWeatherData);
#print(trainDataDF);
#WriteDictToCSV(path+"train1.csv",columns,trainWeatherData)


"""


x = pd.read_csv(path+'train3.csv', usecols=['tmax', 'tmin','tavg','wetbulb','heat','cool','sealevel','station_number','store_nbr','item_nbr','stnpressure','resultspeed','sunrise', 'sunset','depart', 'dewpoint', 'wetbulb','snowfall', 'preciptotal'])
y = pd.read_csv(path+'train3.csv', usecols=['units'])
#x['date'] = pd.to_datetime(x['date'])
#x['date'] = np.datetime64(x['date'])
#print(x['date'])
#y['units'] = np.log(y.units+1)
xMatrix = x.as_matrix()
yMatrix = y.as_matrix()
#print(yMatrix.ravel())
#clf = svm.SVC(kernel='linear', C = 1.0)
#clf.fit(xMatrix,yMatrix.ravel())
regr = linear_model.LinearRegression()
regr.fit(xMatrix, yMatrix)

x_predict = pd.read_csv(path+'train3.csv', usecols=['tmax', 'tmin','tavg','wetbulb','heat','cool','sealevel','station_number','store_nbr','item_nbr','stnpressure','resultspeed','sunrise', 'sunset','depart', 'dewpoint', 'wetbulb','snowfall', 'preciptotal'])
#x_predict['date'] = pd.to_datetime(x_predict['date'])
y_predict = regr.predict(x_predict)
#y_predict = clf.predict(x_predict)
print(y_predict)
#print(xMatrix)
#print(yMatrix)





"""
trainData = pd.read_csv(path+'train.csv')
trainData.to_sql('train', csv_database)


keyData = pd.read_csv(path+'key.csv')
keyData.to_sql('key', csv_database)

weatherData = pd.read_csv(path+'weather1.csv')
weatherData.to_sql('weather', csv_database)
"""
