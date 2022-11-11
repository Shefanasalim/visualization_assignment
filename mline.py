# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:51:13 2022

@author: ASUS
"""
import pandas as pd
import matplotlib.pyplot as plt


"""
    Function to read the data using pandas.
    Return the dataframe  
"""
def read_data():
    # Load the .csv data as dataframe
    df = pd.read_csv('car_details.csv')
    
    return df


"""
    Function to split the column name to brand and name 
    and calculate avg selling price by brand name
    Input: dataframe
    Return: top 10 brands with maximum mean selling price.
"""
def group_by_brand(data):
    data[['brand', 'name']] = data['name'].str.split(' ', 1, expand= True)
    data = data[['brand', 'name', 'selling_price', 'year']].sort_values('year')
    value = data.groupby('brand', as_index= False).mean()
    sorted_price = value.sort_values(by= ['selling_price'], ascending= False)

    return sorted_price.head(10) # return 10 brands with highest average selling prices


"""
    Visualize the data as line plot for Year Vs Selling Price 
    Input: Year, Selling Price
    Return: line graph    
"""
def line_plot(maruti_year, maruti_selling_price, hyundai_year, hyundai_selling_price):
    plt.figure(figsize= (12, 8), facecolor= 'w') # set figure layout
    ax = plt.axes()
    ax.set_facecolor('w')
    ax.tick_params(axis= 'both', colors= 'black')
    ax.set_xticklabels(maruti_year, rotation= 50, fontdict={'horizontalalignment': 'center'})
    plt.title('Average Selling Price Of Maruti Swift Dzire VDI VS Hyundai EON Era Plus ', fontsize= 15, color= 'black')
    plt.xlabel('Year', fontsize= 16, color= 'black')
    plt.ylabel('Avg Selling Price (in INR)', fontsize= 16, color='black')
    plt.legend()
    plt.grid(True)

    plt.plot(maruti_year, maruti_selling_price, label = "Maruti Swift Dzire VDI", marker= 'o', markersize= 4, color= '#12436D', linewidth= 3) # plot line1 graph
    plt.plot(hyundai_year, hyundai_selling_price, label = "Hyundai EON Era Plus", marker= 'o', markersize= 4, color= '#F46A25', linewidth= 3) # plot line2 graph 
    plt.show()   
    
    
""" 
    Visualize the data as bar plot for Brand Vs Average Selling Price
    Input: brand,selling_price
    Return: bar graph
"""
def bar_plot(brand, selling_price):
    plt.figure(figsize= (20, 8)) # set figure layout
    ax = plt.axes() 
    ax.set_facecolor('w')
    ax.set_xticklabels(brand, rotation= 50, fontdict= {'horizontalalignment': 'center'})
    plt.title('Brand Vs Avg Selling Price', fontsize= 15, color= 'black')
    plt.xlabel('Manufacturer', fontsize= 10, color= 'black')
    plt.ylabel('Avg Selling Price (in INR)', fontsize= 10, color= 'black')
    
    plt.bar(brand, selling_price, color= 'maroon', width= 0.4) # plot bar graph
    plt.show()
    

""" 
    Visualize the data as pie plot for the column owner 
    Input: dataframe 
    Return: pie diagram 
"""
def pie_plot(data): 
    data = data['owner'].value_counts()
    fig, ax = plt.subplots()
    ax.set_title('Owner distribution of Maruti Swift Dzire VDI')
    ax.pie(data, labels= None, autopct= '%.0f%%', startangle= 90, textprops= dict(color= "black")) # plot pie chart  
    plt.legend(data.index, loc= "upper left", prop= {"size": 6})
    plt.show()
    
    
# Calling function read_data to read the data
df = read_data()
maruti_data = df[df['name'] == 'Maruti Swift Dzire VDI'] 
maruti_data = maruti_data[['year', 'selling_price', 'owner']].sort_values('year')
maruti_value = maruti_data.groupby('year',as_index= False).mean()

hyundai_data = df[df['name'] == 'Hyundai EON Era Plus']
hyundai_data = hyundai_data[['year', 'selling_price']].sort_values('year')
hyundai_value = hyundai_data.groupby('year', as_index= False).mean()

# Declare and initialize variables year and selling price
maruthi_year = maruti_value.year
maruthi_selling_price = maruti_value.selling_price

hyundai_year = hyundai_value.year
hyundai_selling_price = hyundai_value.selling_price

# calling function line_plot to draw line graph
line_plot(maruthi_year, maruthi_selling_price, hyundai_year, hyundai_selling_price) 

# calling function group_by_brand
brand_avg_selling_price = group_by_brand(df)

# calling function bar_plot to bar graph
bar_plot(brand_avg_selling_price.brand, brand_avg_selling_price.selling_price)

# calling function pie_plot
pie_plot(maruti_data)