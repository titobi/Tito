# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
 #reading the .csv file
df = pd.read_csv("cause_of_deaths.csv")

 
data = df[['Country/Territory', 'Year', 'Malaria', 'HIV/AIDS', 'Self-harm', 'Road Injuries']]
print(data)

#plotting a bar chart to show the number of people that have died from malaria, HIV/AIDS, Self harm and road injuries from 1990 to 2019

summary = [df['Malaria'].sum(), df['HIV/AIDS'].sum(), df['Self-harm'].sum(), df['Road Injuries'].sum()] #Doingasum total of the columns
summary_table = pd.DataFrame(summary, ['Malaria', 'HIV/AIDS', 'Self-harm', 'Road Injuries'], columns = ['Sum'])
print(summary_table)

plt.bar(summary_table.index, summary_table['Sum'])

def bar_chart(x_axis, list, title):
    plt.figure(figsize=(12,5))
    plt.bar(x_axis, list)
    plt.title(title, fontsize= 9)
    plt.show()
    return

x_axis = summary_table.index
my_list = summary_table['Sum']
title = 'A Bar Chart showing the total number of people that have died from malaria, HIV?AIDS, Self harm and road injuries in the from 1990 to 2019'

bar_chart(x_axis, my_list, title)

 "As we can see from the bar chart above, Hiv/Aids and road injuries were the highest causes of death all around the world from 1990 to 2019.\n",

#plotting a line graph to show the number of people that have died from malaria, HIV/AIDS, Self harm and road injuries from 1990 to 2019

year_group = data.groupby('Year')[['Malaria', 'HIV/AIDS', 'Self-harm', 'Road Injuries']].sum()
plt.figure()
plt.plot(year_group.index, year_group['Malaria'], label='Malaria')
plt.plot(year_group.index, year_group['HIV/AIDS'], label='HIV/AIDS')
plt.plot(year_group.index, year_group['Self-harm'], label='Self-harm')
plt.plot(year_group.index, year_group['Road Injuries'], label='Road Injuries')
plt.legend()

plt.show()

def line_plot(x_axis, my_list,xticks, label_name, title):
    plt.figure(figsize=(12,5))
    for i in range(len(my_list)):
        plt.plot(x_axis,my_list[i], label=label_name[i])   
        plt.legend()
        plt.xticks()
        plt.title(title, fontsize=8)
    plt.show()

x_axis = year_group.index
my_list = [year_group['Malaria'], year_group['HIV/AIDS'], year_group['Self-harm'], year_group['Road Injuries']]
xticks = ['1990', '1995', '2000', '2005', '2010', '2015', '2019']
label = ['Malaria', 'HIV/AIDS', 'Self-harm', 'Road Injuries']
title = 'A line plot showing the total number of people that have died from malaria, HIV/AIDS, Self harm and road injuries from 1990 to 2019'
 
line_plot(x_axis, my_list, xticks, label, title)

 "The line chart above is a graphical representation of the rate of people that died from 1990 to 2019 in the world. The chart above shows the numbe deaths caused by malaria,hiv/aids, road accident, self-harm each year in that period.\n",
 "\n",
 "Between the last three years, the cases slowly reduced because of measures put in place and awarenesss created towards the causes of the deaths"/n

#plotting a pie graph to show the number of people that have died from malaria, HIV/AIDS, Self harm and road injuries from 1990 to 2019

plt.figure()
plt.pie(summary_table['Sum'], labels = summary_table.index)
title = 'A pie graph showing the total number of people that died from malaria, HIV/AIDS, Self harm and road injuries from 1990 to 2019'
plt.title(title)

def plot_pie_graph(x_axis, label, title):
    plt.figure(figsize=(15,10))
    for i in range(len(x_axis)):
     plt.plot(x_axis).set_title(title[i])
     plt.pie(x_axis[i],labels=label)
     plt.title(title)
    plt.show()

x_axis = summary_table.index[summary_table]
label = summary_table['Sum']
title = 'A pie graph showing the total number of people that died from malaria, HIV?AIDS, Self harm and road injuries from 1990 to 2019'

plot_pie_graph(x_axis, label, title)

 "The pie graph above isa graphcal representaion showing the number of people that have died in the world from 1990 to 2019"//n


