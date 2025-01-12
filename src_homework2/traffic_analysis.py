"""Traffic Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt 


def analyze_traffic(df):
    """
    Exercise 4: Website Traffic Analysis with Pandas
    --------------------------------------------
    Task: Analyze website traffic patterns and bounce rates.
    
    Required steps:
    1. Time series analysis:
       - Calculate daily traffic patterns
       - Compute moving averages (3-day and 7-day)
       - Identify weekly patterns
    
    2. Bounce rate analysis:
       - Calculate average bounce rates
       - Correlate bounce rates with traffic
       - Identify high/low bounce rate periods
    
    3. Create visualizations:
       - Traffic trends with moving averages
       - Daily traffic patterns
       - Bounce rate trends
       - Traffic vs bounce rate correlation
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns:
        - Date: datetime index
        - Visitors: daily visitor count
        - Bounce_Rate: daily bounce rate percentage
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Traffic trends with moving averages
       - Average daily traffic patterns
       - Bounce rate trend
       - Correlation scatter plot
    2. Dictionary with traffic statistics
    
    Hint: Use df.rolling for moving averages
    """
    pass
