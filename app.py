### Importa las librerías necesarias
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#### Locales
from table_structure import render_content_table
from slider import render_content_slider
from time_series import *
from descriptive_analysis import * 

# Estilos externos
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        [dbc.themes.BOOTSTRAP]]
# Inicializa la app Dash
app = Dash(__name__, external_stylesheets = external_stylesheets, suppress_callback_exceptions = True)
server = app.server
# Diseño de la app
app.layout = html.Div([
    html.Div([
        html.H1('ROBOS EN CDMX', style = {'textAlign': 'center', 'height': '75px', 'margin': '0px -10px 10px', 'background-color': '#FFFFFF', 'border-radius': '2px', 'display': 'block'})]),
    dcc.Tabs(id = "tabs", value = 'tab-1', children = [
        dcc.Tab(label = 'ANALISIS DESCRIPTIVO', value = 'tab-2'),
        dcc.Tab(label = 'ANALISIS ECONOMETRICO', value = 'tab-1')]),
    html.Div(id = 'tabs-content')
])

# Contenido de cada table 
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content_tab(tab):
    return render_content_table(tab)
    
# Control deslizante
@app.callback(Output('tabs-content02', 'children'),
              Input('slider-circular', 'value'))
def render_content_slid(tab):
    return render_content_slider(tab)


### SERIES DE TIEMPO
@app.callback(
    Output("download-text_01", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,)
def func_time(n_clicks):
    return func(n_clicks)

@app.callback(Output('Mi_grafica_ST_1', 'figure'),
              Input('origing_data', 'value'))
def update_graph_s(value):
    return update_graph_ST1(value)  
 
@app.callback(Output('Mi_grafica_ST_2', 'figure'),
              Input('origing_data', 'value'))
def update_graph_st(value):
    return update_graph_ST2(value) 
# GRAFICA ST 3 
@app.callback(Output('Mi_grafica_ST_3', 'figure'),
              Input('origing_data', 'value'))
def update_sts_3(value):
    return update_graph_ST3(value)
        

### ANALISIS DESCRIPTIVO        

@app.callback(Output('Mi_grafica_01_2016', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2016(value)

@app.callback( 
    Output('Mi_grafica_02_2016', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2016(value)

@app.callback( 
    Output('Mi_grafica_04_2016', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2016(value)



if __name__ == '__main__':
    app.run_server(debug=False)
