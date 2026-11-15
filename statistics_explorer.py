import numpy as np
import pandas as pd


def analyze_column(target_col):
    std = target_col.std()
    skewness = target_col.skew() if std > 0 else np.nan

    if target_col.count() == 0:
        return pd.Series({
            "mean": np.nan,
            "median": np.nan,
            "variance": np.nan,
            "standard_deviation": np.nan,
            "Min": np.nan,
            "Max": np.nan,
            "Q1": np.nan,
            "Q3": np.nan,
            "skewness": np.nan
        })
    else : 
        statistic_data = {
            "mean": target_col.mean(),
            "median": target_col.median(),
            "variance": target_col.var(),
            "standard_deviation": std,
            "Min": target_col.min(),
            "Max": target_col.max(),
            "Q1": target_col.quantile(0.25),
            "Q3": target_col.quantile(0.75),
            "skewness": skewness
        }

        return pd.Series(statistic_data)

def analyze_dataset(df, cols):
    results = pd.DataFrame(columns=cols)

    for col in cols:
        results[col] = analyze_column(df[col])

    return results


def analyze_correlation(df, cols):
    selected_cols = df[cols]
    return selected_cols.corr(method="pearson")

def detect_outliers(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = col[(col < lower) | (col > upper)]

    valid_count = col.count()
    outlier_count = outliers.count()

    outlier_percentage = (
        outlier_count / valid_count * 100
        if valid_count > 0
        else np.nan
    )

    return {
        "IQR": iqr,
        "Upper_bound": upper,
        "Lower_bound": lower,
        "outlier_count": outlier_count,
        "outlier_percentage": outlier_percentage
    }

def generate_report(df, cols):
    result = {}

    # 1. Descriptive Statistics
    result["statistics"] = analyze_dataset(df, cols).T

    # 2. Correlation Analysis
    result["correlation"] = analyze_correlation(df, cols)

    # 3. Outlier Detection
    outliers = {}

    for col in cols:
        outliers[col] = detect_outliers(df[col])

    result["outliers"] = pd.DataFrame.from_dict(
        outliers, orient="index"
    )

    return result