# Use Python PyQt5 GUI to show figures of k-means clustering and analysis of iris data
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5 import QtCore 
from PyQt5 import QtWidgets
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from sklearn import cluster

import pandas as pd
import sqlite3

import irispkg.irisdata as iris        #here
from sqlite_module import sqliris  #here
    
class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.layoutVertical = QtWidgets.QVBoxLayout(self)        
        self.layoutVertical.addWidget(self.canvas)
        
               
class MyWindow(QtWidgets.QWidget):
    #num = 0
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Save to SQLite")
        self.button1.clicked.connect(self.button1_clicked)
        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("Read from SQLite")
        self.button2.clicked.connect(self.button2_clicked)
        
        self.lb = QtWidgets.QLabel(self)
        self.lb.setText('6018-2017 Project. Select from the drop down list to see figures and clustering results')
        
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("0. Box plots")
        self.comboBox.addItem("1. Histogram")
        self.comboBox.addItem("2. sepal-length - sepal-width K-means Clustering")
        self.comboBox.addItem("3. sepal-length - petal-length K-means Clustering")
        self.comboBox.addItem("4. sepal-length - petal-width K-means Clustering")
        self.comboBox.addItem("5. sepal-width - petal-length K-means Clustering")
        self.comboBox.addItem("6. sepal-width - petal-width K-means Clustering")
        self.comboBox.addItem("7. petal-length - petal-width K-means Clustering")        
        #self.comboBox.move(50, 250)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        self.matplotlibWidget = MatplotlibWidget(self)
        self.layoutVertical = QtWidgets.QVBoxLayout(self)    
        self.layoutVertical.addWidget(self.lb)
        self.layoutVertical.addWidget(self.comboBox)        
        self.layoutVertical.addWidget(self.matplotlibWidget)
        self.layoutVertical.addWidget(self.button1)
        self.layoutVertical.addWidget(self.button2)
    
    @QtCore.pyqtSlot()
    def button1_clicked(self):          
        sqlite_file = 'iris.db'    
        table_name = 'iris_table'   
        sqliris.save_to_sqlite(sqlite_file, table_name) #here
    @QtCore.pyqtSlot()
    def button2_clicked(self):         
        sqlite_file = 'iris.db'    
        table_name = 'iris_table'   
        dataset=sqliris.read_from_sqlite(sqlite_file, table_name) #here

    def selectionchange(self,i):
        if i==0: 
            dataset = iris.irisdata() #here
            stats = iris.boxplt(dataset)  #here
                  
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.bxp(stats)
            self.matplotlibWidget.axis.set_xlabel('sepal-length, sepal-width, petal-length, petal-width')
            self.matplotlibWidget.canvas.draw()            
            
        if i==1:  
            dataset = iris.irisdata()
            df1 = iris.histplt(dataset)            
            
            self.matplotlibWidget.axis.clear()
            self.matplotlibWidget.axis.hist(df1)   
            self.matplotlibWidget.axis.set_xlabel('sepal-length, sepal-width, petal-length, petal-width')
            self.matplotlibWidget.canvas.draw()               

        if i==2:
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,0,1)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('sepal-length')
            self.matplotlibWidget.axis.set_ylabel('sepal-width')
            self.matplotlibWidget.canvas.draw() 
            
        if i==3:
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,0,2)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('sepal-length')
            self.matplotlibWidget.axis.set_ylabel('petal-length')
            self.matplotlibWidget.canvas.draw()             
            
        if i==4:            
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,0,3)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('sepal-length')
            self.matplotlibWidget.axis.set_ylabel('petal-width')
            self.matplotlibWidget.canvas.draw()               
            
        if i==5:   
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,1,2)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('sepal-width')
            self.matplotlibWidget.axis.set_ylabel('petal-length')
            self.matplotlibWidget.canvas.draw()            
            
        if i==6:
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,1,3)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('sepal-width')
            self.matplotlibWidget.axis.set_ylabel('petal-width')
            self.matplotlibWidget.canvas.draw()             
            
        if i==7:  
            dataset = iris.irisdata()
            data=iris.kmeancls(dataset,2,3)
            k = 3
            kmeans = cluster.KMeans(n_clusters=k)
            kmeans.fit(data)

            labels = kmeans.labels_
            centroids = kmeans.cluster_centers_
            
            self.matplotlibWidget.axis.clear()
            for i in range(k):
                ds = data[np.where(labels==i)]
                self.matplotlibWidget.axis.plot(ds[:,0],ds[:,1],'o')
                self.matplotlibWidget.axis.plot(centroids[i,0],centroids[i,1],'kx')
            self.matplotlibWidget.axis.set_xlabel('petal-length')
            self.matplotlibWidget.axis.set_ylabel('petal-width')
            self.matplotlibWidget.canvas.draw()             
           
    
def main():
    
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(888, 444)
    main.show()
    
    app.exec_()

if __name__ == '__main__':
    main()
