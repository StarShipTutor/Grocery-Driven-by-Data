"""
ETL utilities for data transformation and validation.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any


def clean_dataframe(
    df: pd.DataFrame,
    drop_duplicates: bool = True,
    strip_strings: bool = True,
    lowercase_columns: bool = True,
) -> pd.DataFrame:
    """
    Apply standard cleaning transformations to a DataFrame.
    
    Args:
        df: Input DataFrame
        drop_duplicates: Remove duplicate rows
        strip_strings: Strip whitespace from string columns
        lowercase_columns: Convert column names to lowercase with underscores
        
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    
    if lowercase_columns:
        df.columns = (
            df.columns
            .str.lower()
            .str.replace(r"[^\w\s]", "", regex=True)
            .str.replace(r"\s+", "_", regex=True)
        )
    
    if strip_strings:
        string_cols = df.select_dtypes(include=["object"]).columns
        for col in string_cols:
            df[col] = df[col].str.strip() if df[col].dtype == "object" else df[col]
    
    if drop_duplicates:
        df = df.drop_duplicates()
    
    return df


def validate_schema(
    df: pd.DataFrame,
    expected_columns: List[str],
    required_columns: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Validate DataFrame schema against expected columns.
    
    Args:
        df: DataFrame to validate
        expected_columns: List of expected column names
        required_columns: Subset of columns that must be present
        
    Returns:
        Dict with validation results
    """
    required_columns = required_columns or expected_columns
    
    actual_columns = set(df.columns)
    expected_set = set(expected_columns)
    required_set = set(required_columns)
    
    missing_required = required_set - actual_columns
    missing_expected = expected_set - actual_columns
    extra_columns = actual_columns - expected_set
    
    is_valid = len(missing_required) == 0
    
    return {
        "is_valid": is_valid,
        "missing_required": list(missing_required),
        "missing_expected": list(missing_expected),
        "extra_columns": list(extra_columns),
        "column_count": len(df.columns),
        "row_count": len(df),
    }


def profile_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a profiling summary of a DataFrame.
    
    Args:
        df: DataFrame to profile
        
    Returns:
        Profile DataFrame with column statistics
    """
    profile = []
    
    for col in df.columns:
        col_data = df[col]
        
        stats = {
            "column": col,
            "dtype": str(col_data.dtype),
            "non_null_count": col_data.notna().sum(),
            "null_count": col_data.isna().sum(),
            "null_pct": round(col_data.isna().mean() * 100, 2),
            "unique_count": col_data.nunique(),
            "unique_pct": round(col_data.nunique() / len(df) * 100, 2),
        }
        
        if pd.api.types.is_numeric_dtype(col_data):
            stats.update({
                "min": col_data.min(),
                "max": col_data.max(),
                "mean": round(col_data.mean(), 2),
                "std": round(col_data.std(), 2),
            })
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            stats.update({
                "min": col_data.min(),
                "max": col_data.max(),
            })
        else:
            # String/categorical
            stats.update({
                "min": None,
                "max": None,
                "mean": None,
                "std": None,
            })
        
        profile.append(stats)
    
    return pd.DataFrame(profile)


def detect_outliers(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    method: str = "iqr",
    threshold: float = 1.5,
) -> pd.DataFrame:
    """
    Detect outliers in numeric columns.
    
    Args:
        df: Input DataFrame
        columns: Columns to check (default: all numeric)
        method: Detection method ('iqr' or 'zscore')
        threshold: IQR multiplier or z-score threshold
        
    Returns:
        Boolean DataFrame indicating outliers
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    outliers = pd.DataFrame(index=df.index)
    
    for col in columns:
        if col not in df.columns:
            continue
            
        col_data = df[col].dropna()
        
        if method == "iqr":
            q1 = col_data.quantile(0.25)
            q3 = col_data.quantile(0.75)
            iqr = q3 - q1
            lower = q1 - threshold * iqr
            upper = q3 + threshold * iqr
            outliers[col] = (df[col] < lower) | (df[col] > upper)
        elif method == "zscore":
            mean = col_data.mean()
            std = col_data.std()
            z_scores = np.abs((df[col] - mean) / std)
            outliers[col] = z_scores > threshold
        else:
            raise ValueError(f"Unknown method: {method}")
    
    return outliers
