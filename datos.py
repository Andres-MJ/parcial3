from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session
)


# =====================================
# TODO ORM 1 - CONFIGURAR LA CONEXION
# =====================================
engine = create_engine("sqlite:///zapateria.db")


# =====================================
# TODO ORM 2 - CREAR LA CLASE BASE
# =====================================
class Base(DeclarativeBase):
    pass


# =====================================
# TODO ORM 3 - CREAR EL MODELO ZAPATO
# =====================================
class Zapato(Base):
    __tablename__ = "zapatos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    modelo: Mapped[str] = mapped_column(String(100))
    talla: Mapped[int]
    precio: Mapped[float]


# =====================================
# TODO ORM 4 - CREAR LA TABLA
# =====================================
def inicializar_bd():
    Base.metadata.create_all(engine)


# =====================================
# TODO ORM 5 - REGISTRAR ZAPATO
# =====================================
def crear_zapato(modelo, talla, precio):
    try:
        zapato = Zapato(modelo=modelo, talla=talla, precio=precio)
        with Session(engine) as session:
            session.add(zapato)
            session.commit()
        return True
    except Exception:
        return False


# =====================================
# TODO ORM 6 - LISTAR ZAPATOS
# =====================================
def listar_zapatos():
    with Session(engine, expire_on_commit=False) as session:
        return list(session.scalars(select(Zapato)).all())


# =====================================
# TODO ORM 7 - BUSCAR POR ID
# =====================================
def buscar_zapato(id_zapato):
    with Session(engine, expire_on_commit=False) as session:
        return session.get(Zapato, id_zapato)


# =====================================
# TODO ORM 8 - ACTUALIZAR PRECIO
# =====================================
def actualizar_precio(id_zapato, nuevo_precio):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        zapato.precio = nuevo_precio
        session.commit()
        return True


# =====================================
# TODO ORM 9 - ELIMINAR ZAPATO
# =====================================
def eliminar_zapato(id_zapato):
    with Session(engine) as session:
        zapato = session.get(Zapato, id_zapato)
        if zapato is None:
            return False
        session.delete(zapato)
        session.commit()
        return True