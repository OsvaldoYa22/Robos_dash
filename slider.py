from dash import dcc, html
import dash_bootstrap_components as dbc

def render_content_slider(tab):
    if tab == 2016:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2016', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2016', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2016', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])
    
    elif tab == 2017:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2017', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2017', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2017', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])
    
    elif tab == 2018:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2018', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2018', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2018', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])
    elif tab == 2019:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2019', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2019', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2019', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])

    elif tab == 2020:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2020', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2020', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2020', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])


    elif tab == 2021:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2021', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2021', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2021', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])
    

    elif tab == 2022:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2022', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2022', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2022', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])
    
    elif tab == 2023:
        return html.Div([
##############################################################################################
            html.Div(
            style = {'display': 'flex', 'flex-wrap': 'wrap'},
            children = [
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_01_2023', figure = {}),
                            ]
                        )
                    ]
                ),
                html.Div(
                    style = {'width': '50%'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto'},
                            children = [
                                dcc.Graph(id = 'Mi_grafica_02_2023', figure = {}),
                            ]
                        )
                    ]
                ),
                
                html.Div(
                    style={'width': '100%', 'margin': '0 auto'},
                    children = [
                        html.Div(
                            style = {
                                'background-color': '#F2F2F2','border-radius': '15px',
                                'margin': '5px','padding': '7px','position': 'relative',
                                'box-shadow': '4px 4px 4px 4px lightgrey','overflow-y': 'auto' },
                            children = [
                                dcc.Graph(id = 'Mi_grafica_04_2023', figure = {}),
                            ]
                        )
                    ]
                ),
            ]
        )
        ])