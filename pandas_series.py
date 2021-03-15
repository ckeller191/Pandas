import pandas as pd

grades = pd.Series([87,100,94])

#print(grades)

grades = pd.Series(98.6, range(3))

#0  98.6
#1  98.6
#2  98.6
#dtype: float64

a = grades[0]

grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

#calling Series method describe produces all these stats and more:
grades.describe()


grades =pd.Series([87,100,94], index=['Wally', 'Eva', 'Sam'])

#print(grades)

#If you initialize a Series with a dictionary, its keys 


grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

#print(grades['Eva'])
#100

grades.Wally
#87

grades.dtype
#dtype('int64')

grades.values
#array([87, 100, 94])


#Series of Strings
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
#print(hardware)

""" output
0    Hammer
1       Saw
2    Wrench
dtype: object
"""

#calling string methods apply to each element
hardware.str.contains('a')

"""0   True
   1   True
   2   False
   dtype: bool """

hardware_upper = hardware.str.upper()
print(hardware_upper)

#All hardware names in all caps