import json
from datetime import datetime
import pandas as pd
import plotly.express as px

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def open_json(forecast_file):
    with open("data/{}.json".format(forecast_file)) as json_file:
       json_data = json.load(json_file)
    return(json_data)

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%d %B')

def convert_f_to_c(temp_in_farenheit):
    temp_in_celcius = (temp_in_farenheit - 32) / (9/5)
    temp_in_celcius = "%.1f" % temp_in_celcius
    temp_in_celcius = float(temp_in_celcius)
    return temp_in_celcius

def get_dataframe(json_data):

    day = []
    min_temp = []
    max_temp = []
    min_realfeel = []
    min_shade = []

    for date in json_data["DailyForecasts"]:
        day.append(convert_date(date["Date"]))
        min_temp.append(convert_f_to_c(date["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(date["Temperature"]["Maximum"]["Value"]))
        min_realfeel.append(convert_f_to_c(date["RealFeelTemperature"]["Minimum"]["Value"]))
        min_shade.append(convert_f_to_c(date["RealFeelTemperatureShade"]["Minimum"]["Value"])) 

    df = pd.DataFrame({'Day': day, 'Min': min_temp, 'Max': max_temp, 'Min realfeel': min_realfeel, "Min shade": min_shade})
    return(df)

def create_graph1(df,file):
    day_start = df["Day"][0]
    day_end = df["Day"][len(df)-1]

    yaxis = "Temperature {}".format(DEGREE_SYBMOL)
    title = "Minimum and Maximum Temperatures for {} to {}, 2020. File: {}.json".format(day_start, day_end,file)

    fig = px.line(df, x = "Day", y = "Min", 
                title = title,)

    fig.update_layout(yaxis_title = yaxis, 
                    font = dict(family = 'Arial', size = 12))

    fig.update_traces(line = dict(color = 'blue', width = 2),
                    name = 'Minimum', showlegend = True,
                    mode = 'lines+markers',
                    marker = dict(color = 'Blue', size = 10,
                                line = dict(color='blue', width=2)))

    fig.add_scatter(x = df["Day"], y = df["Max"],
                    name = 'Maximum',
                    mode = 'lines+markers',
                    line = dict(color = 'red', width = 2),
                    marker = dict(color = 'red', size = 10,
                                  line = dict(color = 'red', width = 2)))

    fig.show()


def create_graph2(df,file):

    day_start = df["Day"][0]
    day_end = df["Day"][len(df)-1]
    yaxis = "Temperature {}".format(DEGREE_SYBMOL)

    title = "Min, Min Real Feel and Min Real Feel Shade Temperature: {} to {}, 2020. File: {}.json".format(day_start, day_end, file)
    fig = px.line(df, x = "Day", y = "Min", 
                title = title,)

    fig.update_layout(yaxis_title = yaxis,
                    font = dict(family = 'Arial', size = 12))

    fig.update_traces(line = dict(color = 'blue', 
                                width = 2, dash = 'dash'),
                    name = 'Minimum', showlegend = True,
                    mode = 'lines+markers',
                    marker = dict(color='blue',
                                size = 10,
                                line = dict(color = 'blue', width = 2)))

    fig.add_scatter(x = df["Day"], y = df["Min realfeel"],
                    name = 'Minimum Real Feel',
                    mode = 'lines+markers',
                    line = dict(color = 'orange', width = 2),
                    marker = dict(size = 10, line = dict(color = 'orange', width = 2)))

    fig.add_scatter(x = df["Day"], y = df["Min shade"],
                    name = "Minimum Temperature in the shade",
                    mode = 'lines+markers',
                    line = dict(color = 'purple',width = 2, dash = 'dash'),
                    marker = dict(color = 'purple', size = 10,
                                  line = dict(color = 'purple', width = 2)))
                    
    fig.show()


filename = ["forecast_5days_a","forecast_5days_b","forecast_10days"]

for file in filename:
    json_data = open_json(file)
    df = get_dataframe(json_data)
    create_graph1(df,file)
    create_graph2(df,file)
