# Feel free to create other helper functions
# def helper_function_name(arguments):
#      pass


#!/usr/bin/env python
# coding: utf-8

# In[17]:


# importing the neccessary libary require for the program
import csv
import pandas as pd

# to import the csv file and convert it into a list data type
file = csv.reader(open('medal.csv', 'r'))
rows = [row for row in file] #array created from csv data set




# the bubbling sorting algorithm
def rank_team(file_name):
    n = len(file_name)#gets the length of array
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if file_name[j][1] < file_name[j + 1][1]:#compares gold medals of teams
                file_name[j], file_name[j + 1] = file_name[j + 1], file_name[j]#switch team position with priority to team with higer gold medals

            if file_name[j][1] == file_name[j + 1][1]:#checks if teams have equal gold medals 
                if file_name[j][2] < file_name[j + 1][2]:#compares silver medals of teams with equal gold medals
                    file_name[j], file_name[j+1] = file_name[j+1], file_name[j]#switch team position with priority to team with higer silver medals

                elif file_name[j][2] == file_name[j + 1][2]:#checks if teams have equal silver medals 
                    if file_name[j][3] < file_name[j + 1][3]:#compares bronze medals of teams with equal silver medals
                        file_name[j], file_name[j+1] = file_name[j+1], file_name[j]#switch team position with priority to team with higer bronze medals
                else:
                    pass   
            else:
                pass
               
    return file_name
    #pass

# Program main --- Do not change the code below but feel free to comment out 
# Calling Task 1 function


sorted_rows = [', '.join(row)+'\n' for row in rank_team(rows)]# this creates a list of the sorted array
with open('medal_table.csv', 'w+') as f:#this will create the medal_table.csv since it does not exist in the directory
    f.writelines(sorted_rows) # this writes the sorted array to the medal_table.csv file and saves the file

medal1=pd.read_csv('medal_table.csv') # this is to read the medal_table.csv as a pandas dataframe

print(medal1) # to print out the result in a pandas dataframe format
print('medal_table.csv file has been created in current directory')#to notify user that the medal_table.csv file has been created


#rank_team('medal.csv')
#medal1=pd.read_csv('medal_table.csv')
#medal1











