from dash import dcc, html
import dash_bootstrap_components as dbc

def render_content_table(tab):
    if tab == 'tab-2':
        return html.Div([

            html.Div([

                html.Br(),
                html.P('Seleccione el origen de los datos',
                        style = {'font-weight': 'bold','background-color': '#F2F2F2',
                                'border-radius': '3px','margin': '5px',
                                'padding': '7px','position': 'relative','display': 'inline-block',
                                'box-shadow': '4px 4px 4px 4px lightgrey',
                                'overflow-y': 'auto'
                            }),
                dcc.RadioItems(id = 'origing_data',
                               labelStyle = {'display': 'inline-block',"align-items": "center", 'textAlign': 'center'},
                               options = [
                                   {'label': [
                                       html.Img(src="/assets/FGJ.png", height=60),
                                       #html.Span("FGJ",style={'font-size':15,'padding-left':10}),
                                   ], 'value': 'Data_FGJ'},
                                   {'label': [
                                       html.Img(src="/assets/C5.PNG", height=60),
                                       #html.Span("C5",style={'font-size':15,'padding-left':10,'color':'#AA1818'}),
                                   ], 'value': 'Data_C5'}
                               ], value = 'Data_FGJ',
                               #labelStyle={"display": "flex", "align-items": "center"}
                               ),
                
                html.Br(),
                
                #dcc.Graph(id="graph-circular"),
                dcc.Slider(
                    id="slider-circular", min=2016, max=2023,
                    marks={str(year): str(year) for year in range(2016, 2024)},
                    value=2016, step=1
                ),
                html.Div(id = 'tabs-content02')
                               
                ]),
##############################################################################################
        ])
    
    elif tab == 'tab-1':
        return html.Div([
            html.Div([
                html.Br(),
                html.P('Selecciona el origen de los datos', 
                       style = {'font-weight': 'bold','background-color': '#F2F2F2',
                                'border-radius': '3px','margin': '5px',
                                'padding': '7px','position': 'relative',
                                'display': 'inline-block','box-shadow': '4px 4px 4px 4px lightgrey',
                                'overflow-y': 'auto'}),
                dcc.RadioItems(id = 'origing_data',
                               labelStyle = {'display': 'inline-block',"align-items": "center", 'textAlign': 'center'},
                               options = [
                                   {'label': [
                                       html.Img(src="/assets/FGJ.png", height=60),
                                       #html.Span("FGJ",style={'font-size':15,'padding-left':10}),
                                   ], 'value': 'Data_FGJ'},
                                   {'label': [
                                       html.Img(src="/assets/C5.PNG", height=60),
                                       #html.Span("C5",style={'font-size':15,'padding-left':10,'color':'#AA1818'}),
                                   ], 'value': 'Data_C5'}
                               ], value = 'Data_FGJ',
                               #labelStyle={"display": "flex", "align-items": "center"}
                               )]), 

            html.Div(children='''
                Robos de Enero 2016 a Marzo 2023
            ''', style={'font-weight': 'bold','textAlign': 'center',
                'background-color': '#F2F2F2','margin': '5px','padding': '7px',
                'position': 'relative','box-shadow': '4px 4px 4px 4px lightgrey',
                'overflow-y': 'auto'}),
            html.Div(
                    style = {'width': '100%'},
                    children = [
                        html.Div(
                            style = {'background-color': '#F2F2F2',
                                'border-radius': '15px','margin': '5px',
                                'padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey',
                                'overflow-y': 'auto'
                            },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_ST_1', figure = {}),
                            ]
                        )
                    ]
                ),
            
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {'font-weight': 'bold',
                                'textAlign': 'center','background-color': '#F2F2F2',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = ['''
                                Valores predecidos, NNAR(31,1,16)[366] 
                            '''
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {'font-weight': 'bold',
                                'textAlign': 'center','background-color': '#F2F2F2',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = ['''
                                Distribución de los residuos
                            ''']
                        )
                    ]
                )
                
            ]
        ),

            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_ST_2', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px', 'padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_ST_3', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        ),

        html.Br(),

        html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'textAlign': 'center',
                               },
                            children = [
                                dbc.Button("Descarga los valores", id="btn-download-txt", color="primary", className="me-1" ),
                                dcc.Download(id="download-text_02")
                                
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'textAlign': 'center',
                            },
                            children = [
                                dbc.Button("Descarga más detalles", id="btn-download-txt", color="primary", className="me-1" ),
                                dcc.Download(id="download-text_01")
                            ]
                        )
                    ]
                )

            ]
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
            
        ])
