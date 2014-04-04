import csv
import itertools
import os

teamofinterest = "4990"
#Be sure to save as a windows csv

teams = []
lazyScoutsTeamList=[]
matches = [0]
maxMatchNumber = 0

def deleteOld():
    f = open("MatchesIn.csv", "w+")
    f.close()
    f = open("Teams.csv", "w+")
    f.close()
    f = open("MatchesToWatch.csv", "w+")
    f.close()

def printHeaders():
    with open("MatchesIn.csv", "a") as writefile:
        writer = csv.writer(writefile, delimiter=",")
        writer.writerow(["Match","Teams With","Teams Against","Opposing alliance","Your strategy"])

def findMatches():
    global maxMatchNumber
    i = 0
    with open('Regional.csv') as sourcefile:
        spamreader = csv.reader(sourcefile, delimiter=',')
        for row in spamreader:
            i=i+1
            maxMatchNumber = i
            list(row)
            for j in range (1,len(row)-2):
                if row[j] == teamofinterest:
                    matches.append(i)
                    alliance1 = row[1:4]
                    alliance2 = row[4:7]
                    if teamofinterest in alliance1:
                        temp = alliance1.index(teamofinterest)
                        alliance1.pop(temp)
                        tempAlliance1Str = ""
                        tempAlliance2Str = ""
                        for k in range (0,len(alliance1)):
                            if k<len(alliance1)-1:
                                tempAlliance1Str = tempAlliance1Str + str(alliance1[k]) + " with "
                            else:
                                tempAlliance1Str = tempAlliance1Str + str(alliance1[k])    
                        for k in range (0,len(alliance2)):
                            if k<len(alliance2)-1:
                                tempAlliance2Str = tempAlliance2Str + str(alliance2[k]) + " with "
                            else:
                                tempAlliance2Str = tempAlliance2Str + str(alliance2[k])    
                        with open("MatchesIn.csv", "a") as writefile:
                            writer = csv.writer(writefile, delimiter=",")
                            writer.writerow([str(row[0]),tempAlliance1Str,tempAlliance2Str])
                    if teamofinterest in alliance2:
                        temp = alliance2.index(teamofinterest)
                        alliance2.pop(temp)
                        tempAlliance1Str = ""
                        tempAlliance2Str = ""
                        for k in range (0,len(alliance1)):
                            if k<len(alliance1)-1:
                                tempAlliance1Str = tempAlliance1Str + str(alliance1[k]) + " with "
                            else:
                                tempAlliance1Str = tempAlliance1Str + str(alliance1[k])    
                        for k in range (0,len(alliance2)):
                            if k<len(alliance2)-1:
                                tempAlliance2Str = tempAlliance2Str + str(alliance2[k]) + " with "
                            else:
                                tempAlliance2Str = tempAlliance2Str + str(alliance2[k])
                        with open("MatchesIn.csv", "a") as writefile:
                            writer = csv.writer(writefile, delimiter=",")
                            writer.writerow([str(row[0]),tempAlliance2Str,tempAlliance1Str])

def findTeamsInLater():
    global maxMatchNumber
    for i in range(0, len(matches)):
        findTeams(matches[i-1],maxMatchNumber)
        lazyScouts(lazyScoutsTeamList,matches[i-1],matches[i])

def findTeams(minMatch,maxMatch):
    del lazyScoutsTeamList[:]
    with open('Regional.csv') as sourcefile:
        spamreader = csv.reader(sourcefile, delimiter=',')
        for row in itertools.islice(spamreader,minMatch,maxMatch):
            list(row)
            for i in range (1,len(row)-2):
                if row[i] == teamofinterest:
                    for j in range (1,len(row)-2):
                        if row[j] not in lazyScoutsTeamList:
                            lazyScoutsTeamList.append(row[j])
                        if row[j] not in teams:
                            teams.append(row[j])
                            with open("Teams.csv", "a") as writefile:
                                writer = csv.writer(writefile, delimiter=",")
                                writer.writerow([row[j]])

def lazyScouts(listOfTeams,minMatch,maxMatch):
    with open('Regional.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in itertools.islice(spamreader,minMatch,maxMatch):
            list(row)
            if teamofinterest not in row:
                for i in range (1,len(row)-2):
                    if row[i] in listOfTeams:
                        with open("MatchesToWatch.csv", "a") as writefile2:
                            writer2 = csv.writer(writefile2, delimiter=" ")
                            writer2.writerow([row[i] + " in match " + str(row[0])])


deleteOld()
printHeaders()
findMatches()
findTeamsInLater()
