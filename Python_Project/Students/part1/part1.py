import json
from datetime import datetime


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    temp = str(temp)
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    temp_in_celsius = (temp_in_farenheit - 32) / (9/5)
    temp_in_celsius = round(temp_in_celsius,1)
    return temp_in_celsius

def calculate_mean(total, num_items):
    mean = round((total/num_items),1)
    return mean

def process_weather(forecast_file):
    with open(forecast_file) as json_file:
        forecast_data = json.load(json_file)
        
    min_temp_lst = []
    date_lst = []
    max_temp_lst = []
    output = ""

    for date in forecast_data['DailyForecasts']:

        day_date = (date["Date"])
        formatted_date = convert_date (day_date)
        date_lst.append(formatted_date)

        min_temp_in_farenheit = (date["Temperature"]["Minimum"]["Value"])
        min_temp_in_celsius = convert_f_to_c(min_temp_in_farenheit)
        min_temp_lst.append(min_temp_in_celsius)
        
        max_temp_in_farenheit = (date["Temperature"]["Maximum"]["Value"])
        max_temp_in_celsius = convert_f_to_c(max_temp_in_farenheit)
        max_temp_lst.append(max_temp_in_celsius)
        
        long_phrase_day = (date["Day"]["LongPhrase"])
        rain_chance_day = (date["Day"]["RainProbability"])
        long_phrase_night = (date["Night"]["LongPhrase"])
        rain_chance_night = (date["Night"]["RainProbability"])
        
        output += f"""\n-------- {formatted_date} --------
Minimum Temperature:{min_temp_in_celsius: .1f}{DEGREE_SYBMOL}
Maximum Temperature:{max_temp_in_celsius : .1f}{DEGREE_SYBMOL}
Daytime: {long_phrase_day}
    Chance of rain:  {rain_chance_day}%
Nighttime: {long_phrase_night}
    Chance of rain:  {rain_chance_night}%\n""" 

    minimum_temp = min (min_temp_lst)
    minimum_index = min_temp_lst.index(minimum_temp)
    minimum_date = date_lst[minimum_index]

    maximum_temp = max (max_temp_lst)
    maximum_index = max_temp_lst.index(maximum_temp)
    maximum_date = date_lst[maximum_index]

    average_low = (sum(min_temp_lst)/len(min_temp_lst))
    average_high = (sum(max_temp_lst)/len(max_temp_lst))

    final_output = f"""{len(date_lst)} Day Overview
    The lowest temperature will be {minimum_temp:.1f}{DEGREE_SYBMOL}, and will occur on {minimum_date}.
    The highest temperature will be {maximum_temp:.1f}{DEGREE_SYBMOL}, and will occur on {maximum_date}.
    The average low this week is {average_low:.1f}{DEGREE_SYBMOL}.
    The average high this week is {average_high:.1f}{DEGREE_SYBMOL}.""" 
    
    final = final_output + "\n" + output + "\n"

    return (final)

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))




