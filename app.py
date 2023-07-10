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
# RESIDUOS_01 
@app.callback(
    Output("download-text_01", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,)
def func_time(n_clicks):
    return func(n_clicks)
# GRAFICA ST 1 
@app.callback(Output('Mi_grafica_ST_1', 'figure'),
              Input('origing_data', 'value'))
def update_graph_s(value):
    return update_graph_ST1(value)  
# GRAFICA ST 2 
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
# GRAFICA 1 
@app.callback(Output('Mi_grafica_01_2016', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2016(value)
# GRAFICA 2 
@app.callback( 
    Output('Mi_grafica_02_2016', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2016(value)
# GRAFICA 4 
@app.callback( 
    Output('Mi_grafica_04_2016', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2016(value)


# GRAFICA 1 2017
@app.callback(Output('Mi_grafica_01_2017', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2017(value)
# GRAFICA 2 2017
@app.callback( 
    Output('Mi_grafica_02_2017', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2017(value)
# GRAFICA 4 2017
@app.callback( 
    Output('Mi_grafica_04_2017', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2017(value)


# GRAFICA 1 2018 
@app.callback(Output('Mi_grafica_01_2018', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2018(value)
# GRAFICA 2 2018
@app.callback( 
    Output('Mi_grafica_02_2018', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2018(value)
# GRAFICA 4 2018
@app.callback( 
    Output('Mi_grafica_04_2018', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2018(value)


# GRAFICA 1 2019
@app.callback(Output('Mi_grafica_01_2019', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2019(value)
# GRAFICA 2 2019
@app.callback( 
    Output('Mi_grafica_02_2019', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2019(value)
# GRAFICA 4 2019
@app.callback( 
    Output('Mi_grafica_04_2019', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2029(value)


# GRAFICA 1 2020
@app.callback(Output('Mi_grafica_01_2020', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2020(value)
# GRAFICA 2 2020
@app.callback( 
    Output('Mi_grafica_02_2020', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2020(value)
# GRAFICA 4 2020
@app.callback( 
    Output('Mi_grafica_04_2020', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2020(value)


# GRAFICA 1 2021
@app.callback(Output('Mi_grafica_01_2021', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2021(value)
# GRAFICA 2 2021
@app.callback( 
    Output('Mi_grafica_02_2021', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2021(value)
# GRAFICA 4  2021
@app.callback( 
    Output('Mi_grafica_04_2021', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2021(value)


# GRAFICA 1 2022
@app.callback(Output('Mi_grafica_01_2022', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2022(value)
# GRAFICA 2 2022
@app.callback( 
    Output('Mi_grafica_02_2022', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2022(value)
# GRAFICA 4 2022
@app.callback( 
    Output('Mi_grafica_04_2022', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2022(value)


# GRAFICA 1 2023
@app.callback(Output('Mi_grafica_01_2023', 'figure'),
              Input('origing_data', 'value'))
def update_graph(value):
    return update_graph_01_2023(value)
# GRAFICA 2 2023
@app.callback( 
    Output('Mi_grafica_02_2023', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_02_2023(value)
# GRAFICA 4 2023 
@app.callback( 
    Output('Mi_grafica_04_2023', component_property = 'figure'),
    [Input('origing_data', component_property = 'value')])
def update_graph(value):
    return update_graph_04_2023(value)


if __name__ == '__main__':
    app.run_server(debug=True)