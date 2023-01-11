import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df['overweight'] = [1 if i > 25 else 0 for i in df['weight'].values / ((df['height'].values / 100) ** 2)]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['gluc'] = [1 if x > 1 else 0 for x in df['gluc']]
df['cholesterol'] = [1 if x > 1 else 0 for x in df['cholesterol']]


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['cholesterol', 'gluc', 'smoke','alco','active', 'cardio', 'overweight']]


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.melt(id_vars = 'cardio', var_name='variable', value_name='value')

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x = 'variable', 
                    hue = 'value' , 
                    col = 'cardio',
                    data = df_cat, 
                    kind = 'count', 
                    order = ['active', 'alco','cholesterol', 'gluc', 'overweight', 'smoke']).set_axis_labels('variable','total')
  
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (15,10))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, 
                mask = mask, 
                vmax = 0.3,
                center = 0,
                annot = True,
                square = True, 
                linewidths=0.5, 
                cbar_kws={'shrink': 0.5, 'ticks':             [0.24,0.16,0.08,0, -0.08]}, 
                fmt = '.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
