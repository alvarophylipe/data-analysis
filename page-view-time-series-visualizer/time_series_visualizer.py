import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date',parse_dates=['date'])

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025))) & (df['value'] <= (df['value'].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot

  
    fig = df.plot.line(y = 'value', 
                       figsize = (17,6), 
                       color= '#f90202', 
                       linewidth=0.9, 
                       xlabel = 'Date', 
                       ylabel = 'Page Views',
                       title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
                       legend = None,
                       rot = 0).figure



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot

    label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig = df_bar.plot.bar(figsize = (7.5,6.5), xlabel = 'Years', ylabel = 'Average Page Views').figure
    plt.legend(labels = label, title = 'Months')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (25,10))
    barplt1 = sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axes[0])
    barplt1.set_xlabel('Year')
    barplt1.set_ylabel('Page Views')
    barplt1.set_title('Year-wise Box Plot (Trend)')

    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    barplt2 = sns.boxplot(x = 'month', y = 'value', data =    df_box, ax = axes[1], order = order)
    barplt2.set_xlabel('Month')
    barplt2.set_ylabel('Page Views')
    barplt2.set_title('Month-wise Box Plot (Seasonality)')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
