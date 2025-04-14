import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_titanic_data(filepath):
    df = pd.read_csv(filepath)
    mean_age = df['Age'].mean()
    df['Age'] = df['Age'].fillna(mean_age)
    df.rename(columns = {'PassengerId':'ID'}, inplace = True)
    df.rename(columns = {'Sex':'Gender'}, inplace = True)
    df.rename(columns = {'Pclass':'Class'}, inplace = True)
    return df 

def plot_hist(df, column, title = ''):
    sns.histplot(df[column], bins = 10, kde = True)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_count(df, column, title = ''):
    sns.countplot(x = column, data = df)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

def plot_box(df, x, y, title = ''):
    sns.boxplot(x = x, y = y, data = df)
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

def age_category(age):
    if age < 18:
        return 'Child'
    elif age < 50:
        return 'Adult'
    else:
        return 'Senior'