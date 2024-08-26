# -*- coding: utf-8 -*-
import dash
from dash import dcc, html, Input, Output, State, dash_table, callback
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import dash_bootstrap_components as dbc




CUSTOME_FONT = {
    'font-family': 'Arial serif'
    }


tabs_styles = {
    'height': '44px',
    'width': '600px',
    'justifyContent': 'center'
}
tab_style = {
    #'borderBottom': '1px solid #d6d6d6',
    #'padding': '0px 24px',
    'fontWeight': 'bold',
    'fontColor': 'black',
    'borderTopLeftRadius': '10px',
    'borderTopRightRadius': '10px',
    'borderTop': '0px solid #d6d6d6',
    'borderLeft': '1px solid #d6d6d6',
    'borderLight': '1px solid #d6d6d6',
    'borderBottom': '3px solid #d6d6d6',
    'backgroundColor': '#fafbfc',
    'padding': '12px',
    'color': '#d6d6d6',
    'alignItem': 'center'
}

tab_selected_style = {
    'borderTopLeftRadius': '10px',
    'borderTopRightRadius': '10px',
    'borderTop': '1px solid #B0BACE',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#B0BACE',
    'color': 'black',
    'padding': '6px'
}


# the style arguments for the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": '150px',
    "left": '18px',
    'borderTopLeftRadius': '10px',
    'borderTopRightRadius': '10px',
    'borderBottomRightRadius': '10px',
    'borderBottomLeftRadius': '10px',
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 1rem",
    "background-color": "#B0BACE",
    'height': '15rem'
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.



dash.register_page(__name__, order=2, external_stylesheets=[dbc.themes.FLATLY])
html.Title("OGM")
# Define App Layout
layout = html.Div([
        # Main content
        html.Div([dbc.Button('Load data', id='submit-button', n_clicks=0,color='secondary', outline=True)], 
                  className='d-grid gap-2'),
        html.Br(),
        html.Div([
            dcc.Tabs(id='tabs', value='tab-1', children=[
                dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style)
            ]),
            html.Div(id='tabs-content')
        ], style=tabs_styles, className='content'),
    ], className='container')


# Define Callbacks
@callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value')],
    Input('submit-button', 'n_clicks'),
    [State('store', 'data')]
)


def update_output(tab, n_clicks, number):
    number = number
################################### SCP ########################################
    support_tab = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ['f{number}', 'B', 'C', 'D']}
    fish_tab = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ['f{number}', 'B', 'C', 'D']}
    OGM_results = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ['f{number}', 'B', 'C', 'D']}
    exons_tab = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ['f{number}', 'B', 'C', 'D']}
    gene_tab = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ['f{number}', 'B', 'C', 'D']}
    sophia_overlap = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ["A", 'f{number}', 'C', 'D']}
    another_variants = {'column 1': [1, 2 , 3 , 4],
                   'column 2': ["A", 'B', 'f{number}', 'D']}
    

    if n_clicks > 0:
         if tab == 'tab-1':
             df_tab2 = pd.DataFrame(support_tab)
             return html.Div([ 
                 html.H3(f'{number}'),
                 html.Div([
    ####Support tab
                html.H4('Support Table'),
                dash_table.DataTable(
                    id='support_table',
                    columns=[{"name": i, "id": i} for i in df_tab2.columns],
                    data=df_tab2.to_dict('records'),
                    editable=True,
                    filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        export_format='xlsx',
        export_headers='display',
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
               ], style={'width': '200%',"display": "inline-block"})
            ])
         elif tab == 'tab-2':
             df_tab3 = pd.DataFrame(fish_tab)
             df_tab4 = pd.DataFrame(OGM_results)
             return html.Div([
                 html.Div([
                html.H4('FISH Table'),
                dash_table.DataTable(
                    id='ogm_table',
                    columns=[{"name": i, "id": i} for i in df_tab3.columns],
                    data=df_tab3.to_dict('records'), editable=True,
                    filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        export_format='xlsx',
        export_headers='display',
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

                ),
        ##### FISH tab
                html.H4('OGM Table'),
                dash_table.DataTable(
                    id='fish_table',
                    columns=[{"name": i, "id": i} for i in df_tab4.columns],
                    data=df_tab4.to_dict('records'), editable=True,
                    filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        export_format='xlsx',
        export_headers='display',
        style_table={'overflowX': 'auto',
                     'overflowY': 'auto',
                     'height' : '500px'},
        
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
                ], style={'width': '200%',"display": "inline-block"})
                ])
         elif tab == 'tab-3':
             df_tab5 = pd.DataFrame(exons_tab)
             df_tab6 = pd.DataFrame(gene_tab)
             df_tab7 = pd.DataFrame(sophia_overlap)
             df_tab8 = pd.DataFrame(another_variants)
             return html.Div([
                 html.Div([
                html.H4('NGS panel: exons and regulation'),
                dash_table.DataTable(
                    id='exon_table',
                    columns=[{"name": i, "id": i} for i in df_tab5.columns],
                    data=df_tab5.to_dict('records'), editable=True,
                    filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        style_table={'overflowX': 'auto',
                     'overflowY': 'auto',
                     'height' : '500px'},
        
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

                ),
                
    ###### NGS tabs
                html.H4('NGS Table'),
                dash_table.DataTable(
                    id='ngs_table',
                    columns=[{"name": i, "id": i} for i in df_tab6.columns],
                    data=df_tab6.to_dict('records'), editable=True,
                    filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
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

                ),
####### Sophia tab
        html.H4('Overlapped SOPHiA results'),
        dash_table.DataTable(
        id='exon_table',
        columns=[{"name": i, "id": i} for i in df_tab7.columns],
        data=df_tab7.to_dict('records'), editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        style_table={'overflowX': 'auto',
                 'overflowY': 'auto',
                 'height' : '500px'},
    
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

            ),
####### Sophia another variants
        html.H4('Another SOPHiA results'),
        dash_table.DataTable(
        id='exon_table',
        columns=[{"name": i, "id": i} for i in df_tab8.columns],
        data=df_tab8.to_dict('records'), editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        style_table={'overflowX': 'auto',
                 'overflowY': 'auto',
                 'height' : '500px'},
    
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

            ),
                ],style={'width': '200%',"display": "inline-block"})
                ])
         else:
             return html.Div('Error')
         