from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais
import requests
import json

engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos_json = archivo.json()


for d in datos_json:
    print(d)
    print(len(d.keys()))
    p = Pais(nombre=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoname=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], \
            isCapital=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()