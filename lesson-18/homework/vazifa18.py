# Homework 2:

import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')

df['creationdate'] = pd.to_datetime(df['creationdate'])
questions_before_2014 = df[df['creationdate'] < '2014-01-01']

score_above_50 = df[df['score'] > 50]

score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]

answered_by_scott_boston = df[df['ans_name'] == 'Scott Boston']

users = ['Unutbu', 'Mike Pennington', 'unutbu', 'DSM', 'unutbu']
answered_by_5_users = df[df['ans_name'].isin(users)]

date_filtered = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
]

score_or_views = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]

not_answered_by_scott_boston = df[df['ans_name'] != 'Scott Boston']


# Homework 3:

titanic_df = pd.read_csv("titanic.csv")


female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]


fare_above_100 = titanic_df[titanic_df['Fare'] > 100]


survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]


embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]


with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]


under_15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]


cabin_and_high_fare = titanic_df[
    titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)
]


odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 != 0]


unique_tickets = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]


miss_class1_females = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1)
]
