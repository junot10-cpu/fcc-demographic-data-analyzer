import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    """Calculate demographic statistics and optionally display the results."""
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round(
        df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1
    )

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round(
        df[higher_education & (df['salary'] == '>50K')].shape[0]
        / higher_education.sum() * 100, 1
    )

    lower_education = ~higher_education
    lower_education_rich = round(
        df[lower_education & (df['salary'] == '>50K')].shape[0]
        / lower_education.sum() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_min_workers = df[
        (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')
    ].shape[0]
    rich_percentage = round(rich_min_workers / num_min_workers * 100, 1)

    df['native-country'] = df['native-country'].replace('?', np.nan)
    country_count = df['native-country'].value_counts()
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_percentage = (country_rich_count / country_count * 100).fillna(0)
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage[highest_earning_country], 1
    )

    india_occupations = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts()
    top_IN_occupation = india_occupations.idxmax()

    if print_data:
        print('Number of people of each race:')
        print(race_count)
        print(f'Average age of men: {average_age_men}')
        print(f'Percentage with a Bachelors degree: {percentage_bachelors}%')
        print(f'Percentage earning >50K among those with higher education: {higher_education_rich}%')
        print(f'Percentage earning >50K among those without higher education: {lower_education_rich}%')
        print(f'Minimum hours worked per week: {min_work_hours}')
        print(f'Percentage earning >50K among minimum-hour workers: {rich_percentage}%')
        print(f'Country with the highest percentage earning >50K: {highest_earning_country}')
        print(f'Highest country percentage: {highest_earning_country_percentage}%')
        print(f'Most popular occupation in India among those earning >50K: {top_IN_occupation}')

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == '__main__':
    calculate_demographic_data()
