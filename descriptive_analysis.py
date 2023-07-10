import numpy as np
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import plotly.figure_factory as ff

conteo_fecha_2016 =  pd.read_csv('assets/2016/FRECUENCIA_FECHAS_2016.csv')
conteo_colonia_2016 = pd.read_csv('assets/2016/COLONIAS_2016.csv')
shape_2016 = gpd.read_file('assets/2016/COLONIAS_2016.shp')
shape_2016 = shape_2016.to_crs("EPSG:4326")
conteo_fecha_2017 =  pd.read_csv('assets/2017/FRECUENCIA_FECHAS_2017.csv')
conteo_colonia_2017 = pd.read_csv('assets/2017/COLONIAS_2017.csv')
shape_2017 = gpd.read_file('assets/2017/COLONIAS_2017.shp')
shape_2017 = shape_2017.to_crs("EPSG:4326")
conteo_fecha_2018 =  pd.read_csv('assets/2018/FRECUENCIA_FECHAS_2018.csv')
conteo_colonia_2018 = pd.read_csv('assets/2018/COLONIAS_2018.csv')
shape_2018 = gpd.read_file('assets/2018/COLONIAS_2018.shp')
shape_2018 = shape_2018.to_crs("EPSG:4326")
conteo_fecha_2019 =  pd.read_csv('assets/2019/FRECUENCIA_FECHAS_2019.csv')
conteo_colonia_2019 = pd.read_csv('assets/2019/COLONIAS_2019.csv')
shape_2019 = gpd.read_file('assets/2019/COLONIAS_2019.shp')
shape_2019 = shape_2019.to_crs("EPSG:4326")
conteo_fecha_2020 =  pd.read_csv('assets/2020/FRECUENCIA_FECHAS_2020.csv')
conteo_colonia_2020 = pd.read_csv('assets/2020/COLONIAS_2020.csv')
shape_2020 = gpd.read_file('assets/2020/COLONIAS_2020.shp')
shape_2020 = shape_2020.to_crs("EPSG:4326")
conteo_fecha_2021 =  pd.read_csv('assets/2021/FRECUENCIA_FECHAS_2021.csv')
conteo_colonia_2021 = pd.read_csv('assets/2021/COLONIAS_2021.csv')
shape_2021 = gpd.read_file('assets/2021/COLONIAS_2021.shp')
shape_2021 = shape_2021.to_crs("EPSG:4326")
conteo_fecha_2022 =  pd.read_csv('assets/2022/FRECUENCIA_FECHAS_2022.csv')
conteo_colonia_2022 = pd.read_csv('assets/2022/COLONIAS_2022.csv')
shape_2022 = gpd.read_file('assets/2022/COLONIAS_2022.shp')
shape_2022 = shape_2022.to_crs("EPSG:4326")
conteo_fecha_2023 =  pd.read_csv('assets/2023/FRECUENCIA_FECHAS_2023.csv')
conteo_colonia_2023 = pd.read_csv('assets/2023/COLONIAS_2023.csv')
shape_2023 = gpd.read_file('assets/2023/COLONIAS_2023.shp')
shape_2023 = shape_2023.to_crs("EPSG:4326")




### ANALISIS DESCRIPTIVO        
# GRAFICA 1 
def update_graph_01_2016(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2016, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

def update_graph_02_2016(value):
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
        fig = px.treemap(conteo_fecha_2016, path = [px.Constant("Robos CDMX 2016"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 
def update_graph_04_2016(value):
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

###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
###############################################################################################################################

# GRAFICA 1 2017

def update_graph_01_2017(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2017, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2017

def update_graph_02_2017(value):
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
        fig = px.treemap(conteo_fecha_2017, path = [px.Constant("Robos CDMX 2017"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2017

def update_graph_04_2017(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2017, geojson = shape_2017.geometry, locations = shape_2017.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2017.geometry.centroid.y,
                lon=shape_2017.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2017['NOMDT'] + '<br>' + shape_2017['NOMUT'] + '<br>ROBOS: ' + shape_2017['ROBOS'].apply(lambda x: f'{int(x):,}'),
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

# GRAFICA 1 2018 

def update_graph_01_2018(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2018, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2018

def update_graph_02_2018(value):
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
        fig = px.treemap(conteo_fecha_2018, path = [px.Constant("Robos CDMX 2018"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2018

def update_graph_04_2018(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2018, geojson = shape_2018.geometry, locations = shape_2018.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2018.geometry.centroid.y,
                lon=shape_2018.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2018['NOMDT'] + '<br>' + shape_2018['NOMUT'] + '<br>ROBOS: ' + shape_2018['ROBOS'].apply(lambda x: f'{int(x):,}'),
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

# GRAFICA 1 2019

def update_graph_01_2019(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2019, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2019

def update_graph_02_2019(value):
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
        fig = px.treemap(conteo_fecha_2019, path = [px.Constant("Robos CDMX 2019"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2019

def update_graph_04_2029(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2019, geojson = shape_2019.geometry, locations = shape_2019.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2019.geometry.centroid.y,
                lon=shape_2019.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2019['NOMDT'] + '<br>' + shape_2019['NOMUT'] + '<br>ROBOS: ' + shape_2019['ROBOS'].apply(lambda x: f'{int(x):,}'),
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


# GRAFICA 1 2020

def update_graph_01_2020(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2020, path=[px.Constant("Ciudad De México"), 'NOMDT',], values='ROBOS',
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

# GRAFICA 2 2020
def update_graph_02_2020(value):
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
        fig = px.treemap(conteo_fecha_2016, path = [px.Constant("Robos CDMX 2020"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2020
def update_graph_04_2020(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2020, geojson = shape_2020.geometry, locations = shape_2020.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2020.geometry.centroid.y,
                lon=shape_2020.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2020['NOMDT'] + '<br>' + shape_2020['NOMUT'] + '<br>ROBOS: ' + shape_2020['ROBOS'].apply(lambda x: f'{int(x):,}'),
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


# GRAFICA 1 2021

def update_graph_01_2021(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2021, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2021
def update_graph_02_2021(value):
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
        fig = px.treemap(conteo_fecha_2021, path = [px.Constant("Robos CDMX 2021"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4  2021

def update_graph_04_2021(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2021, geojson = shape_2021.geometry, locations = shape_2021.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2021.geometry.centroid.y,
                lon=shape_2021.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2021['NOMDT'] + '<br>' + shape_2021['NOMUT'] + '<br>ROBOS: ' + shape_2021['ROBOS'].apply(lambda x: f'{int(x):,}'),
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

# GRAFICA 1 2022
def update_graph_01_2022(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2022, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2022

def update_graph_02_2022(value):
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
        fig = px.treemap(conteo_fecha_2016, path = [px.Constant("Robos CDMX 2022"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2022

def update_graph_04_2022(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2022, geojson = shape_2022.geometry, locations = shape_2022.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2022.geometry.centroid.y,
                lon=shape_2022.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2022['NOMDT'] + '<br>' + shape_2022['NOMUT'] + '<br>ROBOS: ' + shape_2022['ROBOS'].apply(lambda x: f'{int(x):,}'),
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


# GRAFICA 1 2023

def update_graph_01_2023(value):
    fig = None
    if value == 'Data_FGJ':
        fig = px.treemap(conteo_colonia_2023, path=[px.Constant("Ciudad De México"), 'NOMDT'], values='ROBOS',
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

# GRAFICA 2 2023

def update_graph_02_2023(value):
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
        fig = px.treemap(conteo_fecha_2023, path = [px.Constant("Robos CDMX 2023"), 'mes','dia'], values = 'Frecuencia',
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

# GRAFICA 4 2023

def update_graph_04_2023(value):
    if value == 'Data_FGJ':

        fig = px.choropleth_mapbox(shape_2023, geojson = shape_2023.geometry, locations = shape_2023.index, color = "ROBOS",
                                   color_continuous_scale = 'orrd',
                                   mapbox_style = "open-street-map",
                                   zoom = 9.7, center = {"lat": 19.4326, "lon": -99.1332},
                                   opacity = 0.5,
                                   #labels = {'ROBOS': 'Robos'},
                                   )
        fig.add_trace(
            go.Scattermapbox(
                lat=shape_2023.geometry.centroid.y,
                lon=shape_2023.geometry.centroid.x,
                mode='markers',
                hovertext=shape_2023['NOMDT'] + '<br>' + shape_2023['NOMUT'] + '<br>ROBOS: ' + shape_2023['ROBOS'].apply(lambda x: f'{int(x):,}'),
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