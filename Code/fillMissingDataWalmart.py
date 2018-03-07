import MySQLdb
import csv
import matplotlib

path = 'C:\\Users\\ziaullhaq.s\\Desktop\\01042017\\Algebra\\ML\\Walmart\\Wallmart_ML\\Wallmart_ML\\'

class Database:

    host = 'localhost'
    user = 'root'
    password = 'Root@123'
    db = 'walmart'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insertUsingQuery(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()
            
    def insert(self,query,params):
        try:
            self.cursor.execute(query,params)
            self.connection.commit()
        except:
            self.connection.rollback()

    def jsutUseQuery(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)
        return cursor.fetchall()
        
        
    def query(self,query,params):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query,params)
        return cursor.fetchall()		

    def __del__(self):
        self.connection.close()
        

def updateColumns(columns,valToCk):	
	db = Database()
	for column in columns:			
		columnName = column		
		query = ("SELECT DISTINCT station_number from weather where TRIM("+columnName+")=%s")
		db.cursor.execute(query, (valToCk))	

		for(station_number) in db.cursor:
			avgOfTmax = db.query(("SELECT avg("+columnName+"),station_number from weather where station_number=%s"),(station_number))
			for x in avgOfTmax:
				db.insert(("UPDATE weather SET "+columnName+"=%s WHERE station_number=%s and TRIM("+columnName+")=%s"),(x['avg('+columnName+')'],x['station_number'],valToCk))	
	db.connection.commit()			
	db.cursor.close()

def updateColumnsByMinValue(columns,valToCk):	
	db = Database()
	for column in columns:			
		columnName = column				
		x = db.query(("SELECT distinct "+columnName+" FROM weather where trim("+columnName+")!=%s ORDER BY "+columnName+" ASC"),(valToCk))
		for minValue in x:
			if(float(minValue[columnName])>0):
				db.insert(("UPDATE weather SET "+columnName+"=%s WHERE TRIM("+columnName+")=%s"),(minValue[columnName],valToCk))	
				break;
	db.connection.commit()			
	db.cursor.close()

if __name__ == "__main__":
	
	db = Database()
	
	del_query = "DELETE FROM weather"
	db.insertUsingQuery(del_query)
	query = '''INSERT into weather (station_number,datee,tmax,tmin,tavg,depart,dewpoint,wetbulb,heat,cool,sunrise,sunset,codesum,snowfall,preciptotal,stnpressure,sealevel,resultspeed,resultdir,avgspeed) values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)'''
	#keyQuery = '''INSERT into str_stn_mp (store_number,station_number) values (%s, %s)'''
	fileWeather=open( path +"weather.CSV", "r")
	reader = csv.reader(fileWeather)
	for line in reader:
		db.cursor.execute(query,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19]))
	db.connection.commit()
	
	del_query = "DELETE FROM str_stn_mp"
	db.insertUsingQuery(del_query)
	keyQuery = '''INSERT into str_stn_mp (store_number,station_number) values (%s, %s)'''
	filekey=open( path +"key.CSV", "r")
	reader = csv.reader(filekey)
	for line in reader:
		db.cursor.execute(query,(line[0],line[1]))
	db.connection.commit()
	
	
	columns = ["tmax","tmin","tavg","depart","dewpoint","wetbulb","heat","cool"]
	val = "M"			
	updateColumns(columns,val);		
	
	columns = ["sunrise","sunset"]
	val = "-"			
	updateColumns(columns,val);			
			
	columns = ["stnpressure","sealevel","resultspeed","resultdir","avgspeed"]
	val = "M"
	updateColumns(columns,val);		
	
	columns = ["snowfall","preciptotal"]
	val = "M"
	updateColumns(columns,val);
	
	columns = ["snowfall","preciptotal"]
	val = "T"
	updateColumnsByMinValue(columns,val)
	
	
	with open( path +"weather1.CSV", "w",newline="") as csvfile:
		fieldnames = ['station_number','datee','tmax','tmin','tavg','depart','dewpoint','wetbulb','heat','cool','sunrise','sunset','codesum','snowfall','preciptotal','stnpressure','sealevel','resultspeed','resultdir','avgspeed']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		rows = db.jsutUseQuery(("SELECT * from weather"))
		for row in rows:
			writer.writerow(row) 
		print("Writing complete")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	"""db = Database()
	
	with open( path +"weather1.CSV", "w",newline="") as csvfile:
		fieldnames = ['station_number','datee','tmax','tmin','tavg','depart','dewpoint','wetbulb','heat','cool','sunrise','sunset','codesum','snowfall','preciptotal','stnpressure','sealevel','resultspeed','resultdir','avgspeed']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		rows = db.jsutUseQuery(("SELECT * from weather
		for row in rows:
			writer.writerow(row) 
		print("Writing complete")
"""
	
	
	"""#CleanUp Operation
	del_query = "DELETE FROM weather"
	db.insertUsingQuery(del_query)
	query = '''INSERT into weather (station_number,datee,tmax,tmin,tavg,depart,dewpoint,wetbulb,heat,cool,sunrise,sunset,codesum,snowfall,preciptotal,stnpressure,sealevel,resultspeed,resultdir,avgspeed) values (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)'''
	#keyQuery = '''INSERT into str_stn_mp (store_number,station_number) values (%s, %s)'''
	file=open( path +"weather.CSV", "r")
	reader = csv.reader(file)
	for line in reader:
		#db.cursor.execute(query,(line[0],line[1]))
		db.cursor.execute(query,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18],line[19]))
	db.connection.commit()
	
	columns = ["tmax","tmin","tavg","depart","dewpoint","wetbulb","heat","cool"]
	val = "M"			
	updateColumns(columns,val);		
	
	columns = ["sunrise","sunset"]
	val = "-"			
	updateColumns(columns,val);			
			
	columns = ["stnpressure","sealevel","resultspeed","resultdir","avgspeed"]
	val = "M"
	updateColumns(columns,val);		
	
	columns = ["snowfall","preciptotal"]
	val = "M"
	updateColumns(columns,val);
	
	columns = ["snowfall","preciptotal"]
	val = "T"
	updateColumnsByMinValue(columns,val)
	"""
	
