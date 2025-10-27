

def calculate_average_by_region(df):
    avg_by_region = df.groupby('Область')['Значення'].mean()
    return avg_by_region