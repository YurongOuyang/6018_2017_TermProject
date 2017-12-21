# Data preparation
import pandas as pd
import matplotlib.cbook as cbook
from sklearn import cluster
from matplotlib import pyplot as plt
import numpy as np

# Load dataset
def irisdata():
    "Read data to a dataframe"
    url = "iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pd.read_csv(url, names=names)
    return dataset


def histplt(dataset):
    "Prepare data for histogram"
    df = dataset.drop('class', 1)
    df1=df.as_matrix()    
    return df1
#df1 = histplt(dataset)

def boxplt(dataset):
    "prepare data for box plot"
    df = dataset.drop('class', 1)
    df1=df.as_matrix()
    stats = cbook.boxplot_stats(df1)
    return stats
#stats = boxplt(dataset)   

def scatterplt (dataset, a,b):    
    "Prepare data for histogram and scatter plot"
    x=dataset[a]
    y=dataset[b]
    return x, y
#x,y=scatterplt(dataset,'sepal-length','sepal-width')
    
def kmeancls(dataset,m,n):
    "prepare data for k-means clustering"
    'm,n, 0-sepal-length  1-sepal-width  2-petal-length  3-petal-width'
    df = dataset.drop('class', 1)
    df1=df.as_matrix()   
    data=df1[:,np.r_[m,n]]     
    return data    
