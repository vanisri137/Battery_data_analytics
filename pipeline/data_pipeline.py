import pandas as pd
import numpy as np
import os


def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records")
    return df


def handle_missing(df):
    df['temperature'] = df['temperature'].fillna(df['temperature'].median())
    df['capacity'] = df['capacity'].fillna(df['capacity'].median())
    print("Missing values handled")
    return df


def standardize_categories(df):
    df['test_type'] = df['test_type'].str.lower().str.strip()
    df['status'] = df['status'].str.lower().str.strip()
    return df


def remove_outliers(df):
    before = len(df)
    df = df[df['voltage'].between(2.5, 4.5)]
    df = df[df['temperature'].between(0, 60)]
    df = df[df['retention_rate'].between(0, 100)]
    print(f"Removed {before - len(df)} outliers")
    return df


def create_derived_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['duration_category'] = pd.cut(
        df['duration_minutes'],
        bins=[0, 60, 120, 180],
        labels=['short', 'medium', 'long']
    )
    return df


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicates")
    return df


def run_pipeline(input_path, output_path):
    df = load_data(input_path)
    df = handle_missing(df)
    df = standardize_categories(df)
    df = remove_outliers(df)
    df = create_derived_features(df)
    df = remove_duplicates(df)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Clean data saved: {len(df)} records → {output_path}")
    return df


if __name__ == "__main__":
    run_pipeline(
        'data/raw/sample_battery_data.csv',
        'data/cleaned/cleaned_battery_data.csv'
    )
