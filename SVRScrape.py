import csv

teamofinterest = "613"
#Be sure to save as a windows csv

writer = csv.writer(open("MatchesIn.csv", "a"))
writer2 = csv.writer(open("TeamsInMatches.csv", "a"))
teams = []

def findTeams():
    with open('Regional.csv') as csvfile2:
        spamreader = csv.reader(csvfile2, delimiter=',')
        for row in spamreader:
            list(row)
            for i in range (0,len(row)):
                if row[i] == teamofinterest:
                    for i in range (1,len(row)-2):
                        #print row[i]
                        if row[i] not in teams:
                            teams.append(row[i])
        writer.writerow(list(teams))

def lazyScouts():
    with open('Regional.csv') as csvfile2:
        spamreader = csv.reader(csvfile2, delimiter=',')
        for row in spamreader:
            list(row)
            for i in range (0,len(teams)):
                #print teams[i]
                for j in range (1,len(row)-2):
                    if row[j] == teams[i]:
                        #print row[j]
                        print (teams[i] + " in match " + row[0])
                        writer2.writerow(str(teams[i]) + " in match " + str(row[0]))
                        #if row[0] not in matches:
                           # matches.append(row[0])
                            #print matches
           # writer.writerow(list(matches))

findTeams()
lazyScouts()

