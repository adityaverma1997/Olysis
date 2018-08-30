import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Country medals count.csv")
dataoly = pd.read_csv("olympic_medalists.csv")
datacodes=pd.read_csv("Olympic_codes.csv")

def showSCntryMGraph(self,country,year) :
    try:
        self.Country = country
        self.Year = int(year)
        result = ""
        datacd = datacodes[datacodes['Country'] == self.Country]['Int Olympic Committee code'].item()
        medals=dataoly[(dataoly['NOC'] == datacd) & (dataoly['Edition'] == self.Year)]['Medal'].value_counts().sort_index()
        md = medals.to_dict()
        if medals.empty:
            gold = 0
            silver = 0
            bronze = 0
            total = 0
        else:
            if 'Gold' in md.keys():
                gold = md.get('Gold')
            else:
                gold = 0
            if 'Silver' in md.keys():
                silver = md.get('Silver')
            else:
                silver = 0
            if 'Bronze' in md.keys():
                bronze = md.get('Bronze')
            else:
                bronze = 0
            total = gold + silver + bronze
        result += "Medals won by " + self.Country + " in the year " + str(self.Year) + " are : \n\n"
        result += "Gold medals : " + str(gold) + "\n"
        result += "Silver medals : " + str(silver) + "\n"
        result += "Bronze medals : " + str(bronze) + "\n\n"
        result += "Total medals won by " + self.Country + " in the year " + str(self.Year) + " are : " + str(total) + "\n"
        return result
    except BaseException as ex:
        print(ex)



def showSGndrMGraph(self,gender,year) :
    try:
        self.Gender = gender
        self.Year = int(year)
        result = ""
        medals = dataoly[(dataoly['Gender'] == self.Gender) & (dataoly['Edition'] == self.Year)]['Medal'].value_counts().sort_index()
        md = medals.to_dict()
        if medals.empty:
            gold = 0
            silver = 0
            bronze = 0
            total = 0
        else:
            if 'Gold' in md.keys():
                gold = md.get('Gold')
            else:
                gold = 0
            if 'Silver' in md.keys():
                silver = md.get('Silver')
            else:
                silver = 0
            if 'Bronze' in md.keys():
                bronze = md.get('Bronze')
            else:
                bronze = 0
            total = gold + silver + bronze
        result += "Medals won by " + self.Gender + " in the year " + str(self.Year) + " are : \n\n"
        result += "Gold medals : " + str(gold) + "\n"
        result += "Silver medals : " + str(silver) + "\n"
        result += "Bronze medals : " + str(bronze) + "\n\n"
        result += "Total medals won by " + self.Gender + " in the year " + str(self.Year) + " are : " + str(total) + "\n"
        return result
    except BaseException as ex:
        print(ex)



def showSSprtMGraph(self,sport,year) :
    try:
        self.Sport = sport
        self.Year = int(year)
        result = ""
        medals = dataoly[(dataoly['Sport'] == self.Sport) & (dataoly['Edition'] == self.Year)]['Medal'].value_counts().sort_index()
        md = medals.to_dict()
        if medals.empty:
            gold = 0
            silver = 0
            bronze = 0
            total = 0
        else:
            if 'Gold' in md.keys():
                gold = md.get('Gold')
            else:
                gold = 0
            if 'Silver' in md.keys():
                silver = md.get('Silver')
            else:
                silver = 0
            if 'Bronze' in md.keys():
                bronze = md.get('Bronze')
            else:
                bronze = 0
            total = gold + silver + bronze
        result += "Medals won in " + self.Sport + " in the year " + str(self.Year) + " are : \n\n"
        result += "Gold medals : " + str(gold) + "\n"
        result += "Silver medals : " + str(silver) + "\n"
        result += "Bronze medals : " + str(bronze) + "\n\n"
        result += "Total medals won in " + self.Sport + " in the year " + str(self.Year) + " are : " + str(total) + "\n"
        return result
    except BaseException as ex:
        print(ex)