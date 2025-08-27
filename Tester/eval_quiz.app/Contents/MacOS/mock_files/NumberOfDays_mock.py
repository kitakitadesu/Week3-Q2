# '''
# Find the number of days in the given month and year 
#     Leap year (where February has 29 days) is the year that is either
#         - a divisible by 400 OR
#         - b divisible by 4 but not divisible by 100
#         Examples of leap year: 2000, 2020, 2024, 4, 40
#         Examples of non-leap year (February has 28 days): 2025, 2019, 2100, 100
#     If input doesn't exist return 'Error'
# '''
# Student do quiz here below
# do not change the function name
# do not change the function input
def NumberOfDays(month,year):
    if month <= 0 or month > 12:
        return 'Error'
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,9,11]:
        return 30
    if year % 400 == 0 or (year %4 == 0 and year %100 != 0):
        return 29
    return 28
