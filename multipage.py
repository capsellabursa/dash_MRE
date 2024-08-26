# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:51:01 2024

@author: avigailshn
"""

import dash
from dash import html, dcc, Output, Input
from threading import Timer
import webbrowser
import dash_bootstrap_components as dbc

CUSTOME_FONT = {
    'font-family': 'Arial serif'
    }

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 2,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#B0BACE"
}

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LUX])
sidebar = html.Div([
    html.Br(),
    html.Hr(),
    html.H5("Sample number:", className="display-10"),
    html.Div(dbc.Input(id='input-number', type='text', placeholder="999", debounce=True)),
    html.Br(),
    dbc.Nav(
    #
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-1"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            #className="bg-light",
   )
],style=SIDEBAR_STYLE)
app.layout = dbc.Container([
    dbc.Row([
    ]),

    
    
    dcc.Store(id='store', data={}),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=15, sm=15, md=8, lg=8, xl=8, xxl=8),

            dbc.Col(
                [
                    dash.page_container
                ], xs=15, sm=15, md=15, lg=15, xl=15, xxl=15)
        ]
    )
], fluid=True)

@app.callback(
    Output("store", "data"),
    Input("input-number", "value"),
    )

def get_value(number):
    return number
    
if __name__ == '__main__':
    Timer(1, webbrowser.open_new("http://127.0.0.1:8050/")).start()
    app.run_server(dev_tools_hot_reload=False)