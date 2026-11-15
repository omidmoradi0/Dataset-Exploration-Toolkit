# Dataset Exploration Toolkit

A Python-based toolkit for exploring numerical datasets through descriptive statistics, correlation analysis, and outlier detection.

## Features

- **Descriptive Statistics:** Mean, median, variance, standard deviation, minimum, maximum, quartiles, and skewness.
- **Correlation Analysis:** Pearson correlation matrices for selected numerical columns.
- **Outlier Detection:** Identification of unusual values using the Interquartile Range (IQR) method.
- **Report Generation:** A unified report containing descriptive statistics, correlation matrices, and outlier summaries.
- **Missing Value Handling:** Statistical calculations ignore missing values where appropriate and handle entirely missing columns.
- **Reusable Functions:** Statistical operations are organized in a standalone Python module.

## Tech Stack

- Python
- Pandas
- NumPy
- Jupyter Notebook

## Project Structure

```text
Dataset-Exploration-Toolkit/
├── statistics_explorer.py
├── exploratory_analysis.ipynb
└── README.md
```

## Usage

Import the reporting function:

```python
import pandas as pd
from statistics_explorer import generate_report

df = pd.read_csv("your_dataset.csv")

report = generate_report(df, ["price", "points"])

print(report["statistics"])
print(report["correlation"])
print(report["outliers"])
```

## Validation

The toolkit has been validated using six notebook-based tests covering:

1. Descriptive statistics
2. Pearson correlation
3. IQR outlier detection
4. Missing values
5. Constant-value columns
6. Entirely missing columns

## Future Improvements

- Distribution visualizations
- Additional correlation methods
- Configurable outlier detection
- Automated report export

## License

No license has been selected yet.
