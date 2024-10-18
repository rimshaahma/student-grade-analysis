import pandas as pd
import numpy as np

def calculate_average(df):
    """Calculate the average score for each student."""
    df['Average'] = np.mean(df[['Math', 'Science', 'English']], axis=1)
    return df

def add_grades(df):
    """Assign grades based on the average score."""
    def assign_grade(avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        else:
            return 'D'

    df['Grade'] = df['Average'].apply(assign_grade)
    return df
