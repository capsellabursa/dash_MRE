# -*- coding: utf-8 -*-
import dash
from dash import html, dash_table, Input, Output, State, callback
import pandas as pd
import os
import glob
from collections import OrderedDict
import numpy as np
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=1)

# App layout
layout = html.Div([
    html.Div([
        #dbc.Input(id='input-number', type='text', placeholder="Enter number", debounce=True),
        html.Div([dbc.Button('Load data', id='submit-button', n_clicks=0)], 
                  className='d-grid gap-2'),
        html.Div(
            id='datatable-interactivity',      
        ), html.Div(id='table-dropdown-container')
    ], className='container'),
    html.Br(),
    html.Br(),

    html.Div(id='display_selected_row', className='container')
])

# Callback to update selected row display
@callback(
    Output('datatable-interactivity', "children"),
    [Input('submit-button', 'n_clicks')],
    [State('store', 'data')]
)
def update_table(n_clicks, store):
    number=store
    if n_clicks > 0:
        
        pattern = f"C://Users//avigailshn//MRA//Data//{number}-*"
        matching_dirs = glob.glob(pattern)
        
        if not matching_dirs:
            return []

        dir_path = matching_dirs[0]
        os.chdir(dir_path)

        excel_pattern = f"{number}_table.xlsx"
        excel_file = glob.glob(excel_pattern)
        
        if not excel_file:
            return []

        excel_path = excel_file[0]
        support_data = pd.DataFrame(OrderedDict(pd.read_excel(excel_path, index_col=0)))

        return dash_table.DataTable(
            id='datatable-interactivity',
            data=support_data.to_dict('records'),
            columns=[
                {'id': 'Chromosome', 'name': 'Chromosome'},
                {'id': 'start', 'name': 'start'},
                {'id': 'end', 'name': 'end'},
                {'id': 'Aberration', 'name': 'Aberration'},
                {'id': 'Tier', 'name': 'Tier', 'presentation': 'dropdown'}
            ],
            editable=True,  # Sorting enabled
            dropdown = {'Tier': {
                 'options': [
                    {'label': i, 'value': i}
                    for i in np.array(['Tier III', 'Tier II', 'Tier I'])
                ]
            }},
            row_selectable="multi",
            selected_rows=[],
            sort_action="native",
            sort_mode="multi",
            column_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            page_action="native",
            page_current= 0,
            style_table={'height' : '500px',
                         'overflowX': 'auto',
                         'overflowY': 'auto'},
            
            style_cell={'textAlign': 'left',
                        'height': 'auto',
                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                        'whiteSpace': 'normal'},
                        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Date', 'Region']
        ],
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
            'color': 'black',
            'backgroundColor': 'white'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ],      
        )

    #return []

@callback(
    Output('display_selected_row', "children"),
    [Input('datatable-interactivity', "selected_rows")],
    [State('datatable-interactivity', "data")]
)
def display_selected_row_details(selected_rows, data):

    if selected_rows is None:
        selected_rows = []

    if not data:
        return html.Div()

    dff = pd.DataFrame(data)

    selected_data = dff.iloc[selected_rows]

    return html.Div([

        dash_table.DataTable(
        id='display_selected_row_data_table',
        columns=[{"name": i, "id": i} for i in selected_data.columns],
        data=selected_data.to_dict("records"),
        export_format='xlsx',
        export_headers='display',
        ##### DROPDOWN
        dropdown={
                   "Tier": {
                        'options': [
                            {'label': i, 'value': i}
                            for i in ['Tier III/IV', 'Tier I', 'Tier II']
                            ]
                        }
                    },
        editable=True,
        style_table={'height' : '500px',
                     'overflowX': 'auto',
                     'overflowY': 'auto'},
        
        style_cell={'textAlign': 'left',
                    'height': 'auto',
                    'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                    'whiteSpace': 'normal'},
                    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'color': 'black',
        'backgroundColor': 'white'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(220, 220, 220)',
        }
    ],
    style_header={
        'backgroundColor': 'rgb(210, 210, 210)',
        'color': 'black',
        'fontWeight': 'bold'
    }

    )
])


