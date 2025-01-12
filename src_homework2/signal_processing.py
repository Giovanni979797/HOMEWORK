"""Signal Processing Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
def analyze_signal(time, clean, noisy):
    """
    Exercise 1: Signal Processing with NumPy
    ---------------------------------------
    Task: Analyze and visualize a signal with noise.
    
    Required steps:
    1. Calculate basic signal statistics:
       - Mean and standard deviation
       - Maximum and minimum values
       - Signal-to-noise ratio
    
    2. Process the signal:
       - Apply a moving average filter (window size = 5)
       - Perform frequency analysis using FFT
    
    3. Create visualizations:
       - Plot original clean signal
       - Plot noisy signal
       - Plot filtered signal
       - Show frequency spectrum
    
    Parameters:
    -----------
    time : numpy.ndarray
        Time points for the signal
    clean : numpy.ndarray
        Original clean signal values
    noisy : numpy.ndarray
        Signal with added noise
    
    Expected Output:
    --------------
    1. Two subplot figure showing:
       - Time domain: clean, noisy, and filtered signals
       - Frequency domain: frequency spectrum
    2. Dictionary with signal statistics
    
    Hint: Use np.fft for frequency analysis
    """
    pass

