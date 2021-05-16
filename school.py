#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("District_Level_School_Dataset")

#import dataset
df = pd.read_csv('DistrictLevelData_V3.csv')

#First thirty rows
attendance = df.head(30)
#Display the table
st.table(attendance)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
attendance.plot(kind='bar')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(attendance,)
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(attendance['CovidTotalStateCases'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Mem',y='AttendancePercent',data=attendance,kind='hex',color="#4CB391")
st.pyplot()

#Correation
st.subheader("Heatmap")
sns.heatmap(attendance.corr(),cmap='coolwarm',annot=True)
st.pyplot()
#Replot
st.subheader("RelPlot")
sns.relplot(x='CovidTotalStateCases',y='CovidTotalCountyCases',hue='Weekday', data=attendance)
st.pyplot()

 