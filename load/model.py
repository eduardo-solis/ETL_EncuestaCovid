from sqlalchemy import Column, String, Integer, Float
from base import Base

# Declaramos la clase formulario que define la tabla de la BD
class Formulario(Base):
    __tablename__ = 'formularios'

    # Declaración de columnas
    id = Column(Integer, primary_key=True)
    pregunta1 = Column(String)
    pregunta2 = Column(String)
    pregunta3 = Column(String)
    pregunta4 = Column(String)
    pregunta5 = Column(String)
    pregunta6 = Column(String)
    pregunta7 = Column(String)
    pregunta8 = Column(String)
    pregunta9 = Column(String)
    pregunta10 = Column(String)
    pregunta11 = Column(String)
    pregunta12 = Column(String)
    pregunta13 = Column(String)
    pregunta14 = Column(String)
    pregunta15 = Column(String)
    pregunta16 = Column(String)
    pregunta17 = Column(String)
    pregunta18 = Column(String)
    pregunta19 = Column(String)
    pregunta20 = Column(String)
    pregunta21 = Column(String)
    pregunta22 = Column(String)
    pregunta23 = Column(String)
    pregunta24 = Column(String)
    pregunta25 = Column(String)
    pregunta26 = Column(String)
    pregunta27 = Column(String)
    pregunta28 = Column(String)
    pregunta29 = Column(String)
    pregunta30 = Column(String)
    fecha = Column(String)
    edad = Column(String)
    tokens = Column(String)

    def __init__(self, id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, fecha, edad, tokens):
        self.id = id
        self.pregunta1 = p1
        self.pregunta2 = p2
        self.pregunta3 = p3
        self.pregunta4 = p4
        self.pregunta5 = p5
        self.pregunta6 = p6
        self.pregunta7 = p7
        self.pregunta8 = p8
        self.pregunta9 = p9
        self.pregunta10 = p10
        self.pregunta11 = p11
        self.pregunta12 = p12
        self.pregunta13 = p13
        self.pregunta14 = p14
        self.pregunta15 = p15
        self.pregunta16 = p16
        self.pregunta17 = p17
        self.pregunta18 = p18
        self.pregunta19 = p19
        self.pregunta20 = p20
        self.pregunta21 = p21
        self.pregunta22= p22
        self.pregunta23 = p23
        self.pregunta24 = p24
        self.pregunta25 = p25
        self.pregunta26 = p26
        self.pregunta27 = p27
        self.pregunta28 = p28
        self.pregunta29 = p29
        self.pregunta30 = p30
        self.fecha = fecha
        self.edad = edad
        self.tokens = tokens