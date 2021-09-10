import random
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

dataStr = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\DSScoreTerm1.csv'
phy = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\PhysicsScoreTerm1.csv'
maths = 'C:\\Users\\sanjum\\Documents\\Devops\\venv\\kl8tld4aox\\777_m4_datasets_v1.0\\MathScoreTerm1.csv'

score_datastr = pd.read_csv(dataStr)
score_phy = pd.read_csv(phy)
score_math = pd.read_csv(maths)

score_datastr.loc[(score_datastr.Ethinicity == 'White American'), 'Ethinicity'] = 1
score_datastr.loc[(score_datastr.Ethinicity == 'European American'), 'Ethinicity'] = 2
score_datastr.loc[(score_datastr.Ethinicity == 'Hispanic'), 'Ethinicity'] = 3
score_datastr.loc[(score_datastr.Ethinicity == 'African American'), 'Ethinicity'] = 4
score_phy.loc[(score_phy.Ethinicity == 'White American'), 'Ethinicity'] = 1
score_phy.loc[(score_phy.Ethinicity == 'European American'), 'Ethinicity'] = 2
score_phy.loc[(score_phy.Ethinicity == 'Hispanic'), 'Ethinicity'] = 3
score_phy.loc[(score_phy.Ethinicity == 'African American'), 'Ethinicity'] = 4
score_math .loc[(score_math.Ethinicity == 'White American'), 'Ethinicity'] = 1
score_math .loc[(score_math.Ethinicity == 'European American'), 'Ethinicity'] = 2
score_math .loc[(score_math.Ethinicity == 'Hispanic'), 'Ethinicity'] = 3
score_math .loc[(score_math.Ethinicity == 'African American'), 'Ethinicity'] = 4

score_datastr.loc[(score_datastr.Sex == 'M'), 'Sex'] = 1
score_phy.loc[(score_phy.Sex == 'M'), 'Sex'] = 1
score_math.loc[(score_math.Sex == 'M'), 'Sex'] = 1
score_datastr.loc[(score_datastr.Sex == 'F'), 'Sex'] = 2
score_phy.loc[(score_phy.Sex == 'F'), 'Sex'] = 2
score_math.loc[(score_math.Sex == 'F'), 'Sex'] = 2

score_datastr_average = round(score_datastr["Score"].mean(), 0)
score_phy_average = round(score_phy["Score"].mean(), 0)
score_math_average = round(score_math["Score"].mean(), 0)

score_math['Score'] = score_math.Score.fillna(score_math_average)
score_phy['Score'] = score_phy.Score.fillna(score_phy_average)
score_datastr['Score'] = score_datastr.Score.fillna(score_datastr_average)

score_phy.rename(columns={'Score': 'Physics'}, inplace=True)
score_math.rename(columns={'Score': 'Maths'}, inplace=True)
score_datastr.rename(columns={'Score': 'DataStructures'}, inplace=True)

score_datastr.drop(['Name', 'Subject'], axis=1, inplace=True)
score_phy.drop(['Name', 'Subject'], axis=1, inplace=True)
score_math.drop(['Name', 'Subject'], axis=1, inplace=True)

score_phy_math = pd.merge(score_phy, score_math[['ID', 'Maths']], on='ID', how='inner')
score_phy_math_data = pd.merge(score_phy_math, score_datastr[['ID', 'DataStructures']], on='ID', how='inner')

score_phy_math_data.to_csv('Score.csv', header=True, index=False)

score_phy_math_data_corr = score_phy_math_data.corr()
print('Correlation Analysis:')
print(score_phy_math_data_corr)

sn.heatmap(score_phy_math_data_corr, annot=True)
plt.show()
print('Correlation Matrix is complete')
print('\n')
