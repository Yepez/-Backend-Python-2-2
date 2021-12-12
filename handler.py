import logging
import os

import requests
from dotenv import load_dotenv

# loading enviroment variable
load_dotenv()

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def get_negocios(event, context):
    """Retrieve business by condition and entity"""
    url = (
        os.environ.get("API_INEGI")
        + "/"
        + str(event["pathParameters"]["condicion"])
        + "/"
        + str(entidades(event["pathParameters"]["entidad"]))
        + "/"
        + str(os.environ.get("REGISTRO_INICIAL"))
        + "/"
        + str(os.environ.get("REGISTRO_FINAL"))
        + "/"
        + str(os.environ.get("TOKEN_INEGI"))
    )

    log.debug("calling " + url)
    res = requests.get(url)

    response = {"statusCode": res.status_code, "body": res.text}

    return response


def entidades(entidad):
    entidades = [
        {"id_estado": "00", "nombre": "TODOS"},
        {"id_estado": "1", "nombre": "AGUASCALIENTES"},
        {"id_estado": "2", "nombre": "BAJA CALIFORNIA"},
        {"id_estado": "3", "nombre": "BAJA CALIFORNIA SUR"},
        {"id_estado": "4", "nombre": "CAMPECHE"},
        {"id_estado": "5", "nombre": "COAHUILA"},
        {"id_estado": "6", "nombre": "COLIMA"},
        {"id_estado": "7", "nombre": "CHIAPAS"},
        {"id_estado": "8", "nombre": "CHIHUAHUA"},
        {"id_estado": "9", "nombre": "CIUDAD DE MEXICO"},
        {"id_estado": "10", "nombre": "DURANGO"},
        {"id_estado": "11", "nombre": "GUANAJUATO"},
        {"id_estado": "12", "nombre": "GUERRERO"},
        {"id_estado": "13", "nombre": "HIDALGO"},
        {"id_estado": "14", "nombre": "JALISCO"},
        {"id_estado": "15", "nombre": "MEXICO"},
        {"id_estado": "16", "nombre": "MICHOACAN"},
        {"id_estado": "17", "nombre": "MORELOS"},
        {"id_estado": "18", "nombre": "NAYARIT"},
        {"id_estado": "19", "nombre": "NUEVO LEON"},
        {"id_estado": "20", "nombre": "OAXACA"},
        {"id_estado": "21", "nombre": "PUEBLA"},
        {"id_estado": "22", "nombre": "QUERETARO"},
        {"id_estado": "23", "nombre": "QUINTANA ROO"},
        {"id_estado": "24", "nombre": "SAN LUIS POTOSI"},
        {"id_estado": "25", "nombre": "SINALOA"},
        {"id_estado": "26", "nombre": "SONORA"},
        {"id_estado": "27", "nombre": "TABASCO"},
        {"id_estado": "28", "nombre": "TAMAULIPAS"},
        {"id_estado": "29", "nombre": "TLAXCALA"},
        {"id_estado": "30", "nombre": "VERACRUZ"},
        {"id_estado": "31", "nombre": "YUCATAN"},
        {"id_estado": "32", "nombre": "ZACATECAS"},
    ]

    filtered_record = list(
        filter(lambda item: item["nombre"] == entidad.upper(), entidades)
    )

    id_estado = "00"

    if len(filtered_record) > 0:
        id_estado = filtered_record[0]["id_estado"]

    return id_estado
