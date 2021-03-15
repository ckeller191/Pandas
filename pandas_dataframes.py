import pandas as pd

grades_dict = {'Wally': [87,96,70],
                'Eva': [100,87,90],
                'Sam': [94,77,90],
                'Katie': [100,81,82],
                'Bob': [83,65,85]}

#create dataframe provided given dictionary
grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

#print(grades)

#print(grades['Eva'])
#both methods let you print grades for a specific student
#print(grades.Sam)


#using the loc and iloc methods

#print(grades.loc['Test2'])

#zero-based indexing - iloc[1] gives 2nd test
#print(grades.iloc[1])


#for consecutive rows
#print(grades.loc['Test1':'Test2'])
    #gives only rows 1 and 2; doesn't count upper bounds
#print(grades.iloc[0:2])

#non-consecutive rows
#print(grades.loc[['Test1', 'Test3']])
#use double square brackets because the parameter is a list
#print(grades.iloc[[0,2]])

#view only Eva's and Katie's grades for test 1 and test 2

#print(grades[['Eva', 'Katie']].loc['Test1':'Test2'])

#method given in class
#print(grades.loc[:'Test2',['Eva', 'Katie']])

#view only Sam and Katie grades for test 1 and test 3

#print(grades[['Sam', 'Katie']].loc[['Test1', 'Test3']])

#method given in class
#print(grades.loc[['Test1', 'Test3'],['Sam','Katie']])

#COLONS for consecutive, COMMAS for non-consecutive


grades_A = grades[grades>=90]

#print(grades_A)


#create a dataframe for everyone with a B grade

grades_B = grades[(grades >= 80) & (grades < 90)]
#print(grades_B)

#create a dataframe for everyone with a A or B grade

grades_AB = grades[(grades >= 90) | (grades>= 80)]
# | symbol not needed, just to show how to use the symbol for 'or'
#print(grades_AB)

print(grades.describe())

pd.set_option('precision', 2)
#changes numbers precision to 2 decimal places

print(grades.describe())