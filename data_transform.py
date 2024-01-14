import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
import statsmodels.api as sm
import missingno as msno
from scipy import stats


# read csv file with data
loan_df = pd.read_csv('loan_payment.csv')
loan_df.head() # display the first few rows
loan_df.info() # get number of rows, data types and null values


# class to get various information about the dataframe
class DataFrameInfo:
    def __init__(self, df):
        self.df = df
    
    def df_info(self):
        # statistical overview of dataset
        return self.df.describe()

    def data_types(self):
        # data types in columns
        return self.df.dtypes
    
    def df_shape(self, df):
        # shape of the dataframe (number of rows and columns)
        print(df.shape)
    
    def null_values(self, df):  
        # get the percentage of null values in the columns   
        print(df.isnull().sum()/len(df)*100)

    def unique_values(self, table, col):
        # count distict values in columns
        print(table[col].nunique())


# class to visualise insights from the data
class Plotter:
    def __init__(self, df):
        self.df = df
    
    def histogram(self, column):
        # histogram
        plt.xlabel(self.column)
        plt.title("Histogram")
        plt.show()
        return sns.histplot(data=self.df, x=column, kde=True)

    def nan_values(self):
        # visualise NaN values
        return msno.bar(self.df)
    
    def heatmap(self):
        # correlation matrix
        return sns.heatmap(self.df.corr(), square=True, annot=False, cmap='coolwarm')
    
    def qq_plot(self, col):
        self.col = col
        return qqplot(self.df[self.col] , scale=1 ,line='q', fit=True)
    

# class to perform EDA transformations on the data
class DataFrameTransform():
    def __init__(self, df):
        self.df = df
    
    def nan_removal(self, column):
        return self.df[column].dropna()
    
    def outlier_removal(self, column):
        # remove outliers
        outliers = DataFrameInfo.outliers_in_columns(self, column)
        self.df = self.df.drop(outliers)
        return self.df[column]
    
    def mean_imputation(self, column):
        # replace NaN values with the mean of the respective column
        mean = self.df[column].mean()
        self.df[column].fillna(mean, inplace= True)
        return self.df[column]

    def median_imputation(self, column):
        # replace NaN values with the median of the respective column
        median = self.df[column].median()
        self.df[column].fillna(median, inplace= True)
        return self.df[column]
    
    def box_cox(self, column):
        # Box-Cox transformation mainly for positive data
        return stats.boxcox(self.df[column])
    
    def yeo_johnson(self, column):
        # Yeo-Johnson transformation to handle both positive and negative values
        return stats.yeojohnson(self.df[column])