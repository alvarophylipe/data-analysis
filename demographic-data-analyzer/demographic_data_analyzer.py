import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male']['age'].mean().round(decimals = 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df.education.value_counts()['Bachelors'] / df.education.value_counts().values.sum() * 100).round(decimals = 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = (df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors') | (df['education'] == 'Doctorate')) & (df['salary'] == '<=50K')].education.value_counts().values.sum() / df.education.value_counts().values.sum() * 100).round(decimals = 1)

  
    lower_education = (df.loc[((df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate')) & (df['salary'] == '<=50K')].education.value_counts().values.sum() / df.education.value_counts().values.sum() * 100).round(decimals = 1)

    # percentage with salary >50K
    high_education_df = df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors') | (df['education'] == 'Doctorate'))]

    lower_education_df = df.loc[(df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate')]
  
    higher_education_rich = (high_education_df[high_education_df['salary'] == '>50K'].education.value_counts().values.sum() / high_education_df.education.value_counts().values.sum() * 100).round(decimals = 1)
  
    lower_education_rich = (lower_education_df[lower_education_df['salary'] == '>50K'].education.value_counts().values.sum() / lower_education_df.education.value_counts().values.sum() * 100).round(decimals = 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[(df['hours-per-week'] == min_work_hours)]['salary'].count()

    rich_percentage = (df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]['salary'].count() / num_min_workers * 100).round(decimals = 1)

    # What country has the highest percentage of people that earn >50K?

    country_counts_df = pd.DataFrame(df.groupby(df['native-country'])['salary'].count())
    country_counts_df = country_counts_df.rename(columns={"salary": "counts"}).reset_index()
    country_rich_counts_df = pd.DataFrame(df.groupby(df['native-country'])['salary'].value_counts())
    country_rich_counts_df = country_rich_counts_df.loc[(slice(None), '>50K'), :]
    country_rich_counts_df = country_rich_counts_df.rename(columns={"salary": "rich-counts"})
    country_rich_counts_df = country_rich_counts_df.reset_index()[['native-country', 'rich-counts']]
    country_counts_df = country_counts_df.merge(country_rich_counts_df, on='native-country')
    country_counts_df['rich-percent'] = (country_counts_df['rich-counts'] / country_counts_df['counts'] * 100)
    country_counts_df['rich-percent'] = country_counts_df['rich-percent'].round(decimals=1)
    top_country = country_counts_df.sort_values('rich-percent', ascending=False).head(1)
  
    highest_earning_country = top_country.iloc[0]['native-country']
    highest_earning_country_percentage = top_country.iloc[0]['rich-percent']

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
