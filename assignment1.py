# This is the file you will need to edit in order to complete assignment 1
# You may create additional functions, but all code must be contained within this file


# Some starting imports are provided, these will be accessible by all functions.
# You may need to import additional items
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import json
import csv
import re
import os

# You should use these two variable to refer the location of the JSON data file and the folder containing the news articles.
# Under no circumstances should you hardcode a path to the folder on your computer (e.g. C:\Chris\Assignment\data\data.json) as this path will not exist on any machine but yours.
datafilepath = 'data/data.json'
articlespath = 'data/football'

def task1():
    #Complete task 1 here
    with open(datafilepath) as f:
        data = json.load(f)
    return sorted(data['teams_codes'])
    
def task2():
    #Complete task 2 here
    with open('task2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        # write header row
        writer.writerow(['team_code', 'goals_scored_by_team', 'goals_scored_against_team'])
        with open(datafilepath) as f:
            data = json.load(f)
            team_codes = data['teams_codes']
            sorted_team_codes = sorted(data['teams_codes'])
            for i in sorted_team_codes:
                club_index = team_codes.index(i)
                club = data['clubs'][club_index]
                # header info
                team_code = club["club_code"]
                goals_scored_by_team = club["goals_scored"]
                goals_scored_against_team = club["goals_conceded"]
                writer.writerow([team_code, goals_scored_by_team, goals_scored_against_team])
    return 
      
def task3():
    #Complete task 3 here
    
    with open('task3.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['filename', 'total_goals'])
        for txtfile in os.listdir(articlespath):
            sumOfScores = 0
            scores = re.findall(r'[0-99]{1,2}-[0-99]{1,2}', txtfile)

    return scores

def task4():
    #Complete task 4 here
    return
    
def task5():
    #Complete task 5 here
    return
    
def task6():
    #Complete task 6 here
    return
    
def task7():
    #Complete task 7 here
    return
    
def task8(filename):
    #Complete task 8 here
    return
    
def task9():
    #Complete task 9 here
    return