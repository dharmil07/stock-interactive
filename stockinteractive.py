import plotly

import plotly as py
import plotly.graph_objs as go 

plotly.tools.set_credentials_file(username='themysterious07', api_key='wzM34UdHWbsrIoc6df3N')

from datetime import datetime
import pandas as pd

df = pd.read_csv('C:\Dharmil Imp\Projects\Stocks Interactive\portfolio_data.csv')

trace_0 = go.Scatter(
    x=df.Date,
    y=df['AMZN'],
    name = "Amazon",
    line = dict(color = '#00CC00'),
    opacity = 0.8)

trace_1 = go.Scatter(
    x=df.Date,
    y=df['BTC'],
    name = "Bitcoin",
    line = dict(color = '#0000CC'),
    opacity = 0.8)

trace_2 = go.Scatter(
    x=df.Date,
    y=df['NFLX'],
    name = "Netflix",
    line = dict(color = '#CC0000'),
    opacity = 0.8)

data = [trace_0,trace_1,trace_2]
layout = dict(
    title='Stock Market Prices',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.26,
                              xanchor='center', yanchor='top',
                              text='Conceptualized by Dharmil Sanghavi',
                              font=dict(family='Arial',
                                        size=15,
                                        color='rgb(37,37,37)'),
                              showarrow=False))

layout['annotations'] = annotations

fig = dict(data=data, layout=layout)
py.offline.plot(fig)