import sys
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



#engine = create_engine("sqlite:///banco.db")
#Base = declarative_base()
#Session = sessionmaker()
#Session.configure(bind=engine)
#
#session = Session()
#
#class Todo(Base):
#    __tablename__ = "todo"
#    id = Column(Integer,primary_key=True)
#    task = Column(String)
#    user = Column(String)
#    status = Column(Boolean)
#
#if __name__ == "__main__":
#    try:
#        Base.metadata.create_all(engine)
#        #funcionario = Funcionario(id=1,nome="Elias Neves")
#        #session.add(funcionario)
#        #dependente1 = Dependentes(id=1,nome="Joao")
#        #dependente2 = Dependentes(id=2,nome="Maria")
#        #funcionario.dependentes.append(dependente1)
#        #funcionario.dependentes.append(dependente2)
#        #session.add(dependente1)
#        #session.add(dependente2)
#        #session.commit()
#    except Exception as e:
#        print ("Falhou ao criar o banco: {}".format(e))
#
