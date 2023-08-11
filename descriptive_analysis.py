import numpy as np
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.figure_factory as ff

conteo_fecha =  pd.read_csv('assets/FRECUENCIA_FECHAS.csv')
conteo_colonia = pd.read_csv('assets/COLONIAS.csv')
shape = gpd.read_file('assets/COLONIAS.shp')
shape = shape.to_crs("EPSG:4326")



### ANALISIS DESCRIPTIVO        

def update_graph_01(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
                 color='NOMDT',
                 color_continuous_scale='orrd',
                 hover_data={'NOMUT': True, 'ROBOS': ':,.0f'})
                 #hover_data={'NOMUT': True, 'ROBOS': ':,'})
        
        fig.update_traces(marker=dict(cornerradius=5))
        fig.update_traces(hovertemplate='<b>%{label}<br>ROBOS: %{customdata[1]:,.0f}')

        fig.update_layout(margin = dict(t = 15, l = 7, r = 7, b = 5,)) 
    else:
        x = np.linspace(0, 10, 100)
        y = 2 * x  
        fig = px.line(x = x, y = y)
    return fig

# GRAFICA 2 

def update_graph_02(value):
    if value == 'Data_FGJ':
        
        colores_personalizados = [#"black",     # Para "Robos en CDMX"
                          "#FEDDDD", ## Dos primeras
                          "#E28B8B",   # enero
                          "#DF6F6F",   # abril
                          "#E28B8B",   # septiembre

                          "#DE0000",   # octubre
                          "#DF5B5B",   # noviembre
                          "#DF6F6F",   # mayo
                          "#E0A5A5",   # julio
                          "#DF4545",   # febrero
                          "#DF4545",   # marzo y dos primeros
                          "#DE1717",   # diciembre
                          "#E07F7F",   # agosto
                          "#DFB0B0"    # junio
                          ]
        #colores_personalizados = px.colors.sequential.Reds
        fig = px.treemap(conteo_fecha, path = [px.Constant("Robos CDMX"), 'mes','dia'], values = 'Frecuencia',
                         color = 'mes', 
                         color_continuous_scale = 'orrd',
                         hover_data={'Frecuencia': ':,.0f'},
                         #color_discrete_sequence=colores_personalizados
                         #marker_colors = colores_personalizados
                        )
        
        fig.update_traces(marker=dict(cornerradius=5), 
                  hovertemplate='<b>%{label}<br>ROBOS: %{customdata[0]}',
                  insidetextfont=dict(color='white'),  # Opcional: para que el texto dentro de las cajas sea blanco
                  textfont_color='black',  # Opcional: para que el texto fuera de las cajas sea negro
                  #textinfo='label+value+percent parent'
                  )
        

        fig.update_layout(margin = dict(t = 10, l = 7, r = 7, b = 5))   
    else:
        x = np.linspace(0, 10, 100)
        y = 6 * x  
        fig = px.line(x = x, y = y)    
    return fig


def update_graph_04(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2016, geojson = shape_2016.geometry, locations = shape_2016.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2016.geometry.centroid.y,
                lon=shape_2016.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2016['NOMDT'] + '<br>' + shape_2016['NOMUT'] + '<br>ROBOS: ' + shape_2016['ROBOS'].apply(lambda x: f'{int(x):,}'),
                hoverinfo='text',
                #hoveron='fills',
                #hovertemplate = '<b>%{text}</b>',
                marker=dict(
                    size=5,
                    opacity=0
                ),
                hoverlabel=dict(
                    bgcolor='#FEDDDD'
                    
                )
            )
        )

        fig.update_layout(
            margin=dict(t=10, l=7, r=7, b=5),
            coloraxis_showscale=False
        )
    else:
        x = np.linspace(0, 10, 100)
        y = 6 * x
        fig = px.line(x=x, y=y)

    return fig
