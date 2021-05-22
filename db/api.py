#Carga de librerias
import pandas as pd
import numpy as np
#import json

#Carga datos de IES
#consolidado = pd.read_csv('https://datavizjfme.s3.amazonaws.com/consolidado')
#tarjetas_vigentes_año_total = pd.read_csv('https://datavizjfme.s3.amazonaws.com/tarjetas_vigentes_año_total')


#Si no existe crea la columna
#if 'Año_Semestre' not in DFutil:
#    DFutil['Año_Semestre'] = DFutil['Año'] + '-' + DFutil['Semestre']


###############################################################################
#Analis tarjetas vigentes
def get_g1():
    ContratosxEstado = pd.read_csv("C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosxEstado.csv")
    return ContratosxEstado

def get_g2():
    ContratosXDepartamento = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosxDepartamento.csv')
    return ContratosXDepartamento

def get_g3():
    ContratosXDepartamentox10000hb = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosxDepartamentox10000hb.csv')
    return ContratosXDepartamentox10000hb

def get_g4():
    ContratosxSector = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosxSector.csv')
    return ContratosxSector

def get_g5():
    ContratosSaludxCiudad = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosSaludxCiudad.csv')
    return ContratosSaludxCiudad

def get_g6():
    ContratosSaludxTipo = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosSaludxTipo.csv')
    return ContratosSaludxTipo

def get_g7():
    ContratosSaludxOrden = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosSaludxOrden.csv')
    return ContratosSaludxOrden

def get_g8():
    ContratosSaludxModalidad = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosSaludxModalidad.csv')
    return ContratosSaludxModalidad

def get_g9():
    ContratosSaludxDepartamento = pd.read_csv('C:/Users/slvargas/VD/dash-contratos/datacontratos/ContratosSaludxDepartamento.csv')
    return ContratosSaludxDepartamento
