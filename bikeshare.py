import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. If the user inputs invalid data, he will get that information until he inputs valid information.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day = ''
    
    while city not in CITY_DATA.keys():
        city = input('Would you like to see data for Chicago, New York City or Washington?\n').lower()
        if city not in CITY_DATA.keys():
            print('No valid city, please try again.')
        else:
            print('You selected {}. Great!'.format(city))
    


    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february', 'march', 'april', 'may' , 'june']
    while month not in month_list:
        month = input('Would you like to filter by month? If no, please type in \'all\'. If yes, please select from january, february, march, april, may, june.\n').lower()
        if month not in month_list:
            print('No valid input, please try again.')
        else:
            print('You selected {}. Great!'.format(month))
    


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in day_list:
        day = input('Would you like to filter by day? If no, please type in \'all\'. If yes, please type in weekday.\n').lower()
        if day not in day_list:
            print('No valid input, please try again.')
        else:
            print('You selected {}. Great!'.format(day))


    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()
    print('The most common month is: {}'.format(common_month[0]))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print('The most common day is: {}'.format(common_day[0]))


    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()
    print('The most common hour is: {}'.format(common_hour[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('The most common Start Station is: {}'.format(common_start_station[0]))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('The most common End Station is: {}'.format(common_end_station[0]))


    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()
    print('The most common trip is from: {}'.format(common_trip[0]))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is {} seconds'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('The mean travel time is {} seconds'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_dict()
    print('The number of user types is:')
    for ut, count in user_types.items():
        print('{}: {}'.format(ut, count))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts().to_dict()
        print('\nThe count per gender is:')
        for g, count in genders.items():
            print('{}: {}'.format(g, count))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth is {}'.format(int(df['Birth Year'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    """Displays raw data if user wants to."""
    
    r = 0
    while True:
        rows_left = len(df) - r
        rows_to_display = min(rows_left, 5)
        
        if rows_to_display > 0 and rows_left > 5:
            print(df[r:r+rows_to_display])
            r += 5
        elif rows_to_display > 0 and rows_left <= 5:
            print(df[r:r+rows_to_display])
            print("End of dataset reached. No more data to display.")
            break
        else:
            print("End of dataset reached. No more data to display.")
            break
        
        next_rows = input('\nWould you like to see the next 5 rows? Enter yes or no.\n')
        if next_rows.lower() != 'yes':
            break
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if display.lower() == 'yes':
            display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
