import csv

teamofinterest = "613"
#Be sure to save as a windows csv

teams = []

def findTeams():
    with open('Regional.csv') as csvfile2:
        spamreader = csv.reader(csvfile2, delimiter=',')
        for row in spamreader:
            list(row)
            for i in range (0,len(row)):
                if row[i] == teamofinterest:
                    for i in range (1,len(row)-2):
                        if row[i] not in teams:
                            teams.append(row[i])
                            with open("Teams.csv", "a") as writefile:
                                writer = csv.writer(writefile, delimiter=",")
                                writer.writerow([row[i]])       

def lazyScouts():
    with open('Regional.csv') as csvfile2:
        spamreader = csv.reader(csvfile2, delimiter=',')
        for row in spamreader:
            list(row)
            for i in range (0,len(teams)):
                for j in range (1,len(row)-2):
                    if row[j] == teams[i]:
                        with open("MatchesToWatch.csv", "a") as writefile2:
                            writer2 = csv.writer(writefile2, delimiter=" ")
                            writer2.writerow([str(teams[i]) + " in match " + str(row[0])])

findTeams()
lazyScouts()

