import numpy as np
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.figure_factory as ff

## ANALISIS ECONOMETRICO
data3 = gpd.read_file('assets/FRECUENCIA_ROBOS_DIARIA.csv')
data3['Fecha'] = pd.to_datetime(data3['Fecha']).dt.strftime('%Y-%m-%d')
data3['Frecuencia'] = pd.to_numeric(data3['Frecuencia'], errors='coerce').fillna(0)
data4 = gpd.read_file('assets/PRONOSTICO_DIARIO.csv')
data4['Fecha'] = pd.to_datetime(data4['Fecha']).dt.strftime('%Y-%m-%d')
data4['Frecuencia'] = pd.to_numeric(data4['Frecuencia'], errors='coerce').fillna(0)
data5 = gpd.read_file('assets/RESIDUALES_DIARIO.csv')
data5['forecast'] = data5['forecast'].astype(float)

# RESIDUOS_01 
def func(n_clicks):
    return dict(content='''
    Ljung-Box test

data:  Residuals from NNAR(31,1,16)[365]
Q* = 588.49, df = 529, p-value = 0.03714

Model df: 0.   Total lags used: 529
    ''', filename="Residuales_DIA.txt")

# GRAFICA ST 1 
def update_graph_ST1(value):
    fig = None
    if value == 'Data_FGJ':
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data3['Fecha'], y=data3['Frecuencia'], name="Delitos FGR"))
        fig.update_layout(
            #title="Robos en CDMX",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label="3 mo", step="month", stepmode="backward"),
                        dict(count=6, label="6 mo", step="month", stepmode="backward"),
                        dict(count=1, label="1 yr", step="year", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(step="all")
                    ])
                ),
                #rangeslider=dict(type="date")
            ),
            yaxis=dict(title="Número de Robos")
        )
        #fig = px.line(data3, x = 'Fecha', y = 'Frecuencia')
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(margin = dict(t = 15, l = 7, r = 7, b = 5)) 
    else:
        x = np.linspace(0, 10, 100)
        y = 2 * x  
        fig = px.line(x = x, y = y)
    return fig
        
# GRAFICA ST 2 
def update_graph_ST2(value):
    fig = None
    if value == 'Data_FGJ':
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data4['Fecha'], y=data4['Frecuencia'], name="Pronostico"))
        fig.update_layout(
            #title="Robos en CDMX",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=3, label="3 mo", step="month", stepmode="backward"),
                        dict(count=6, label="6 mo", step="month", stepmode="backward"),
                        dict(count=1, label="1 yr", step="year", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(step="all")
                    ])
                ),
                #rangeslider=dict(type="date")
            ),
            yaxis=dict(title="Número de Robos")
        )
        #fig = px.line(data3, x = 'Fecha', y = 'Frecuencia')
        fig.update_xaxes(rangeslider_visible=True)
        fig.update_layout(margin = dict(t = 15, l = 7, r = 7, b = 5))#modebar_remove= 
    else:
        x = np.linspace(0, 10, 100)
        y = 2 * x  
        fig = px.line(x = x, y = y)
    return fig
        
# GRAFICA ST 3 
def update_graph_ST3(value):
    #fig = None
    if value == 'Data_FGJ':
        fig = go.Figure()
        #fig = px.histogram(data5, x="time", y="forecast", marginal="rug",hover_data=data5.columns)
        #fig = ff.create_distplot([data4['Frecuencia']], ['Residuales'], show_hist=True, show_curve=True, show_rug=True)
        fig = ff.create_distplot([data5['forecast']], ['Residuales'], show_hist=True, show_curve=True, show_rug=True)
        #fig = ff.create_distplot([data5['forecast']]  )#show_hist=True, show_curve=True, show_rug=True)
        fig.update_layout(margin = dict(t = 15, l = 7, r = 7, b = 5),showlegend=False) 
    else:
        x = np.linspace(0, 10, 100)
        y = 2 * x  
        fig = px.line(x = x, y = y)
    return fig
