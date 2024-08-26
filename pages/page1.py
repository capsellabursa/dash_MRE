# -*- coding: utf-8 -*-

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/',  external_stylesheets=[dbc.themes.FLATLY])

layout = html.Div([
    html.H2('Tool'),
    html.Hr(),
    html.Br(),
    html.H4('Welcome to the home page of Tool'),
    dbc.Accordion([
        dbc.AccordionItem(
            [html.P('This is a tool for conversion and annotation'),
             ], title="results converter"),
        dbc.AccordionItem(
            [html.P('Report selection')
             ], title="This is a tool for selection of relevant data for report")
        ])
], className='container')
