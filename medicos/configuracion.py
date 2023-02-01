from datetime import datetime, timedelta

# cambiar 
base_path = '/home/opc/api_empleador2/api_empleador'
carpeta_modelos = base_path+'/modelos'
carpeta_modelo_medicos = carpeta_modelos+'/medicos'
carpeta_modelo_medicos_generales = carpeta_modelos+'/medicos/generales'
carpeta_modelo_medicos_psiquiatria = carpeta_modelos+'/medicos/psiquiatria'
carpeta_modelo_pacientes = carpeta_modelos+'/pacientes'
#carpeta_modelo_empleadores = carpeta_modelos+'/empleador'


carpeta_modelo_compin = carpeta_modelos+'/compin'
path_encoder_nombre_compin = carpeta_modelo_compin + "/encoder_nombre_compin"
path_encoder_grupo_diag = carpeta_modelo_compin + "/encoder_grupo_diag"
path_modelo_compin = carpeta_modelo_compin + "/modelo_gam_compin"
carpeta_modelo_score = carpeta_modelos+'/score_licencias'
path_modelo_score = carpeta_modelo_score+'/gam_logis_score'
path_modelo_bienestar = carpeta_modelos+'/kmeans_model_bienestar.pkl'
path_modelo_cotizacion = carpeta_modelos+'/kmeans_model_cotizacion.pkl'
path_scaler=carpeta_modelos+'/scaler.pkl'
path_scaler_cot=carpeta_modelos+'/scaler_cot.pkl'

config = {
    "base_path" : base_path,
    "carpeta_modelo_medicos_generales" : carpeta_modelo_medicos_generales,
    "carpeta_modelo_medicos_psiquiatria" : carpeta_modelo_medicos_psiquiatria,
    "carpeta_modelo_pacientes" : carpeta_modelo_pacientes,
    "carpeta_modelo_compin" : carpeta_modelo_compin,
    "path_encoder_nombre_compin":path_encoder_nombre_compin,
    "path_encoder_grupo_diag":path_encoder_grupo_diag,
    "path_encoder_nombre_compin": path_encoder_nombre_compin,
    "path_encoder_grupo_diag": path_encoder_grupo_diag,
    "path_modelo_compin": path_modelo_compin,
    "path_modelo_score": path_modelo_score,
    "path_modelo_bienestar": path_modelo_bienestar,
    "path_modelo_cotizacion": path_modelo_cotizacion,    
    "path_scaler": path_scaler,
    "path_scaler_cot": path_scaler_cot


}

import pickle
#import pickle4 as pickle


def write_model(model, archivo):
    with open(archivo, 'wb+') as fp:
        pickle.dump(model, fp)

def read_model(archivo):
    with open(archivo, 'rb') as fp:
        n_model = pickle.load(fp)
        return n_model
