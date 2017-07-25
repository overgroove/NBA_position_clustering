import pandas as pd
import numpy as np
import os

year1 = ["1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
         "2011", "2012", "2013", "2014", "2015", "2016" ]
year2 = ["97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17" ]

season = []
for i in range(21):
    season.append(year1[i] + "-" + year2[i])

def mergeData(season):
    df = []
    kind = ["traditional", "advanced", "defense", "misc", "usage"]
    for i in kind:
        temp = pd.read_csv(season + i + ".csv")
        temp = temp.iloc[:, 1:]

        if i == "traditional":
            del temp["STL"]
            del temp["BLK"]
            del temp["PF"]
        elif i == "advanced":
            del temp["MIN"]
        elif i == "defense":
            del temp["%DREB"]
            del temp["DREB%"]
            del temp["DREB"]
            del temp["BLK"]
            del temp["MIN"]
        elif i == "misc":
            del temp["MIN"]
        elif i == "usage":
            del temp["%BLK"]
            del temp["USG%"]
            del temp["MIN"]

        df.append(temp)

    df[2].rename(columns={"Player": "PLAYER"}, inplace=True)
    df[3].rename(columns={"Player": "PLAYER"}, inplace=True)
    df[4].rename(columns={"Player": "PLAYER"}, inplace=True)

    data = df[0]
    for i in [1, 2, 3, 4]:
        data = pd.merge(data, df[i], on=["PLAYER", "TEAM", "AGE", "GP", "W", "L"])

    data.columns = [u'PLAYER', u'TEAM', u'AGE', u'GP', u'W', u'L', u'MIN', u'PTS', u'FGM',
                    u'FGA', u'FG%', u'3PM', u'3PA', u'3P%', u'FTM', u'FTA', u'FT%', u'OREB',
                    u'DREB', u'REB', u'AST', u'TOV', u'DD2', u'TD3', u'+/-', u'OFFRTG',
                    u'DEFRTG', u'NETRTG', u'AST%', u'AST/TO', u'AST Ratio', u'OREB%',
                    u'DREB%', u'REB%', u'TO Ratio', u'eFG%', u'TS%', u'USG%', u'PACE',
                    u'PIE', u'DEF RTG', u'STL', u'STL%', u'%BLK', u'OPP PTSOFF TOV',
                    u'OPP PTS2ND CHANCE', u'OPP PTSFB', u'OPP PTSPAINT', u'DEFWS',
                    u'PTSOFF TO', u'2ndPTS', u'FBPs', u'PITP', u'OppPTS OFF TO',
                    u'Opp2nd PTS', u'OppFBPs', u'OppPITP', u'BLK', u'BLKA', u'PF', u'PFD',
                    u'%FGM', u'%FGA', u'%3PM', u'%3PA', u'%FTM', u'%FTA', u'%OREB',
                    u'%DREB', u'%REB', u'%AST', u'%TOV', u'%STL', u'%BLKA', u'%PF', u'%PFD',
                    u'%PTS']

    col = ["PLAYER", "TEAM", "AGE", "GP", "W", "L", "MIN", "PTS", "%PTS", 'FGM', "%FGM", 'FGA', "%FGA", 'FG%',
           '3PM', "%3PM", '3PA', "%3PA", '3P%', 'FTM', "%FTM", 'FTA', "%FTA", 'FT%', "eFG%", "TS%",
           'OREB', 'OREB%', '%OREB', 'DREB', 'DREB%', '%DREB', 'REB', 'REB%', "%REB",
           "AST", "AST%", "%AST", "AST/TO", 'AST Ratio', "TOV", "%TOV", "STL", "STL%", "%STL",
           "BLK", "%BLK", "BLKA", "%BLKA", "PF", "%PF", "PFD", "%PFD",
           'DD2', 'TD3', '+/-', 'OFFRTG', 'DEFRTG', 'NETRTG', 'TO Ratio', 'USG%', 'PACE', 'PIE',
           'OPP PTSOFF TOV', 'OPP PTS2ND CHANCE', 'OPP PTSFB', 'OPP PTSPAINT', 'DEFWS',
           'PTSOFF TO', '2ndPTS', 'FBPs', 'PITP', 'OppPTS OFF TO', 'Opp2nd PTS', 'OppFBPs', 'OppPITP']

    data = data[col]

    print("----------------------------------------------")
    print("      merge " + season + " data complete !    ")
    print("               ", data.shape, "               ")
    print("----------------------------------------------")

    os.chdir(os.getcwd()+"/mergedata")
    data.to_csv(season + ".csv")


pwd = os.getcwd()
for i in season:
    mergeData(i)
    os.chdir(pwd)