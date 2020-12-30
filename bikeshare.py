import time
import pandas as pd
import numpy as np
import os

def cls():
    """clear screen
    source: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console"""
    
    os.system('cls' if os.name=='nt' else 'clear')
    
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        cls()
        welcome1 = '¤' * 84 + '\n'
        welcome2 = '¤                  Hello! Let\'s explore some US bikeshare data!                    ¤\n'
        full_message = welcome1 + welcome2 + welcome1
        print(full_message)

        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        valid_city = 'no'
        message = 'We have available data for chicago, new york city and washington. Which city would you like to explore?'
        print(message)  
        full_message += '\n' + message

        while valid_city == 'no':   
            city = input().lower()
            if city != 'chicago' and city != 'new york city' and city != 'washington':
                cls()
                print (full_message)
                print('Ooops! Looks like your input is not accepted. Can you enter the city again?')
            else:
                valid_city = 'yes'
        else:
            cls()
            print(full_message)
            message='Great! You have selected ' + city.upper() + '.'
            print(message)
            full_message = full_message + '\n' + message

        # TO DO: get user input for month (all, january, february, ... , june)

        valid_month = 'no'    
        message = 'Which month would you like to explore? Would you want to see \'all\' or for only a specific month from \'january\' to \'june\'?'
        print(message)  
        full_message += '\n' + message

        while valid_month == 'no':   
            month = input().lower()
            if month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
                cls()
                print(full_message)
                print('Ooops! Looks like your input is not accepted. Can you enter the month again?')
            else:
                valid_month = 'yes'
        else:
            cls()
            print(full_message)
            if month == 'all':
                message='You have selected the data for ALL months.'
                month_message = ' of ALL the available months'
            else:
                message='You have selected to see the data for the month of ' + month.upper() + ' only.'
                month_message = ' of the month of ' + month.upper()
            print(message)
            full_message += '\n' + message

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        valid_day = 'no'
        message = 'Which day of the week would you like to explore? Would you want to see \'all\' or for only specific day from \'monday\' to \'sunday\'?'
        print(message)  
        full_message += '\n' + message    
        while valid_day == 'no':
            day = input().lower()
            if day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
                cls()
                print(full_message)
                print('Ooops! Looks like your input is not accepted. Can you enter your answer again?')
            else:
                valid_day = 'yes'
        else:
            cls()
            if day == 'all':
                message='You have selected to see the data for ALL days of the week.\n'
                day_message = ' for ALL days of the week'
            else:
                message='You have selected to see the data for every ' + day.upper() + ' only.\n'
                day_message = ' for every ' + day.upper()
            full_message += '\n' + message      
            print(full_message)
                
        print('You wish to explore bikeshare data from ' + city.upper() + day_message + month_message + '.\nEnter any key to confirm. Or input \'restart\' to reinitiate the program.')
        answer = input()
        if answer.lower() != 'restart':
            print('Thanks for the confirmation!\n')
            break
        
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
        
    """Create columns for Month, Day of Week, Hour from Start Time"""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start-Month'] = df['Start Time'].dt.month_name()
    df['Start-Day of Week'] = df['Start Time'].dt.day_name()
    df['Start-Hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df.loc[df['Start-Month'] == month.title()]
    
    if day != 'all':
        df = df.loc[df['Start-Day of Week'] == day.title()]  
    
    df.fillna(0)
    
    return df

def display_data(df):
    start = 0
    end = 5
    message = 'Would you like to see the first 5 rows? Enter any key for yes or enter \'no\' to proceed to the data statistics.\n' 
    
    """Show all columns
    Source: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe"""
    pd.set_option('display.max_columns',12)
    
    while True:
        answer = input(message)
        if answer.lower() == 'no':
            break
        if df[start:end].empty:
            print('\n'+'*'*110+'\nEnd of Rows. Proceeding to display the data statistics...')
            break
        print(df[start:end])
        start+=5
        end+=5
        message = ('\n'+'*'*110)+'\nWould you like to see the next 5 rows? Enter any key for yes or enter \'no\' to proceed to the data statistics.\n'

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n')
    print('*'*37)
    print('*   Most Frequent Times of Travel   *')
    print('*'*37)
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['Start-Month'].mode()[0]
    print('\nMost Common Month: ', common_month) 

    # TO DO: display the most common day of week
    common_dayofweek = df['Start-Day of Week'].mode()[0]
    print('Most Common Day of Week: ', common_dayofweek)

    # TO DO: display the most common start hour
    common_hour = df['Start-Hour'].mode()[0]
    print('Most Common Hours: ', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    answer = input('\nEnter any key to see the next statistics.\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('*'*37)
    print('*   Most Popular Stations & Trip    *')
    print('*'*37)
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print('\nMost Commonly Used Start Station: ', common_startstation)

    # TO DO: display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End Station trip'] = df['Start Station'] + " to " + df['End Station']
    common_stationcombination = df['Start to End Station trip'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station trip: ', common_stationcombination)

    print("\nThis took %s seconds." % (time.time() - start_time))  
    answer = input('\nEnter any key to see the next statistics.\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    

    print('*'*37)
    print('*           Trip Duration           *')
    print('*'*37)
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    print('\nTotal Travel Time: ',total_travel_time.round(), ' hours')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('Mean Travel Time: ',mean_travel_time.round(), ' minutes')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    answer = input('\nEnter any key to see the next statistics.\n')

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('*'*37)
    print('*          User Statistics          *')
    print('*'*37)
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCount per User Type:\n', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nCount per Gender:\n', gender)
    except:
        print('\nNo available data for Gender\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest Birth Year: ', earliest_birth_year)
        recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year: ', recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth: ', common_birth_year)
    except:
        print('No available data for Birth year\n')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        cls()

        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter \'yes\' to restart or enter any key to exit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
