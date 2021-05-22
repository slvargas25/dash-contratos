import os
import pathlib
import numpy as np
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go #Libreria de objetos graficos de Plotly

from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from scipy.stats import rayleigh

from db.api import get_g1, get_g2, get_g3, get_g4, get_g5, get_g6, get_g7, get_g8, get_g9

import plotly.express as px
import plotly.figure_factory as ff


def generate_section_banner(title):
    return html.Div([html.H6(title, className="graph__title")])

def generate_g1():
    df = get_g1()
    df = df.set_index('periodo')
    
    title="Valor de los contratos por estados"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)

def generate_g2():
    df = get_g2()
    df = df.set_index('periodo')
    
    title="Valor general de los contratos por año y departamento"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)

def generate_g3():
    df = get_g3()
    df = df.set_index('periodo')
    
    title="Valor general de los contratos por año y departamento x cada 10000 habitantes"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)

def generate_g4():
    df = get_g4()
    df = df.set_index('periodo')
    
    title="Valor contratos por sector económico"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)

def generate_g5():
    df = get_g5()
    df = df.set_index('periodo')
    
    title="Contratos por año y ciudad - Sector Salud"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)

def generate_g6():
    df = get_g6()
    df = df.set_index('periodo')
    
    title="Contratos por año y modalidad de contrato - Sector Salud"
    
    fig = go.Figure()
    
    for column in df.columns.to_list():
        fig.add_trace(go.Scatter(x = df.index, y = df[column], name = column))
        
    fig.update_layout(title_text=title, height=600)#, width=1200)
    
    #Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness = 0.06) #Altura del rangeslider
    
    return dcc.Graph(figure=fig)


def generate_g7():
    df = get_g7()
    df = df.set_index('periodo')

    title = "Contratos por año y orden (Nacional-Territorial) - Sector Salud"

    fig = go.Figure()

    for column in df.columns.to_list():
        fig.add_trace(go.Bar(x=df.index, y=df[column], name=column))

    fig.update_layout(title_text=title, height=600)  # , width=1200)

    # Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness=0.06)  # Altura del rangeslider

    return dcc.Graph(figure=fig)

def generate_g8():
    df = get_g8()
    # df = df.reset_index()
    df = df.set_index('periodo')

    title = "Distribución de contratos por año y tipo de contrato - Sector Salud"

    fig = go.Figure()

    for column in df.columns.to_list():
        fig.add_trace(go.Bar(x=df.index, y=df[column], name=column))

    fig.update_layout(title_text=title, height=600)  # , width=1200)

    # Slider
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(rangeslider_thickness=0.06)  # Altura del rangeslider

    return dcc.Graph(figure=fig)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],)
server = app.server

#app_color = {"graph_bg": "#B0C4DE", "graph_line": "#00FF00"}

app.layout = html.Div([
    #Encabezado
    html.Div(
        [
            html.Div(
                [
                    html.H2("INFORMACION DE LOS CONTRATOS REGISTRADOS EN SECOP II", className="app__header__title"),
                    html.H3("Información visual entre 2016 y 2021.",className="app__header__title--grey",),
                    html.P("En datos abiertos https://www.datos.gov.co/en/Gastos-Gubernamentales/SECOP-II-Contratos-Electr-nicos/jbjy-vk9h  se encuentra disponible la base de datos SECOP II - Contratos Electrónicos que contiene información de los contratos registrados en SECOP II desde su lanzamiento hasta la fecha realizados en  los diferentes departamentos y asignados a diferentes sectores a nivel nacional (Salud, Educación, Defensa, Cultura, etc)",className="app__header__title--grey",),
                ],
                className="app__header__desc",
            ),
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("MapaColombia_.png"),
                        className="app__menu__img",
                    )
                ],
                className="app__header__logo",
            ),
        ],
        className="app__header",
    ),
    
    #Tabs
    dcc.Tabs([
        
        #Tab 1
        dcc.Tab(label='Contratos por estados y departamentos', children=[
            
            html.Hr(),
            html.Table([html.Tr([html.Td([html.H4("Contratos por estados",className="app__header__title--grey",),]),html.Td([html.Img(src=app.get_asset_url("Inversion.png")),],),],),],),
            html.Div(children='''El total de contratos de la base general se clasifican en diferentes estados: Activo, Borrador, Cancelado, Cedido, Cerrado, En aprobación, En ejecución, Enviado proveedor, Modificado, Prorrogado, Suspendido y Terminado.  De los anteriores estados se tomarán para el análisis los contratos en estado Activo, En ejecución, Prorrogado, y Terminado que de acuerdo a su clasificación indican que se realizó una inversión real de recursos en los departamentos y los diferentes sectores económicos.'''),
            generate_g1(),
            
            html.Hr(),
            html.Table([html.Tr([html.Td([html.H4("Valor de los contratos por departamentos ",className="app__header__title--grey",),]),html.Td([html.Img(src=app.get_asset_url("MapaColombia1.png")),],),],),],),
            #html.H4("Total Tarjetas de Crédito Activas Franquicia Visa",className="app__header__title--grey",),
            html.Div(children='''A continuación, se plasmará el valor de inversión o asignación de los contratos nacionales por departamento, sin contemplar la cantidad de habitantes que serán beneficiados con el valor de los contratos. Es decir, se realizará una distribución del valor de los contratos en los estados Activo, En ejecución, Prorrogado, y Terminado para los diferentes departamentos a nivel nacional.'''),
            generate_g2(),
            
            html.Hr(),
            html.Table([html.Tr([html.Td([html.H4("Valor de los contratos por departamentos por cada 10000 habitantes ",className="app__header__title--grey",),]),html.Td([html.Img(src=app.get_asset_url("MapaColombia1.png")),],),],),],),
            #html.H4("Total Tarjetas de Crédito Activas Franquicia Mastercard",className="app__header__title--grey",),
            html.Div(children='''A continuación, se plasmará el valor de inversión o asignación de los contratos nacionales por departamento.  Las cifras aquí presentadas hacen una relación de inversión por cada 10000 habitantes; de igual manera la base de los estados de contratos contemplados es Activo, En ejecución, Prorrogado, y Terminado para los diferentes departamentos a nivel nacional.  Se evidencia que el departamentos con mayor inversión en proporción al número de habitantes corresponden a Distrito Capital y se resalta que San Andres y Chocó alcanzaron una mayor inversión durante el año 2020 y 2021, posiblemente derivado de las necesidades de la emergencia sanitaria y el huracan que presento grandes afectaciones en San Andres y Providencia.'''),
            generate_g3(),
        ]),

        
        #Tab 2
        dcc.Tab(label='Contratos por sector', children=[

            html.Hr(),
            html.Table([html.Tr([html.Td(
                [html.H4("Valor contratos por sectores económicos ", className="app__header__title--grey", ), ]),
                                 html.Td([html.Img(src=app.get_asset_url("Sectores4.jpg")), ], ), ], ), ], ),
            html.Div(
                children='''Al realizar el análisis de los contratos por sectores económicos, se ve claramente como han cambiado las prioridades de inversión.   Se evidencia que hasta el año 2019 la mayor inversión se enfocaba en el sector Defensa mientras que en los años 2020 y 2021 la mayor inversión se concentra en los sectores Salud, Servicio públicos y Transporte.'''),

            html.Div(
                children='''Por otra parte, se puede mencionar que el sector Salud, Servicio Público, y Tecnologías de información y telecomunicaciones y trabajo han tenido una tendencia de crecimiento desde el año 2016 hasta la fecha.'''),

            html.Div(
                children='''Desde el punto de vista de los sectores que tienen baja inversión y pueden tener un gran alcance y proyección a nivel nacional son: Ciencia tecnología, deportes, cultura, agricultura. Este último, aunque ha tenido un leve crecimiento en la inversión en los últimos años la inversión es baja teniendo en cuenta que nuestro país es altamente agrícola.'''),

            html.Div(
                children='''El sector en el año 2020 invirtió 3.79 trillones de pesos aproximadamente y en el 2021 3.09 trillones en lo corrido del año, lo que es razonable dado la alta inversión que se ha tenido que realizar dada la emergencia sanitaria.'''),

            generate_g4(),

            html.Hr(),
            html.Table([html.Tr([html.Td(
                [html.H4("Contratos por periodo y orden (Nacional o Territorial) - Sector Salud", className="app__header__title--grey", ), ]),
                                 html.Td([html.Img(src=app.get_asset_url("Orden.jpg")), ], ), ], ), ], ),
            # html.H4("Total Tarjetas de Crédito Activas Franquicia America Express",className="app__header__title--grey",),
            html.Div(
                children='''Al enfocarnos en analizar el sector Salud y Protección encontramos que la tendencia de distribución de contratos en el orden nacional y territorial permite ver que durante los años 2020 y 2021 ha cambiado y la mayoria de contratos hacen parte del tipo de orden nacional, es posible que este resultado este condicionado a las inversiones que ha realizado el estado con respecto a temas de salud encaminadas a mitigar los efectos de la emergencia sanitaria.'''),
            generate_g7(),

            html.Hr(),
            html.H4("Contratos por tipo de contrato - Sector Salud", className="app__header__title--grey", ),
            html.Div(
                children='''Dentro de la clasificación del tipo de contratación realizada en el sector Salud y Protección encontramos que en los años 2021 y 2021 la contratación se centra en: Contratación de regimén especial y contratación directa'''),
            generate_g8(),

            html.Hr(),
            html.Table([html.Tr([html.Td([html.H4("Contratos por modalidad de contrato - Sector Salud",className="app__header__title--grey",),]),html.Td([html.Img(src=app.get_asset_url("Modalidad.png")),],),],),],),
            html.Div(children='''La modalidad de contrato de sector Salud se enfoca principalmente en prestación de servicios, sin embargo se evidencia que para el año 2020 y 2021 se creció considerablemente la categoria otro con un monto de 2.8 Trillones y 2,54 Trillones respectivamente con relación a contratos en salud cuyo estado del contrato es Activo, En Ejecucuón, Prorrogado, y Terminado.'''),
            generate_g6(),
            
            html.Hr(),
            html.Table([html.Tr([html.Td([html.H4("Valor contrato salud por ciudad y año",className="app__header__title--grey",),]),html.Td([html.Img(src=app.get_asset_url("Ciudad.png")),],),],),],),
            html.Div(children='''Las ciudades con mayor inversión en el sector salud corresponden a las cuidades capitales tales como: Bogota, Medellin, Cali y Barranquilla. De igual manera se evidencia el crecimiento en la inversión durante los años 2021 y lo corrido del año 2021 en dichas cuidades '''),
            generate_g5(),

        ]),
    ])
])








# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)