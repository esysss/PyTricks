import sqlite3
import time
import datetime
import random
import matplotlib.pyplot
import matplotlib.dates
import matplotlib.style

matplotlib.style.use('ggplot')

conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS staffToPlot(unix REAL ,datestamp TEXT,keyword TEXT , value REAL)")

def data_entry():#for entering the data into the table
    c.execute("INSERT INTO staffToPlot VALUES (123456,'2019-01-20','python',5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H:%M:%S'))
    keyword = 'python' #becouse it's awesome
    value = random.randrange(0,10)
    c.execute("INSERT INTO staffToPlot(unix,datestamp,keyword,value ) VALUES (?,?,?,?)",
              (unix,date,keyword,value))
    conn.commit()

def makeData():
    for i in range(10):#we want to add some random data to the dataBase
        dynamic_data_entry()
        time.sleep(1)

def read_from_db():
    #c.execute("SELECT * FROM staffToPlot")#it catches all the data
    #c.execute("SELECT * FROM staffToPlot WHERE VALUE=3 AND KEYWORD='python'")#it catches just ...
    #c.execute("SELECT * FROM staffToPlot WHERE unix > 1548008112 AND value >5")#it catches just ...
    c.execute("SELECT unix,value From staffToPlot WHERE value >= 8")#it catches just ...
    data = c.fetchall()
    for row in data:
        print(row)

def graph_data():
    c.execute("SELECT unix,value FROM staffToPlot")
    dates = []
    values = []
    temp = c.fetchall()
    for row in temp:
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    matplotlib.pyplot.plot_date(dates,values,'-')
    matplotlib.pyplot.show()

def del_and_update():
    c.execute("SELECT * FROM staffToPlot")
    [print(row) for row in c.fetchall()]

    c.execute("UPDATE staffToPlot SET keyword = 'esysss' WHERE keyword = 'python'")# to change data in DB
    c.execute("UPDATE staffToPlot SET value = 50 WHERE value = 5")# to change data in DB
    conn.commit()

    [print('#'*50)] #it printes the # 50 times in a row

    c.execute("DELETE FROM staffToPlot WHERE value = 50") # it will delete where value is 50
    conn.commit()
    c.execute("SELECT * FROM staffToPlot")
    [print(row) for row in c.fetchall()]

#create_table()
# makeData()
# data_entry()
#read_from_db()
#graph_data()
del_and_update()

c.close()
conn.close()