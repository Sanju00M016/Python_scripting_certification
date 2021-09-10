import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


filepath = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\Module5\\v9d2ub3fjr\\777_m5_datasets_v1.0\\Hurricanes.csv'
filepath2 = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\Module5\\v9d2ub3fjr\\777_m5_datasets_v1.0\\CityTemps.csv'
filepath3 = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\Module5\\v9d2ub3fjr\\777_m5_datasets_v1.0\\Cars2015.csv'
filepath4 = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\Module5\\v9d2ub3fjr\\777_m5_datasets_v1.0\\sample-salesv2.csv'

#QUESTION 1
'''
df_read = pd.read_csv(filepath)
df_read.plot(kind='bar',x='Year',y='Hurricanes')
plt.ylabel('No of Hurricanes')
plt.xlabel('Year')
plt.show()
'''

#QUESTION 2
'''
df_read = pd.read_csv(filepath2)
plt.hist(df_read['Moscow'], bins=500)
plt.hist(df_read['Melbourne'],bins=500)
plt.title("City Temperature of Moscow and Melbourne")
plt.show()
'''

#QUESTION 3
'''
df_read = pd.read_csv(filepath3,skipinitialspace=True)
df_read['Make'] = df_read['Make'].str.strip()
df_add = df_read.groupby('Make')['Model'].count().reset_index()
print(df_add)
plt.figure(figsize=(8,9))
plt.pie(df_add['Model'],labels=df_add['Make'])
plt.show()
'''

#QUESTION 4
'''
#Phase 1 -Reading Data
df_read = pd.read_csv(filepath4)

#Phase 2 –Describe the data
print(df_read['unit price'].describe())

#Phase 3 –filter the data
df_new = df_read[['name','net_price','date']]
df_new_sales = df_new.groupby('name').sum('net_price').reset_index()
print(df_new_sales)

#Phase 4 –Plotting graph
df_new_sales.plot.bar()
plt.xlabel('Customer Name')
plt.ylabel("Net Price")
plt.show()
'''


#Question 5

'''
x = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]

fig, ax = plt.subplots(1, 2, figsize=(4,5), dpi=100)
fig.tight_layout(h_pad=2)

plt.subplot(1, 2, 1)
plt.plot(x, y, ls=':', marker='D')
plt.title('With Line & Markers')

plt.grid()
plt.axis([0, 5, 19.8, 21.2])
plt.xlabel('X-Axis Data points')
plt.ylabel('Y-Axis Data points')

plt.subplot(1, 2, 2)
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(x, y, yerr=y_error)
plt.title('With Error Bar')

plt.grid()
plt.axis([0, 5, 19.8, 21.2])
plt.xlabel('X-Axis Data points')

plt.subplots_adjust(top=0.85, bottom=0.1, left=0.08)
plt.suptitle('Simple Plot Example', fontsize=14)

plt.show()
'''

#5.8
'''
x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x,y)
plt.show()
'''

#5.9
'''
df_data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
}

df = pd.DataFrame(data=df_data)
print(df)

plt.scatter(df['preTestScore'],df['postTestScore'],s=df['age'])
plt.title('Test Score Scatter by age ')
#plt.show()
'''

#5.10
'''
plt.scatter(df['preTestScore'],df['postTestScore'],s=300,c=df['female'])
plt.title("Test Score Scatter by Sex")
plt.show()
'''