import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math 

num_points = 30

#Graph 1: Correlation Between Genre's Size and Popularity 
def graph1(df, printGraph):
    print("Exporting Graph: Correlation Between Genre's Size and Popularity")
    #Groups df by genre
    genre_df = df.groupby('genre')
    #Gathers size of each genre
    genre_size = genre_df.size()
    #Graph a line plot with genre size (x) and popularity (y)
    fig = plt.figure()
    fig, ax = plt.subplots(1, 1)
    ax.scatter(genre_size, genre_df.mean()['popularity'])
    #Sets properties of graph
    ax.set_xlabel("Genre Size")
    ax.set_ylabel("Popularity")
    ax.set_title("Correlation Between Genre's Size and Popularity")
    #Displays correlation coefficent via Pearson's method
    corr_coeff = genre_size.corr(genre_df.mean()['popularity'])
    ax.text(.95, .05,     #Sets position
            f'r= {corr_coeff:.2f}', #Displays coeff at a 2 decimal place float
            transform=plt.gca().transAxes, ha='right'    #Sets position relative to axes, aligned at the right
            )
    #Shows graph
    if printGraph == True:
        plt.show()
    #Deletes temporary variables for memory allocation
    del genre_df
    del genre_size
    
#Graph 2: Corrlation Between Audio Features and Popularity
def graph2(df, printGraph, features):
      print("Exporting Graph: Correlation Between Audio Features and Popularity")
      #Declares variables
      num_cols = df.shape[1]
      const_var = df['popularity']
      #Creates a graph via loop
      for xcol in features:
         dfSample = df.sample(100)
         corr_coeff = df[xcol].corr(df['popularity'])
         sns.scatterplot(data = dfSample, x = xcol, y = const_var)
         plt.title('Correlation between {} and Popularity'.format(xcol))
         plt.text(.05, .90,     #Sets position
            f'r= {corr_coeff:.2f}', #Displays coeff at a 2 decimal place float
            transform=plt.gca().transAxes, ha='left'    #Sets position relative to axes, aligned at the right
            )
         plt.show()
         
       

