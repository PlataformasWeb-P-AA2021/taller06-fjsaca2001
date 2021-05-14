from sqlalchemy import create_engine
engine = create_engine('sqlite:///paises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    isCapital = Column(String)

    def __repr__(self):
        return "Pais: nombre=%s capital=%s continente:%s dial=%s geoname:%s itu:%s lenguajes:%s isCapital:%s" % (
                          self.nombre, 
                          self.capital, 
                          self.continente,
                          self.dial,
                          self.geoname,
                          self.itu,
                          self.lenguajes,
                          self.isCapital)


Base.metadata.create_all(engine)