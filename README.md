# Demographic Data Analyzer

A Python and Pandas project by **Junot Cacoq** for the freeCodeCamp Data Analysis with Python curriculum.

This project analyzes census data to answer questions about education, income, age, working hours, country of origin, and occupation. It uses filtering, frequency counts, Boolean masks, and descriptive statistics to calculate each answer.

## Dataset

The included `adult.data.csv` contains **32,561 records and 15 columns**. It is the CSV provided in the freeCodeCamp project template, based on the [UCI Adult dataset](https://archive.ics.uci.edu/dataset/2/adult).

The analysis describes the records in this dataset; the percentages are not estimates of current country populations.

## Questions answered

1. How many people belong to each race category in the dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelors degree?
4. Among people with Bachelors, Masters, or Doctorate degrees, what percentage earn more than $50,000?
5. Among people without those degrees, what percentage earn more than $50,000?
6. What is the minimum number of hours worked per week?
7. Among people who work that minimum, what percentage earn more than $50,000?
8. Which country has the highest percentage of people earning more than $50,000, and what is that percentage?
9. What is the most common occupation among people from India earning more than $50,000?

## Project files

| File | Purpose |
| --- | --- |
| `demographic_data_analyzer.py` | Reads the CSV, calculates the answers, and returns a dictionary. |
| `adult.data.csv` | Input dataset. |
| `main.py` | Displays the analysis and runs the included tests. |
| `test_module.py` | Eleven learning tests for the results and optional console output. |

## Installation

Install Python 3 and Git, then run:

```bash
git clone https://github.com/junot10-cpu/fcc-demographic-data-analyzer.git
cd fcc-demographic-data-analyzer
python -m pip install pandas numpy
```

On Windows, if you use Python 3.14 through the Python launcher, replace `python` with `py -3.14` in the commands.

## Run the project

Run these commands from the project folder so the CSV can be found.

Display the analysis and run the included tests:

```bash
python main.py
```

Display only the analysis:

```bash
python demographic_data_analyzer.py
```

Run only the tests:

```bash
python -m unittest test_module -v
```

## Use the function

```python
from demographic_data_analyzer import calculate_demographic_data

# Return the results without printing them.
results = calculate_demographic_data(print_data=False)

print(results['average_age_men'])
print(results['highest_earning_country'])
```

`print_data=True` displays the answers. Both modes return the same dictionary. Importing the module does not run the analysis automatically.

## Results

Results calculated using the included CSV:

| Metric | Result |
| --- | --- |
| Average age of men | 39.4 years |
| People with a Bachelors degree | 16.4% |
| Earn >50K among those with higher education | 46.5% |
| Earn >50K among those without higher education | 17.4% |
| Minimum weekly working hours | 1 hour |
| Earn >50K among minimum-hour workers | 10.0% |
| Country with the highest proportion earning >50K | Iran |
| Highest country proportion | 41.9% |
| Most common occupation in India among those earning >50K | Prof-specialty |

Percentages and the average age are rounded to one decimal place. Country percentages use the number of records from each country as the denominator. Unknown country values (`?`) are excluded from country counts.

## Testing

All **11 included learning tests passed** with the supplied dataset. They check the ten returned dictionary entries and confirm that `print_data=False` produces no console output.

These are custom learning tests, not the official freeCodeCamp test suite. They are tied to the included dataset and should be used alongside the official project tests.

## Skills practiced

- Reading CSV data with Pandas.
- Filtering rows with multiple conditions.
- Counting categories with `value_counts()`.
- Creating Boolean masks with `isin()` and `~`.
- Calculating percentages with the correct group denominator.
- Aligning Pandas Series by country name.
- Finding maximum values and their labels with `max()` and `idxmax()`.
- Organizing calculations into a reusable function.
- Writing and running tests with `unittest`.
- Using Git and GitHub to manage a project.

## References

- [freeCodeCamp project instructions](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer)
- [freeCodeCamp starter template](https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer)
- [UCI Adult dataset](https://archive.ics.uci.edu/dataset/2/adult)

## Author

**Junot Cacoq** · [GitHub](https://github.com/junot10-cpu)
