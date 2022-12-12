import requests
import unittest
import sqlite3
import json
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from statistics import mean


# def get_michigan_date(year,week):
#     headers = {
#             'accept': 'application/json',
#             'Authorization': 'Bearer jZGKLT++7nEywEb8ej0sEtM/+rMHPO59/KxVx/8BWlTfYpV4Hsj8+lzLpLZiwuGh',
#     }
#     params = {
#             'year': year,
#             'week': week,
#             'seasonType': 'regular',
#             'team': 'Michigan',
#             'division': 'fbs',
#     }
#     response = requests.get('https://api.collegefootballdata.com/games', params=params, headers=headers)
#     data_as_json = response.json()
#     start_date = (data_as_json[0]["start_date"])
#     date = start_date[:10]
#     return date

# def get_michigan_score(year,week):
#     headers = {
#             'accept': 'application/json',
#             'Authorization': 'Bearer jZGKLT++7nEywEb8ej0sEtM/+rMHPO59/KxVx/8BWlTfYpV4Hsj8+lzLpLZiwuGh',
#     }
#     params = {
#             'year': year,
#             'week': week,
#             'seasonType': 'regular',
#             'team': 'Michigan',
#             'division': 'fbs',
#     }
#     response = requests.get('https://api.collegefootballdata.com/games', params=params, headers=headers)
#     data_as_json = response.json()
#     score_total = data_as_json[0]["home_points"] + data_as_json[0]["away_points"]
#     return score_total

# def get_michigan_temp(year,week):
#     string = "https://api.weatherstack.com/historical?access_key=89cc8c429b8e9d7635ec1dcc34bace1a&query=Ann%20Arbor&units=f&historical_date=" + str(get_michigan_date(year,week))
#     response = requests.get(string)
#     data_as_json = response.json()
#     return data_as_json['historical'][str(get_michigan_date(year,week))]['avgtemp']


# def data_storing ():
#     search_year = []
#     search_week = []
#     date_list = []
#     temp_list = []
#     score_list = []
#     for b in range(2009,2019):
#         for x in range(1,12):
#             search_year.append(str(b))
#             search_week.append(str(x))
#     x = tuple(zip(search_year, search_week))
#     for values in range(len(x)):
#         try:
#             date_list.append(get_michigan_date(x[values][0],x[values][1]))
#             print(get_michigan_date(x[values][0],x[values][1]))
#         except:
#             print('date error')
#         try:
#             temp_list.append(get_michigan_temp(x[values][0],x[values][1]))
#             print(get_michigan_temp(x[values][0],x[values][1]))
#         except:
#             print('temp error')
#         try:
#             score_list.append(get_michigan_score(x[values][0],x[values][1]))
#             print(get_michigan_score(x[values][0],x[values][1]))
#         except:
#             print('score error')
#     temp_list.append(42)
#     final_tuple = (date_list,temp_list,score_list)
#     print(final_tuple)
#     return final_tuple

# data = data_storing()
data = (['2009-09-05', '2009-09-12', '2009-09-19', '2009-09-26', '2009-10-03', '2009-10-11', '2009-10-17', '2009-10-24', '2009-10-31', '2009-11-07', '2009-11-14', '2010-09-04', '2010-09-11', '2010-09-18', '2010-09-25', '2010-10-02', '2010-10-09', '2010-10-16', '2010-10-31', '2010-11-06', '2010-11-13', '2011-09-03', '2011-09-11', '2011-09-17', '2011-09-24', '2011-10-01', '2011-10-08', '2011-10-15', '2011-10-29', '2011-11-05', '2011-11-12', '2012-09-02', '2012-09-08', '2012-09-15', '2012-09-22', '2012-10-06', '2012-10-13', '2012-10-20', '2012-10-28', '2012-11-03', '2012-11-10', '2013-08-31', '2013-09-08', '2013-09-14', '2013-09-22', '2013-10-05', '2013-10-12', '2013-10-19', '2013-11-02', '2013-11-09', '2014-08-30', '2014-09-06', '2014-09-13', '2014-09-20', '2014-09-27', '2014-10-04', '2014-10-11', '2014-10-25', '2014-11-01', '2014-11-08', '2015-09-04', '2015-09-12', '2015-09-19', '2015-09-26', '2015-10-03', '2015-10-10', '2015-10-17', '2015-10-31', '2015-11-07', '2015-11-14', '2016-09-03', '2016-09-10', '2016-09-17', '2016-09-24', '2016-10-01', '2016-10-08', '2016-10-22', '2016-10-29', '2016-11-05', '2016-11-13', '2017-09-02', '2017-09-09', '2017-09-16', '2017-09-23', '2017-10-07', '2017-10-14', '2017-10-21', '2017-10-28', '2017-11-05', '2017-11-11', '2018-09-01', '2018-09-08', '2018-09-15', '2018-09-22', '2018-09-29', '2018-10-06', '2018-10-13', '2018-10-20', '2018-11-03', '2018-11-10'], [73, 70, 61, 64, 52, 41, 41, 45, 45, 54, 54, 57, 61, 66, 54, 50, 64, 54, 41, 34, 50, 81, 68, 57, 57, 68, 50, 43, 43, 46, 72, 63, 64, 54, 45, 48, 48, 43, 37, 55, 73, 68, 59, 54, 70, 64, 45, 45, 46, 77, 66, 66, 68, 68, 43, 50, 57, 34, 39, 73, 55, 64, 66, 48, 55, 39, 46, 46, 41, 70, 72, 70, 63, 63, 52, 45, 64, 54, 45, 64, 59, 73, 82, 73, 66, 66, 41, 59, 32, 79, 64, 77, 59, 54, 72, 45, 46, 41, 30, 42], [38, 72, 62, 69, 46, 58, 69, 45, 51, 74, 69, 40, 52, 79, 86, 77, 51, 66, 72, 132, 43, 44, 66, 34, 35, 58, 66, 42, 50, 40, 45, 55, 56, 76, 19, 57, 45, 22, 32, 48, 69, 68, 71, 52, 45, 55, 83, 110, 35, 30, 66, 31, 44, 36, 44, 50, 31, 46, 44, 19, 41, 42, 35, 31, 28, 38, 50, 55, 65, 89, 66, 65, 73, 59, 21, 78, 49, 55, 62, 27, 50, 50, 42, 38, 24, 47, 55, 49, 43, 45, 41, 52, 65, 66, 37, 63, 51, 28, 49, 49])

#//////////////////////////////////////////////////////////////////////////////////////////

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
setUpDatabase("final_project_1.db")

#//////////////////////////////////////////////////////////////////////////////////////////
id_list = list(range(1,101))

def create_date_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Dates (ID INTEGER PRIMARY KEY, Date TEXT)")
    cur.execute("SELECT COUNT(ID) as count_pet FROM Dates")
    result = cur.fetchone()
    current_count = result[0]
    dates = data[0]
    
    if current_count + 25 > len(id_list):
        endValue = len(id_list)
    else:
        endValue = current_count + 25
    
    for x in range(current_count,endValue):
        cur.execute("INSERT or IGNORE INTO Dates (ID, Date) VALUES (?,?)", (id_list[x], dates[x]))
    conn.commit()



def create_weather_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Temperature (ID INTEGER PRIMARY KEY, Temp TEXT)")
    cur.execute("SELECT COUNT(ID) as count_pet FROM Temperature")
    result = cur.fetchone()
    current_count = result[0]
    weather = data[1]

    if current_count + 25 > len(id_list):
        endValue = len(id_list)
    else:
        endValue = current_count + 25
    
    for x in range(current_count,endValue):
        cur.execute("INSERT or IGNORE INTO Temperature (ID, Temp) VALUES (?,?)", (id_list[x], weather[x]))
    conn.commit()



def create_game_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Scores (ID INTEGER PRIMARY KEY, Score TEXT)")
    cur.execute("SELECT COUNT(ID) as count_pet FROM Scores")
    result = cur.fetchone()
    current_count = result[0]
    score = data[2]

    if current_count + 25 > len(id_list):
        endValue = len(id_list)
    else:
        endValue = current_count + 25
    
    for x in range(current_count,endValue):
        cur.execute("INSERT or IGNORE INTO Scores (ID, Score) VALUES (?,?)", (id_list[x], score[x]))
    conn.commit()


def join_tables(cur, conn):
    cur.execute('SELECT * FROM Scores INNER JOIN Temperature ON Scores.ID = Temperature.ID')
    
    res = cur.fetchall()
    score_temp_list = []
    conn.commit()
    for values in res:
        x = (int(values[1]),int(values[3]))
        score_temp_list.append(x)
    return score_temp_list

def writing_file(data):
    with open('desktop/data_output.txt', 'w') as f:
        x_values = []
        for values in data:
            x_values.append(values[1])
        f.write("Mean of Temperatures: " + str(mean(x_values)))

#//////////////////////////////////////////////////////////////////////////////////////////

def plotly_Scores_Vs_temp(table_data):
    years = data[0]
    scores = []
    temp = []
    for values in table_data:
        scores.append(values[0])
        temp.append(values[1])
    df = px.data.tips()
    fig = px.scatter(df,x=scores,y=temp, trendline="ols",title="Scores VS Temperatures for Umich Football Games 2009 - 2019")
    fig.show()


def make_hist_score(data):
    x_values = []
    for values in data:
        x_values.append(values[0])
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(x_values, bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130])
    plt.xlabel("Scores")
    plt.ylabel("Number of Times")
    plt.show()



def make_mean_hist_temp(data):
    x_values = []
    for values in data:
        x_values.append(values[1])
    fig, ax = plt.subplots(figsize =(10, 7))
    
    ax.hist(mean(x_values), bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
    plt.xlabel("Mean of Temperatures")
    plt.ylabel("Number of Times")
    plt.show()

def make_hist_temp(data):
    x_values = []
    for values in data:
        x_values.append(values[1])
    fig, ax = plt.subplots(figsize =(10, 7))
    
    ax.hist((x_values), bins = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])
    plt.xlabel("Temperatures")
    plt.ylabel("Number of Times")
    plt.show()


def make_plotly(table_data):
    years = data[0]
    scores = []
    temp = []
    for values in table_data:
        scores.append(values[0])
        temp.append(values[1])
    fig = go.Figure(data = [
        go.Bar(name= "Scores", x=years, y=scores),
        go.Bar(name= "Temperature", x=years, y=temp)])
    fig.update_layout(barmode='group')
    fig.show()




#//////////////////////////////////////////////////////////////////////////////////////////


def main():
    cur, conn = setUpDatabase("final_project_1.db")
    create_date_table(cur, conn)
    create_weather_table(cur, conn)
    create_game_table(cur, conn)
    join_tables(cur, conn)
    writing_file(join_tables(cur, conn))
    plotly_Scores_Vs_temp(join_tables(cur, conn))
    make_mean_hist_temp(join_tables(cur, conn))
    make_hist_score(join_tables(cur, conn))
    make_hist_temp(join_tables(cur, conn))
    make_plotly(join_tables(cur, conn))

main()