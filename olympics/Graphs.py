from itertools import product

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import math
from PyQt5.QtWidgets import QMessageBox
from collections import OrderedDict
from random import randrange

data = pd.read_csv("Country medals count.csv")
dataoly = pd.read_csv("olympic_medalists.csv")
datacodes=pd.read_csv("Olympic_codes.csv")
dataath = pd.read_csv("Max_ medal_winning_cont.csv")

col = ['#f1c40f', '#9b59b6', '#0984e3', '#fd79a8', '#273c75', '#ED4C67', '#6F1E51', '#12CBC4', '#EE5A24', '#A3CB38', '#aaa69d', '#ff4d4d', '#7158e2', '#ffb8b8', '#B33771', '#e84393', '#a29bfe', '#c7ecee', '#f0932b', '#D980FA']
rndm_indx = randrange(0, len(col))

colors = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Purples, plt.cm.Oranges, plt.cm.RdPu, plt.cm.GnBu, plt.cm.PuBuGn]
rndm = randrange(0, len(colors))


def showSCntryMGraph(self,country,year,medal) :
    try:
        self.Country = country
        self.Year = int(year)
        self.medal=medal
        ml = ['Gold', 'Silver', 'Bronze']
        pos = np.arange(len(ml))
        if self.medal=="Total medals":
            datacd = datacodes[datacodes['Country'] == self.Country]['Int Olympic Committee code'].item()
            medals = dataoly[(dataoly['NOC'] == datacd) & (dataoly['Edition'] == self.Year)]['Medal'].value_counts().sort_index()
            md = medals.to_dict()
            if 'Gold' in md.keys():
                gd = md.get('Gold')
            else:
                gd = 0
            if 'Silver' in md.keys():
                sl = md.get('Silver')
            else:
                sl = 0
            if 'Bronze' in md.keys():
                bz = md.get('Bronze')
            else:
                bz = 0
            if medals.empty:
                QMessageBox.information(self, 'Message from OLYSIS', 'No medals won by ' + self.Country + ' in ' + str(self.Year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                plt.title(self.Country + "'s Medals Tally in " + str(self.Year),fontname="Browallia New" ,fontsize=24)
                plt.xlabel("Medals",fontname="Browallia New" ,fontsize=21)
                plt.ylabel("No. of medals",fontname="Browallia New" ,fontsize=21)
                plt.bar(1, gd, label='Gold',color="#FFC312")
                plt.bar(2, sl, label='Silver',color="#aaa69d")
                plt.bar(3, bz, label='Bronze',color="#b33939")
                plt.xticks(pos + 1, ml)
                plt.legend()
                plt.show()
        else:
            datacd = datacodes[datacodes['Country'] == self.Country]['Int Olympic Committee code'].item()
            count=len(dataoly.loc[(dataoly["NOC"] == datacd) & (dataoly["Edition"] == self.Year) & (dataoly["Medal"] == self.medal), ["Medal", "Edition"]])
            df = pd.DataFrame({'Medal': [self.medal], 'No. of ' + self.medal + ' Medals': [count]})
            if count==0:
                QMessageBox.information(self, 'Message from OLYSIS', 'No ' + self.medal + ' medals won by ' + self.Country + ' in ' + str(self.Year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                if self.medal=='Gold':
                    ax=df.plot(kind='bar',color="#FFC312",rot=0)
                elif self.medal=='Silver':
                    ax = df.plot(kind='bar', color="#aaa69d",rot=0)
                else:
                    ax = df.plot(kind='bar', color="#b33939",rot=0)
                ax.legend([self.medal + ' Medals'])
                ax.set_title(self.Country + "'s " + self.medal + " Medals Tally in " + str(self.Year),fontname="Browallia New" ,fontsize=24)
                ax.set_xlabel(self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_ylabel("No. of " + self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_xticklabels(self.medal)
                '''plt.title(self.Country + "'s " + self.medal + " Medals Tally in " + str(self.Year))
                plt.xlabel(self.medal + " Medals")
                plt.ylabel("No. of " + self.medal + " Medals")
                plt.savefig('output.png')'''
                plt.show()

    except BaseException as ex:
        print(ex)



def showSGndrMGraph(self,gender,year,medal) :
    try:
        self.gender = gender
        self.year = int(year)
        self.medal=medal
        ml = ['Gold', 'Silver', 'Bronze']
        pos = np.arange(len(ml))
        if self.medal=="Total medals":
            medals = dataoly[(dataoly['Gender'] == self.gender) & (dataoly['Edition'] == self.year)]['Medal'].value_counts().sort_index()
            md = medals.to_dict()
            if 'Gold' in md.keys():
                gd = md.get('Gold')
            else:
                gd = 0
            if 'Silver' in md.keys():
                sl = md.get('Silver')
            else:
                sl = 0
            if 'Bronze' in md.keys():
                bz = md.get('Bronze')
            else:
                bz = 0
            if medals.empty:
                QMessageBox.information(self, 'Message from OLYSIS', 'No medals won by ' + self.gender + ' in ' + str(self.year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                plt.title(self.gender + "'s Medals Tally in " + str(self.year),fontname="Browallia New" ,fontsize=24)
                plt.xlabel("Medals",fontname="Browallia New" ,fontsize=21)
                plt.ylabel("No. of medals",fontname="Browallia New" ,fontsize=21)
                plt.bar(1, gd, label='Gold',color="#FFC312")
                plt.bar(2, sl, label='Silver',color="#aaa69d")
                plt.bar(3, bz, label='Bronze',color="#b33939")
                plt.xticks(pos + 1, ml)
                plt.legend()
                plt.show()
        else:
            count=len(dataoly.loc[(dataoly["Gender"] == self.gender) & (dataoly["Edition"] == self.year) & (dataoly["Medal"] == self.medal), ["Medal", "Edition"]])
            df = pd.DataFrame({'Medal': [self.medal], 'No. of ' + self.medal + ' Medals': [count]})
            if count==0:
                QMessageBox.information(self, 'Message from OLYSIS', 'No ' + self.medal + ' medals won by ' + self.gender + ' in ' + str(self.year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                if self.medal=='Gold':
                    ax=df.plot(kind='bar',color="#FFC312",rot=0)
                elif self.medal=='Silver':
                    ax = df.plot(kind='bar', color="#aaa69d",rot=0)
                else:
                    ax = df.plot(kind='bar', color="#b33939",rot=0)
                ax.legend([self.medal + ' Medals'])
                ax.set_title(self.gender + "'s " + self.medal + " Medals Tally in " + str(self.year),fontname="Browallia New" ,fontsize=24)
                ax.set_xlabel(self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_ylabel("No. of " + self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_xticklabels(self.medal)
                plt.show()

    except BaseException as ex:
        print(ex)



def showSSprtMGraph(self,sport,year,medal) :
    try:
        self.sport = sport
        self.year = int(year)
        self.medal=medal
        ml = ['Gold', 'Silver', 'Bronze']
        pos = np.arange(len(ml))
        if self.medal=="Total medals":
            medals = dataoly[(dataoly['Sport'] == self.sport) & (dataoly['Edition'] == self.year)]['Medal'].value_counts().sort_index()
            md = medals.to_dict()
            if 'Gold' in md.keys():
                gd = md.get('Gold')
            else:
                gd = 0
            if 'Silver' in md.keys():
                sl = md.get('Silver')
            else:
                sl = 0
            if 'Bronze' in md.keys():
                bz = md.get('Bronze')
            else:
                bz = 0
            if medals.empty:
                QMessageBox.information(self, 'Message from OLYSIS', 'No medals won in ' + self.sport + ' in ' + str(self.year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                plt.title(self.sport + "'s Medals Tally in " + str(self.year),fontname="Browallia New" ,fontsize=24)
                plt.xlabel("Medals",fontname="Browallia New" ,fontsize=21)
                plt.ylabel("No. of medals",fontname="Browallia New" ,fontsize=21)
                plt.bar(1, gd, label='Gold',color="#FFC312")
                plt.bar(2, sl, label='Silver',color="#aaa69d")
                plt.bar(3, bz, label='Bronze',color="#b33939")
                plt.xticks(pos + 1, ml)
                plt.legend()
                plt.show()
        else:
            count=len(dataoly.loc[(dataoly["Sport"] == self.sport) & (dataoly["Edition"] == self.year) & (dataoly["Medal"] == self.medal), ["Medal", "Edition"]])
            df = pd.DataFrame({'Medal': [self.medal], 'No. of ' + self.medal + ' Medals': [count]})
            if count==0:
                QMessageBox.information(self, 'Message from OLYSIS', 'No ' + self.medal + ' medals won in ' + self.sport + ' in ' + str(self.year) + ' Olympic Games.' , QMessageBox.Ok)
            else:
                if self.medal=='Gold':
                    ax=df.plot(kind='bar',color="#FFC312",rot=0)
                elif self.medal=='Silver':
                    ax = df.plot(kind='bar', color="#aaa69d",rot=0)
                else:
                    ax = df.plot(kind='bar', color="#b33939",rot=0)
                ax.legend([self.medal + ' Medals'])
                ax.set_title(self.sport + "'s " + self.medal + " Medals Tally in " + str(self.year),fontname="Browallia New" ,fontsize=24)
                ax.set_xlabel(self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_ylabel("No. of " + self.medal + " Medals",fontname="Browallia New" ,fontsize=21)
                ax.set_xticklabels(self.medal)
                plt.show()

    except BaseException as ex:
        print(ex)





def showMCntryMGraph(self,country,medal) :
    try:
        self.country = country
        self.medal=medal
        datacd = datacodes[datacodes['Country'] == self.country]['Int Olympic Committee code'].item()
        if self.medal=="Total medals":
            medals = dataoly[dataoly['NOC'] == datacd]['Edition'].value_counts().sort_index()
        else:
            medals = dataoly[(dataoly['NOC'] == datacd) & (dataoly['Medal'] == self.medal)]['Edition'].value_counts().sort_index()
        ml = medals.to_dict()
        for i in range(1896, 2012, 4):
            if i not in ml.keys():
                ml[i] = 0
        m = OrderedDict(sorted(ml.items()))
        yr = list(m.keys())
        vl = list(m.values())
        plt.plot(yr, vl, 'o-', marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        plt.xlabel("Year", fontname="Browallia New", fontsize=21)
        if self.medal == "Total medals":
            plt.title(self.country + "'s Yearwise Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)
            plt.legend(['Total Medals'])
        else:
            plt.title(self.country + "'s Yearwise " + self.medal + " Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of " + self.medal + " medals", fontname="Browallia New", fontsize=21)
            plt.legend([self.medal+ ' Medals'])
        plt.show()

    except BaseException as ex:
        print(ex)



def showMGndrMGraph(self,gender,medal) :
    try:
        self.gender = gender
        self.medal=medal
        col = ['#f1c40f', '#9b59b6', '#0984e3', '#fd79a8', '#273c75', '#ED4C67', '#6F1E51', '#12CBC4', '#EE5A24', '#A3CB38', '#aaa69d', '#ff4d4d', '#7158e2', '#ffb8b8', '#B33771', '#e84393', '#a29bfe', '#c7ecee', '#f0932b', '#D980FA']
        rndm_indx = randrange(0, len(col))
        if self.medal=="Total medals":
            medals = dataoly[dataoly['Gender'] == self.gender]['Edition'].value_counts().sort_index()
        else:
            medals = dataoly[(dataoly['Gender'] == self.gender) & (dataoly['Medal'] == self.medal)]['Edition'].value_counts().sort_index()
        ml = medals.to_dict()
        for i in range(1896, 2012, 4):
            if i not in ml.keys():
                ml[i] = 0
        m = OrderedDict(sorted(ml.items()))
        yr = list(m.keys())
        vl = list(m.values())
        plt.plot(yr, vl, 'o-', marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        plt.xlabel("Year", fontname="Browallia New", fontsize=21)
        if self.medal == "Total medals":
            plt.title(self.gender + "'s Yearwise Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)
            plt.legend(['Total Medals'])
        else:
            plt.title(self.gender + "'s Yearwise " + self.medal + " Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of " + self.medal + " medals", fontname="Browallia New", fontsize=21)
            plt.legend([self.medal+ ' Medals'])
        plt.show()

    except BaseException as ex:
        print(ex)



def showMSprtMGraph(self,sport,medal) :
    try:
        self.sport = sport
        self.medal=medal
        col = ['#f1c40f', '#9b59b6', '#0984e3', '#fd79a8', '#273c75', '#ED4C67', '#6F1E51', '#12CBC4', '#EE5A24', '#A3CB38', '#aaa69d', '#ff4d4d', '#7158e2', '#ffb8b8', '#B33771', '#e84393', '#a29bfe', '#c7ecee', '#f0932b', '#D980FA']
        rndm_indx = randrange(0, len(col))
        if self.medal=="Total medals":
            medals = dataoly[dataoly['Sport'] == self.sport]['Edition'].value_counts().sort_index()
        else:
            medals = dataoly[(dataoly['Sport'] == self.sport) & (dataoly['Medal'] == self.medal)]['Edition'].value_counts().sort_index()
        ml = medals.to_dict()
        for i in range(1896, 2012, 4):
            if i not in ml.keys():
                ml[i] = 0
        m = OrderedDict(sorted(ml.items()))
        yr = list(m.keys())
        vl = list(m.values())
        plt.plot(yr, vl, 'o-', marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
        plt.xlabel("Year", fontname="Browallia New", fontsize=21)
        if self.medal == "Total medals":
            plt.title(self.sport + " Yearwise Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)
            plt.legend(['Total Medals'])
        else:
            plt.title(self.sport + " Yearwise " + self.medal + " Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of " + self.medal + " medals", fontname="Browallia New", fontsize=21)
            plt.legend([self.medal+ ' Medals'])
        plt.show()

    except BaseException as ex:
        print(ex)




def showTopTenMedalists(self):
    try:
        # y-axis in bold
        rc('font', weight='bold')

        ml = ['Gold', 'Silver', 'Bronze']

        dataath['Total'] = dataath['Total'].astype('str')

        gold = dataath['Golds'].head(10).values
        slvr = dataath['Silvers'].head(10).values
        brnz = dataath['Bronzes'].head(10).values

        gold = gold.tolist()

        #Replacing nan elements to 0
        sil = [0 if math.isnan(x) else x for x in slvr]
        brn = [0 if math.isnan(x) else x for x in brnz]

        #Converting list elements to int type
        silver = [int(i) for i in sil]
        bronze = [int(i) for i in brn]

        ht = list()

        #Preparing height for bronze medals
        for i in range(0, 10):
            ht.append(gold[i] + silver[i])

        names = dataath["Name"].head(10).values
        barwidth = 1
        names = names.tolist()

        r = np.arange(2, 2 * len(names) + 1, 2)
        r = r.tolist()

        # Create brown bars
        plt.bar(r, gold, color="#FFC312", edgecolor='white', width=barwidth)
        # Create green bars (middle), on top of the firs ones
        plt.bar(r, silver, bottom=gold, color="#aaa69d", edgecolor='white', width=barwidth)
        # Create green bars (top)
        plt.bar(r, bronze, bottom=ht, color="#b33939", edgecolor='white', width=barwidth)

        # Custom X axis
        plt.xticks(r, names, fontname="Browallia New", fontweight='light', fontsize=12, rotation=90)
        plt.xlabel("Names", fontname="Browallia New", fontsize=21)
        plt.ylabel("No of Medals", fontname="Browallia New", fontsize=21)
        plt.title("Top 10 Medal winning Sportspersons", fontname="Browallia New", fontsize=24)
        plt.subplots_adjust(bottom=0.30)
        plt.legend(ml)
        plt.show()

    except BaseException as ex:
        print(ex)



def showTopTenMedalCountries(self):
    try:
        # y-axis in bold
        rc('font', weight='bold')

        ml = ['Gold', 'Silver', 'Bronze']

        gld = data['Gold'].head(10).values
        slvr = data['Silver'].head(10).values
        brnz = data['Bronze'].head(10).values

        gold = [int(i) for i in gld]
        silver = [int(i) for i in slvr]
        bronze = [int(i) for i in brnz]

        ht = list()

        for i in range(0, 10):
            ht.append(gold[i] + silver[i])

        names = data["Country"].head(10).values
        barwidth = 1
        names = names.tolist()

        r = np.arange(2, 2 * len(names) + 1, 2)
        r = r.tolist()

        # Create brown bars
        plt.bar(r, gold, color="#FFC312", edgecolor='white', width=barwidth)
        # Create green bars (middle), on top of the firs ones
        plt.bar(r, silver, bottom=gold, color="#aaa69d", edgecolor='white', width=barwidth)
        # Create green bars (top)
        plt.bar(r, bronze, bottom=ht, color="#b33939", edgecolor='white', width=barwidth)

        # Custom X axis
        plt.xticks(r, names, fontname="Browallia New", fontweight='light', fontsize=14, rotation=90)
        plt.xlabel("Countries", fontname="Browallia New", fontsize=21)
        plt.ylabel("No of Medals", fontname="Browallia New", fontsize=21)
        plt.title("Top 10 Medal winning Countries", fontname="Browallia New", fontsize=24)
        plt.subplots_adjust(bottom=0.18)
        plt.legend(ml)
        plt.show()

    except BaseException as ex:
        print(ex)



def cmpSCntryGraph(self,country1,country2,year):
    try:
        self.country1=country1
        self.country2=country2
        self.year=int(year)
        ml = ['Gold', 'Silver', 'Bronze']
        datacd1 = datacodes[datacodes['Country'] == self.country1]['Int Olympic Committee code'].item()
        datacd2 = datacodes[datacodes['Country'] == self.country2]['Int Olympic Committee code'].item()
        medals1 = dataoly[(dataoly['NOC'] == datacd1) & (dataoly['Edition'] == self.year)]['Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['NOC'] == datacd2) & (dataoly['Edition'] == self.year)]['Medal'].value_counts().sort_index()
        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [country1, country2])

        plt.title(self.country1 + " VS " + self.country2 + " Medals Tally comparison in " + str(self.year) + " Olympics", fontname="Browallia New",fontsize=20)
        plt.xlabel("Country", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend(ml)
        plt.show()

    except BaseException as ex:
        print(ex)


def cmpMCntryGraph(self,country,year1,year2):
    try:
        self.country=country
        self.year1=int(year1)
        self.year2=int(year2)

        # y-axis in bold
        rc('font', weight='bold')

        ml = ['Gold', 'Silver', 'Bronze']

        datacd = datacodes[datacodes['Country'] == self.country]['Int Olympic Committee code'].item()
        medals1 = dataoly[(dataoly['NOC'] == datacd) & (dataoly['Edition'] == self.year1)][
            'Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['NOC'] == datacd) & (dataoly['Edition'] == self.year2)][
            'Medal'].value_counts().sort_index()

        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        ht = list()

        # Preparing height for bronze medals
        for i in range(2):
            ht.append(gold[i] + silver[i])

        names = [self.year1, self.year2]
        barwidth = 1

        r = np.arange(2, 2 * len(names) + 1, 2)
        r = r.tolist()

        # Create brown bars
        plt.bar(r, gold, color="#FFC312", edgecolor='white', width=barwidth)
        # Create green bars (middle), on top of the firs ones
        plt.bar(r, silver, bottom=gold, color="#aaa69d", edgecolor='white', width=barwidth)
        # Create green bars (top)
        plt.bar(r, bronze, bottom=ht, color="#b33939", edgecolor='white', width=barwidth)

        # Custom X axis
        plt.xticks(r, names, fontname="Browallia New", fontsize=16, rotation=0)
        plt.xlabel("Years", fontname="Browallia New", fontsize=21)
        plt.ylabel("No of Medals", fontname="Browallia New", fontsize=21)
        plt.title(self.country + "'s Medals Tally Comparison in " + str(self.year1) + " VS " + str(self.year2),
                  fontname="Browallia New", fontsize=24)
        # plt.subplots_adjust(bottom=0.30)
        plt.legend(ml,loc='upper center')
        plt.show()

    except BaseException as ex:
        print(ex)



def cmpOCntryGraph(self,country1,country2):
    try:
        self.country1=country1
        self.country2 = country2

        datacd1 = datacodes[datacodes['Country'] == self.country1]['Int Olympic Committee code'].item()
        datacd2 = datacodes[datacodes['Country'] == self.country2]['Int Olympic Committee code'].item()
        medals1 = dataoly[dataoly['NOC'] == datacd1]['Medal'].value_counts().sort_index()
        medals2 = dataoly[dataoly['NOC'] == datacd2]['Medal'].value_counts().sort_index()

        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        ml = ['Gold', 'Silver', 'Bronze']

        '''mdls1 = list()
        mdls2 = list()
        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            mdls1.append(gd1)
        else:
            gd1 = 0
            mdls1.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            mdls1.append(sl1)
        else:
            sl1 = 0
            mdls1.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            mdls1.append(bz1)
        else:
            bz1 = 0
            mdls1.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            mdls2.append(gd2)
        else:
            gd2 = 0
            mdls2.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            mdls2.append(sl2)
        else:
            sl2 = 0
            mdls2.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            mdls2.append(bz2)
        else:
            bz2 = 0
            mdls2.append(bz2)

        mdls = list()
        sum1 = 0
        sum2 = 0
        for i in range(3):
            mdls.append(mdls1[i])
            sum1 += mdls1[i]
        for i in range(3):
            mdls.append(mdls2[i])
            sum2 += mdls2[i]

        group_names = [self.country1, self.country2]
        group_size = [sum1, sum2]
        subgroup_names = ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze']
        subgroup_size = mdls

        # Create colors
        a, b = [plt.cm.Blues, plt.cm.Reds]

        # First Ring (outside)
        fig, ax = plt.subplots()
        ax.axis('equal')
        mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6)])
        plt.setp(mypie, width=0.3, edgecolor='white')

        # Second Ring (Inside)
        mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                           colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3)])
        plt.setp(mypie2, width=0.4, edgecolor='white')
        plt.margins(0, 0)

        plt.title(self.country1 + " VS " + self.country2 + " Overall Medals Tally comparison in Olympics\n\n",fontname="Browallia New", fontsize=20,y=1.08)
        plt.subplots_adjust(top=0.78)

        # show it
        plt.show()'''

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [country1, country2])

        plt.title(
            self.country1 + " VS " + self.country2 + " Overall Medals Tally comparison in Olympics",
            fontname="Browallia New", fontsize=20)
        plt.xlabel("Country", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend(ml)
        plt.show()


    except BaseException as ex:
        print(ex)


def cmpSGndrGraph(self,year):
    try:
        self.year=int(year)
        gender1 = "Men"
        gender2 = "Women"
        medals1 = dataoly[(dataoly['Gender'] == gender1) & (dataoly['Edition'] == self.year)][
            'Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['Gender'] == gender2) & (dataoly['Edition'] == self.year)][
            'Medal'].value_counts().sort_index()
        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white', label='Gold')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white', label='Silver')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white', label='Bronze')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [gender1, gender2])

        plt.title(gender1 + " VS " + gender2 + " Medals Tally comparison in " + str(self.year) + " Olympics", fontname="Browallia New",fontsize=20)
        plt.xlabel("Gender", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend()
        plt.show()

    except BaseException as ex:
        print(ex)


def cmpMGndrGraph(self,gender,year1,year2):
    try:
        self.gender = gender
        self.year1 = int(year1)
        self.year2 = int(year2)

        # y-axis in bold
        rc('font', weight='bold')

        ml = ['Gold', 'Silver', 'Bronze']

        medals1 = dataoly[(dataoly['Gender'] == self.gender) & (dataoly['Edition'] == self.year1)][
            'Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['Gender'] == self.gender) & (dataoly['Edition'] == self.year2)][
            'Medal'].value_counts().sort_index()

        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        ht = list()

        # Preparing height for bronze medals
        for i in range(2):
            ht.append(gold[i] + silver[i])

        names = [self.year1, self.year2]
        barwidth = 1

        r = np.arange(2, 2 * len(names) + 1, 2)
        r = r.tolist()

        # Create brown bars
        plt.bar(r, gold, color="#FFC312", edgecolor='white', width=barwidth)
        # Create green bars (middle), on top of the firs ones
        plt.bar(r, silver, bottom=gold, color="#aaa69d", edgecolor='white', width=barwidth)
        # Create green bars (top)
        plt.bar(r, bronze, bottom=ht, color="#b33939", edgecolor='white', width=barwidth)

        # Custom X axis
        plt.xticks(r, names, fontname="Browallia New", fontsize=16, rotation=0)
        plt.xlabel("Years", fontname="Browallia New", fontsize=21)
        plt.ylabel("No of Medals", fontname="Browallia New", fontsize=21)
        plt.title(self.gender + "'s Medals Tally Comparison in " + str(self.year1) + " VS " + str(self.year2),
                  fontname="Browallia New", fontsize=24)
        # plt.subplots_adjust(bottom=0.30)
        plt.legend(ml,loc='upper center')
        plt.show()

    except BaseException as ex:
        print(ex)



def cmpOGndrGraph(self):
    try:
        gender1 = "Men"
        gender2 = "Women"
        medals1 = dataoly[dataoly['Gender'] == gender1]['Medal'].value_counts().sort_index()
        medals2 = dataoly[dataoly['Gender'] == gender2]['Medal'].value_counts().sort_index()
        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        mdls1 = list()
        mdls2 = list()
        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            mdls1.append(gd1)
        else:
            gd1 = 0
            mdls1.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            mdls1.append(sl1)
        else:
            sl1 = 0
            mdls1.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            mdls1.append(bz1)
        else:
            bz1 = 0
            mdls1.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            mdls2.append(gd2)
        else:
            gd2 = 0
            mdls2.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            mdls2.append(sl2)
        else:
            sl2 = 0
            mdls2.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            mdls2.append(bz2)
        else:
            bz2 = 0
            mdls2.append(bz2)

        mdls = list()
        sum1 = 0
        sum2 = 0
        for i in range(3):
            mdls.append(mdls1[i])
            sum1 += mdls1[i]
        for i in range(3):
            mdls.append(mdls2[i])
            sum2 += mdls2[i]

        group_names = [gender1, gender2]
        group_size = [sum1, sum2]
        subgroup_names = ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze']
        subgroup_size = mdls

        # Create colors
        a, b = [plt.cm.Blues, plt.cm.Reds]

        # First Ring (outside)
        fig, ax = plt.subplots()
        ax.axis('equal')
        mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6)])
        plt.setp(mypie, width=0.3, edgecolor='white')

        # Second Ring (Inside)
        mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                           colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3)])
        plt.setp(mypie2, width=0.4, edgecolor='white')
        plt.margins(0, 0)

        plt.title(gender1 + " VS " + gender2 + " Overall Medals Tally comparison in Olympics\n\n",
                  fontname="Browallia New", fontsize=20, y=1.08)
        plt.subplots_adjust(top=0.78)

        # show it
        plt.show()


        '''gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white', label='Gold')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white', label='Silver')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white', label='Bronze')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [gender1, gender2])

        plt.title(gender1 + " VS " + gender2 + " Overall Medals Tally comparison in Olympics", fontname="Browallia New",fontsize=20)
        plt.xlabel("Gender", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend()
        plt.show()'''

    except BaseException as ex:
        print(ex)


def cmpSSprtGraph(self,sport1,sport2,year):
    try:
        self.sport1=sport1
        self.sport2 = sport2
        self.year=int(year)
        medals1 = dataoly[(dataoly['Sport'] == self.sport1) & (dataoly['Edition'] == self.year)][
            'Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['Sport'] == self.sport2) & (dataoly['Edition'] == self.year)][
            'Medal'].value_counts().sort_index()
        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white', label='Gold')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white', label='Silver')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white', label='Bronze')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [self.sport1, self.sport2])

        plt.title(self.sport1 + " VS " + self.sport2 + " Medals Tally comparison in " + str(self.year) + " Olympics", fontname="Browallia New",
                  fontsize=20)
        plt.xlabel("Sport", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend()
        plt.show()

    except BaseException as ex:
        print(ex)


def cmpMSprtGraph(self,sport,year1,year2):
    try:
        self.sport = sport
        self.year1 = int(year1)
        self.year2 = int(year2)

        # y-axis in bold
        rc('font', weight='bold')

        ml = ['Gold', 'Silver', 'Bronze']

        medals1 = dataoly[(dataoly['Sport'] == self.sport) & (dataoly['Edition'] == self.year1)][
            'Medal'].value_counts().sort_index()
        medals2 = dataoly[(dataoly['Sport'] == self.sport) & (dataoly['Edition'] == self.year2)][
            'Medal'].value_counts().sort_index()

        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        ht = list()

        # Preparing height for bronze medals
        for i in range(2):
            ht.append(gold[i] + silver[i])

        names = [self.year1, self.year2]
        barwidth = 1

        r = np.arange(2, 2 * len(names) + 1, 2)
        r = r.tolist()

        # Create brown bars
        plt.bar(r, gold, color="#FFC312", edgecolor='white', width=barwidth)
        # Create green bars (middle), on top of the firs ones
        plt.bar(r, silver, bottom=gold, color="#aaa69d", edgecolor='white', width=barwidth)
        # Create green bars (top)
        plt.bar(r, bronze, bottom=ht, color="#b33939", edgecolor='white', width=barwidth)

        # Custom X axis
        plt.xticks(r, names, fontname="Browallia New", fontsize=16, rotation=0)
        plt.xlabel("Years", fontname="Browallia New", fontsize=21)
        plt.ylabel("No of Medals", fontname="Browallia New", fontsize=21)
        plt.title(self.sport + "'s Medals Tally Comparison in " + str(self.year1) + " VS " + str(self.year2),
                  fontname="Browallia New", fontsize=24)
        # plt.subplots_adjust(bottom=0.30)
        plt.legend(ml,loc='upper center')
        plt.show()

    except BaseException as ex:
        print(ex)



def cmpOSprtGraph(self,sport1,sport2):
    try:
        self.sport1=sport1
        self.sport2 = sport2
        medals1 = dataoly[dataoly['Sport'] == self.sport1]['Medal'].value_counts().sort_index()
        medals2 = dataoly[dataoly['Sport'] == self.sport2]['Medal'].value_counts().sort_index()
        md1 = medals1.to_dict()
        md2 = medals2.to_dict()

        mdls1 = list()
        mdls2 = list()
        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            mdls1.append(gd1)
        else:
            gd1 = 0
            mdls1.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            mdls1.append(sl1)
        else:
            sl1 = 0
            mdls1.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            mdls1.append(bz1)
        else:
            bz1 = 0
            mdls1.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            mdls2.append(gd2)
        else:
            gd2 = 0
            mdls2.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            mdls2.append(sl2)
        else:
            sl2 = 0
            mdls2.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            mdls2.append(bz2)
        else:
            bz2 = 0
            mdls2.append(bz2)

        mdls = list()
        sum1 = 0
        sum2 = 0
        for i in range(3):
            mdls.append(mdls1[i])
            sum1 += mdls1[i]
        for i in range(3):
            mdls.append(mdls2[i])
            sum2 += mdls2[i]

        group_names = [self.sport1, self.sport2]
        group_size = [sum1, sum2]
        subgroup_names = ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze']
        subgroup_size = mdls

        # Create colors
        a, b = [plt.cm.RdPu, plt.cm.Purples]

        # First Ring (outside)
        fig, ax = plt.subplots()
        ax.axis('equal')
        mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6)])
        plt.setp(mypie, width=0.3, edgecolor='white')

        # Second Ring (Inside)
        mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                           colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), b(0.3)])
        plt.setp(mypie2, width=0.4, edgecolor='white')
        plt.margins(0, 0)

        plt.title(self.sport1 + " VS " + self.sport2 + " Overall Medals Tally comparison in Olympics\n\n",
                  fontname="Browallia New", fontsize=20, y=1.08)
        plt.subplots_adjust(top=0.78)

        # show it
        plt.show()

        '''gold = list()
        silver = list()
        bronze = list()

        if 'Gold' in md1.keys():
            gd1 = md1.get('Gold')
            gold.append(gd1)
        else:
            gd1 = 0
            gold.append(gd1)

        if 'Silver' in md1.keys():
            sl1 = md1.get('Silver')
            silver.append(sl1)
        else:
            sl1 = 0
            silver.append(sl1)

        if 'Bronze' in md1.keys():
            bz1 = md1.get('Bronze')
            bronze.append(bz1)
        else:
            bz1 = 0
            bronze.append(bz1)

        if 'Gold' in md2.keys():
            gd2 = md2.get('Gold')
            gold.append(gd2)
        else:
            gd2 = 0
            gold.append(gd2)

        if 'Silver' in md2.keys():
            sl2 = md2.get('Silver')
            silver.append(sl2)
        else:
            sl2 = 0
            silver.append(sl2)

        if 'Bronze' in md2.keys():
            bz2 = md2.get('Bronze')
            bronze.append(bz2)
        else:
            bz2 = 0
            bronze.append(bz2)

        barwidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(gold))
        r2 = [x + barwidth for x in r1]
        r3 = [x + barwidth for x in r2]

        # Make the plot
        plt.bar(r1, gold, color="#FFC312", width=barwidth, edgecolor='white', label='Gold')
        plt.bar(r2, silver, color="#aaa69d", width=barwidth, edgecolor='white', label='Silver')
        plt.bar(r3, bronze, color="#b33939", width=barwidth, edgecolor='white', label='Bronze')

        # Add xticks on the middle of the group bars
        plt.xticks([r + barwidth for r in range(len(gold))], [self.sport1, self.sport2])

        plt.title(self.sport1 + " VS " + self.sport2 + " Overall Medals Tally comparison in Olympics", fontname="Browallia New",
                  fontsize=20)
        plt.xlabel("Sport", fontname="Browallia New", fontsize=21)
        plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)

        # Create legend & Show graphic
        plt.legend()
        plt.show()'''

    except BaseException as ex:
        print(ex)



def otherCountGraph(self,count,med):
    try:
        self.country=count
        self.medal=med
        datacd = list()
        m1 = dict()
        m2 = dict()
        m3 = dict()
        m4 = dict()
        # medals={country[0]:[],country[1]:[],country[2]:[]}
        # medals=list()
        for i in range(len(self.country)):
            datacd.append(datacodes[datacodes['Country'] == self.country[i]]['Int Olympic Committee code'].item())
        # print(datacd)
        if self.medal == "Total medals":
            for i in range(len(self.country)):
                # medals[country[i]].append(dataoly[dataoly['NOC'] == datacd[i]]['Edition'].value_counts().sort_index())
                medals = dataoly[dataoly['NOC'] == datacd[i]]['Edition'].value_counts().sort_index()
                if i == 0:
                    m1 = medals.to_dict()
                elif i == 1:
                    m2 = medals.to_dict()
                elif i == 2:
                    m3 = medals.to_dict()
                else:
                    m4 = medals.to_dict()


        else:
            for i in range(len(self.country)):
                # medals[country[i]].append(dataoly[(dataoly['NOC'] == datacd[i]) & (dataoly['Medal'] == medal)]['Edition'].value_counts().sort_index())
                medals = dataoly[(dataoly['NOC'] == datacd[i]) & (dataoly['Medal'] == self.medal)][
                    'Edition'].value_counts().sort_index()
                if i == 0:
                    m1 = medals.to_dict()
                elif i == 1:
                    m2 = medals.to_dict()
                elif i == 2:
                    m3 = medals.to_dict()
                else:
                    m4 = medals.to_dict()

        for i in range(1896, 2012, 4):
            if i not in m1.keys():
                m1[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m2.keys():
                m2[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m3.keys():
                m3[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m4.keys():
                m4[i] = 0

        med1 = OrderedDict(sorted(m1.items()))
        med2 = OrderedDict(sorted(m2.items()))
        med3 = OrderedDict(sorted(m3.items()))
        med4 = OrderedDict(sorted(m4.items()))

        yr1 = list(med1.keys())
        vl1 = list(med1.values())

        yr2 = list(med2.keys())
        vl2 = list(med2.values())

        yr3 = list(med3.keys())
        vl3 = list(med3.values())

        yr4 = list(med4.keys())
        vl4 = list(med4.values())

        plt.style.use('seaborn-darkgrid')

        plt.plot(yr1, vl1, 'o-', marker='o', markerfacecolor='blue', color='skyblue', linewidth=2, label=self.country[0])
        plt.plot(yr2, vl2, 'o:', markerfacecolor='#fd9644', color='#fed330', linewidth=2, label=self.country[1])
        plt.plot(yr3, vl3, '-.o', markerfacecolor='#1dd1a1', color='#7bed9f', linewidth=2, label=self.country[2])
        plt.plot(yr4, vl4, 'o--', markerfacecolor='#ff3838', color='#f78fb3', linewidth=2, label=self.country[3])
        plt.xlabel("Year", fontname="Browallia New", fontsize=21)
        if self.medal == "Total medals":
            plt.title("Various Countries Yearwise Overall Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)
        else:
            plt.title("Various Countries Yearwise " + self.medal + " Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of " + self.medal + " medals", fontname="Browallia New", fontsize=21)
        plt.legend()
        plt.show()

    except BaseException as ex:
        print(ex)



def otherSportsGraph(self, sprt,med):
    try:
        self.sports = sprt
        self.medal = med
        datacd = list()
        m1 = dict()
        m2 = dict()
        m3 = dict()
        m4 = dict()
        # medals={country[0]:[],country[1]:[],country[2]:[]}
        # medals=list()
        if self.medal == "Total medals":
            for i in range(len(self.sports)):
                # medals[country[i]].append(dataoly[dataoly['NOC'] == datacd[i]]['Edition'].value_counts().sort_index())
                medals = dataoly[dataoly['Sport'] == self.sports[i]]['Edition'].value_counts().sort_index()
                if i == 0:
                    m1 = medals.to_dict()
                elif i == 1:
                    m2 = medals.to_dict()
                elif i == 2:
                    m3 = medals.to_dict()
                else:
                    m4 = medals.to_dict()


        else:
            for i in range(len(self.sports)):
                # medals[country[i]].append(dataoly[(dataoly['NOC'] == datacd[i]) & (dataoly['Medal'] == medal)]['Edition'].value_counts().sort_index())
                medals = dataoly[(dataoly['Sport'] == self.sports[i]) & (dataoly['Medal'] == self.medal)][
                    'Edition'].value_counts().sort_index()
                if i == 0:
                    m1 = medals.to_dict()
                elif i == 1:
                    m2 = medals.to_dict()
                elif i == 2:
                    m3 = medals.to_dict()
                else:
                    m4 = medals.to_dict()

        for i in range(1896, 2012, 4):
            if i not in m1.keys():
                m1[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m2.keys():
                m2[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m3.keys():
                m3[i] = 0

        for i in range(1896, 2012, 4):
            if i not in m4.keys():
                m4[i] = 0

        med1 = OrderedDict(sorted(m1.items()))
        med2 = OrderedDict(sorted(m2.items()))
        med3 = OrderedDict(sorted(m3.items()))
        med4 = OrderedDict(sorted(m4.items()))

        yr1 = list(med1.keys())
        vl1 = list(med1.values())

        yr2 = list(med2.keys())
        vl2 = list(med2.values())

        yr3 = list(med3.keys())
        vl3 = list(med3.values())

        yr4 = list(med4.keys())
        vl4 = list(med4.values())

        plt.style.use('seaborn-darkgrid')

        plt.plot(yr1, vl1, 'o-', marker='o', markerfacecolor='blue', color='skyblue', linewidth=2, label=self.sports[0])
        plt.plot(yr2, vl2, 'o:', markerfacecolor='#fd9644', color='#fed330', linewidth=2, label=self.sports[1])
        plt.plot(yr3, vl3, '-.o', markerfacecolor='#1dd1a1', color='#7bed9f', linewidth=2, label=self.sports[2])
        plt.plot(yr4, vl4, 'o--', markerfacecolor='#ff3838', color='#f78fb3', linewidth=2, label=self.sports[3])
        plt.xlabel("Year", fontname="Browallia New", fontsize=21)
        if self.medal == "Total medals":
            plt.title("Various Sports Yearwise Overall Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of medals", fontname="Browallia New", fontsize=21)
        else:
            plt.title("Various Sports Yearwise " + self.medal + " Medals Tally", fontname="Browallia New", fontsize=24)
            plt.ylabel("No. of " + self.medal + " medals", fontname="Browallia New", fontsize=21)
        plt.legend()
        plt.show()

    except BaseException as ex:
        print(ex)