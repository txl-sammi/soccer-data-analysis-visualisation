# This is the file you will need to edit in order to complete assignment 1
# You may create additional functions, but all code must be contained within this file


# Some starting imports are provided, these will be accessible by all functions.
# You may need to import additional items
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import arange
import seaborn as sns
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
    with open(datafilepath, encoding='utf-8') as f:
        data = json.load(f)
    return sorted(data['teams_codes'])
    
def task2():
    #Complete task 2 here
    with open('task2.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        # write header row
        writer.writerow(['team_code', 'goals_scored_by_team', 'goals_scored_against_team'])
        with open(datafilepath, encoding='utf-8') as f:
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
        listOfFiles = os.listdir(articlespath)
        listOfFiles.sort()
        for txtfile in listOfFiles:
            if txtfile.endswith(".txt"):
                filename = open(articlespath + '/' + txtfile, 'r')
                text = filename.read()
                filename.close()
                scores = re.findall(r'(?<=\D)\d{1,2}-\d{1,2}(?=\D)', text)
                maxSum = 0
                if scores == []:
                    maxSum = 0
                else:
                    for score in scores:
                        sumOfScores = 0
                        listOfString = score.split('-')
                        for number in listOfString:
                            sumOfScores += int(number)
                        if sumOfScores > maxSum:
                            maxSum = sumOfScores
            writer.writerow([txtfile, maxSum])
        
    return

def task4():
    #Complete task 4 here
    with open('task3.csv', 'r'):
        total_goals = pd.read_csv('task3.csv', encoding = 'ISO-8859-1')
        goals = total_goals['total_goals']
        files = total_goals['filename']
        goals.index = files
        plt.boxplot(goals)
        plt.title("Distribution of highest total number of goals found in news articles")
        plt.ylabel("Number of goals")
        plt.savefig("task4.png")
    return
    
def task5():
    #Complete task 5 here
    with open('task5.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['club_name', 'number_of_mentions'])
        listOfFiles = os.listdir(articlespath)
        with open(datafilepath, encoding='utf-8') as f:
            data = json.load(f)
            clubs = data["clubs"]
            for club in clubs:
                counter = 0
                for filename in listOfFiles:
                    if filename.endswith(".txt"):
                        txtfile = open(articlespath + '/' + filename, 'r')
                        text = txtfile.read()
                        txtfile.close()
                        mentions = re.findall(club["name"], text)
                        if mentions != []:
                            counter += 1
                writer.writerow([club["name"], counter])
    with open('task5.csv', 'r'):
        taskcsv = pd.read_csv('task5.csv', encoding = 'ISO-8859-1')
        mentions = taskcsv['number_of_mentions']
        clubs = taskcsv['club_name']
        plt.bar(arange(len(mentions)),mentions)
        plt.xticks( arange(len(clubs)),clubs, rotation=70, fontsize=9)
        plt.ylabel('Number of mentions')
        plt.xlabel('Club names')
        plt.title('Number of articles that mentioned the club name')
        plt.tight_layout()
        plt.savefig('task5.png')
    return
    
def task6():
    #Complete task 6 here
    with open('task5.csv', 'r') as csvfile:
        mentions = pd.read_csv('task5.csv', encoding = 'ISO-8859-1')
        numberOfMentions = mentions['number_of_mentions']
        clubName = mentions['club_name']
        reader = csv.DictReader(csvfile)
        with open('task6.csv', 'w') as heatcsv:
            writer = csv.writer(heatcsv)
            writer.writerow(clubName)
            i=0
            for row in reader:
                club1_name = row['club_name']
                number_of_mentions1 = row['number_of_mentions']
                data = []
                while i<len(numberOfMentions):
                    number_of_mentions2 = numberOfMentions[i]
                    club2_name = clubName[i]
                    listOfFiles = os.listdir(articlespath)
                    number_of_mentions_both = 0
                    for filename in listOfFiles:
                        txtfile = open(articlespath + '/' + filename, 'r')
                        text = txtfile.read()
                        txtfile.close()
                        mentionsClub1 = re.findall(club1_name, text)
                        mentionsClub2 = re.findall(club2_name, text)
                        if mentionsClub2 != [] and mentionsClub1 != []:
                            number_of_mentions_both += 1
                    if number_of_mentions1 == 0 and number_of_mentions2 == 0:
                        similarityScore = 0
                    else:
                        similarityScore = (2*number_of_mentions_both) / (int(number_of_mentions1) + int(number_of_mentions2))
                    data.append(similarityScore)
                writer.writerow(data)
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