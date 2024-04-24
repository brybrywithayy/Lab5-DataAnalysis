"""
Bryan Dalina
SDEV 300
11 February 2024
Lab 5 - Data Analysis
    The User will load in one of the two CSV files and 
    perform histogram analysis and plots for select variables
    within the datasets.
    The first dataset represents population change over time.
    The second dataset represents housing data over time
    describing home age, number of bedrooms, and other vars.
    The first row provides a column name within each dataset.
    For Population, use
        - Pop Apr 1
        - Pop Jul 1
        - Change pop
    For Housing, use 
        - Age
        - Bedrms
        - Built
        - Rooms
        - Utility
    For each column, calculate the following:
        - Count
        - Mean
        - Standard Deviation
        - Min
        - Max
        - Histogram
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Main menu function
Prints user selection loop and gives exit option"""
def main_menu():
    while True:
        print("********Welcome to the Python Data Anyalysis App********")
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")

        user_input = input()
        if user_input == "1":
            pop_menu()
        elif user_input == "2":
            housing_menu()
        elif user_input == "3":
            print("********Thanks for using the Data Analysis App********")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

"""load file function
Attempts to find and load file from current directory"""
def load_file(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print("Something went wrong - the file could not be found in the current dir.")

"""Population Data Menu
Root menu for population data inputs and function calls"""
def pop_menu():
    # read in the csv first
    data_file = load_file("PopChange.csv")

    while True:
        # print the menu to the user
        print("You have selected Population Data from PopChange.csv")
        print("Select the Column you want to analyze: ")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit to Main Menu")
        user_input = input()
        if user_input == "a":
            retrieve_data("Pop Apr 1", data_file)
        elif user_input == "b":
            retrieve_data("Pop Jul 1", data_file)
        elif user_input == "c":
            retrieve_data("Change Pop", data_file)
        elif user_input == "d":
            break
        else:
            print("Invalid input. Please enter one of the options listed.")

"""Housing Data Menu
Root menu for housing data inputs and function calls"""
def housing_menu():
    data_file = load_file("Housing.csv")

    while True:
        # print housing menu to user
        print("You have selected Housing Data from Housing.csv")
        print("Select the column you want to analyze: ")
        print("a. AGE")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Exit to Main Menu")
        user_input = input()
        if user_input == "a":
            retrieve_data("AGE", data_file)
        elif user_input == "b":
            retrieve_data("BEDRMS", data_file)
        elif user_input == "c":
            retrieve_data("BUILT", data_file)
        elif user_input == "d":
            retrieve_data("ROOMS", data_file)
        elif user_input == "e":
            retrieve_data("UTILITY", data_file)
        elif user_input == "f":
            break
        else:
            print("Invalid input. Please enter one of the options listed.")


"""Retrieve data function
Helper function to keep menu clear of excessive function calls
Calls all data analysis functions and translates results to user"""
def retrieve_data(column, file):
    # values from function calls saved to use f strings later
    total_count = col_count(column, file)
    mean = col_mean(column, file)
    std_dev = col_std_dev(column, file)
    min_val = col_min(column, file)
    max_val = col_max(column, file)

    # print data from function calls using f strings to round off decimals
    print("The statistics for column " + column + " are: ")
    print(f"Count: {total_count}")
    print(f"Mean: {mean:.1f}")
    print(f"Standard Deviation: {std_dev:.1f}")
    print(f"Min: {min_val:.1f}")
    print(f"Max: {max_val:.1f}")
    print("The Histogram for this column is now displayed.")
    col_histogram(column, file)

"""Count function
Counts the total number of values within a column"""
def col_count(col_name, file):
    # adds the total number of fields within the csv's column
    return len(file[col_name])

"""Mean function
Calculates the mean of the column"""
def col_mean(col_name, file):
    # calculates the mean value of the column
    return np.mean(file[col_name])

"""Standard Deviation function
Calculates the standard deviation of the column"""
def col_std_dev(col_name, file):
    # calculates the standard deviation of the column
    return np.std(file[col_name])

"""Min function
Calculates the minimum value of the column"""
def col_min(col_name, file):
    # calculates the minimum value of the column
    return np.min(file[col_name])

"""Max function
Calculates the maximum value of the column"""
def col_max(col_name, file):
    # calculates the maximum value of the column
    return np.max(file[col_name])

"""Histogram function
Creates a histogram of the column"""
def col_histogram(col_name, file):
    # creates a histogram of the column
    plt.hist(file[col_name])
    plt.show()

# call main_menu function to start program
main_menu()
