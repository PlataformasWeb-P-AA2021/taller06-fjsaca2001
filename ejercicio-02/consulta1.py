from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Pais 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad pais 
paises = session.query(Pais).all()

print("Presentación de todos los paises del continente americano")
paises = session.query(Pais).filter(or_(Pais.continente=="NA", Pais.continente=="SA")).all()
print("\n",paises)

