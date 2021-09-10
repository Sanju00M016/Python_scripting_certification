import random

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\SalaryGender.csv'

'''
#QUESTION 1
filepath = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\SalaryGender.csv'

df_read = pd.read_csv(filepath)

arr_salary = (df_read['Salary'].to_numpy())
arr_gender = (df_read['Gender'].to_numpy())
arr_age = (df_read['Age'].to_numpy())
arr_phd = (df_read['PhD'].to_numpy())

print(arr_phd, arr_gender, arr_age, arr_phd)
'''

'''
#QUESTION2

filepath = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\SalaryGender.csv'
df_read = pd.read_csv(filepath)
df_csv_men = (df_read['Gender'] == 1)
df_csv_women = (df_read['Gender'] == 0)
df_csv_phd = (df_read['PhD'] == 1)
Num_of_men = df_read[df_csv_men & df_csv_phd]
Num_of_lady = df_read[df_csv_women & df_csv_phd]

print('The Total number with PhD are:', len(Num_of_lady))
print('The Total number Women with PhD are:', len(Num_of_men))
print('\n')
'''

'''
#QUESTION3
df_read = pd.read_csv(filepath)
df_phd_age = (df_read[['Age', 'PhD']])

df_phd_age = (df_phd_age.drop(df_phd_age[df_phd_age['PhD'] == 0].index))

print(("Data of Age & Phd", df_phd_age))
'''

'''
#Question 4
df_read = pd.read_csv(filepath)
df_phd = df_read['PhD'] == 1
print("Total Number of PHD are:", len(df_phd.index))
'''

'''
#QUESTION 5
list_numpy = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]

empty_list = []

for i in list_numpy:
    empty_list.append(list_numpy.count(i))

print("The Output of Array", np.array(empty_list))
print('\n')
'''

'''
#QUESTION6
np_array = np.array([[0,1,2],
                      [3,4,5],
                      [6,7,8],
                      [9,10,11]])

numpy_array_filter = []
for x in np_array:
    for y in x:
        if y > 5:
            numpy_array_filter.append(y)
        else:
            pass

print("Array after flitering:", np.array(numpy_array_filter))
print('\n')
'''

'''
#QUESTION7
df_array = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
df_nan = []

for i in df_array:
    if np.isnan(i)==True:
        pass
    else:
        df_nan.append(i)
print("THE array with NAN is:", df_array)
print('Array without NaN is :',np.array(df_nan))

print('\n')
'''

#QUESTION8
'''
df_array = np.random.randint(1000, size=(10, 10))
print(df_array)
df_max = df_array.max()
df_min = df_array.min()
print("The Maximum Number in 10X10 is", df_max)
print("The Minimum Number in 10X10 is:", df_min)
'''

'''
#Question9
df_vector = np.linspace(0, 30)
print(df_vector)
df_mean = np.mean(df_vector)
print("The Mean value is:", df_mean)
'''

'''
#Question10
df_array = np.arange(11)
print(df_array)
df_ar = []
for i in df_array:
    if i >= 3 and i<=9:
        df_ar.append(i*-1)
    else:
        df_ar.append(i)
print(df_ar)
'''

'''
#QUESTION11
df_array = np.random.randint(1000, size=(3, 3))
df_sort = np.sort(df_array, axis=0)
print(df_sort)
'''

'''
#QUESTION12
df_array = np.arange(48)
arr = df_array.reshape(4,3,2,2)
print("The 4D Dimensional array:", arr)
print("The Sum of last two columns are:", np.sum(arr, axis=(2, 3)))
'''

'''
#Question13
df_array = np.arange(4)
arr = df_array.reshape(2,2)
print("The Array is :\n", arr)
arr[[0,1]] = arr[[1,0]]
print("The Swapped Array is\n", arr)
'''
'''
#QUESTION14
df_array = np.arange(4)
arr = df_array.reshape(2,2)
print("The Matrix is\n", arr)
print('\n')
print("The Matrix rank is: \n", np.linalg.matrix_rank(arr))
'''

'''
#QUESTION15
filepath_1 = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\middle_tn_schools.csv'
print("Phase 1:Data Collection")
df_read = pd.read_csv(filepath_1)
print(df_read)

print("Describing the file:", df_read.describe())
print('\n')

print("Phase 2:Group data by School Rating")
red_lunch = df_read.groupby(['school_rating','stu_teach_ratio']).size().reset_index(name='Calculated')
red_lunch.drop(['Calculated'],axis=1,inplace=True)
print(red_lunch)


print("Phase 3: Correlation Analysis")
cormat = red_lunch.corr()
print(cormat)

print("Phase 4: Scatter plot")
df_plot = df_read.plot(x='reduced_lunch',y='school_rating',kind='scatter')
print('ScatterPlot is complete')
plt.show()

print("Phase 5: Correlation Matrix")
sn.heatmap(cormat,annot=True)
plt.show()
print('Correlation Matrix is done')
print('\n')
'''