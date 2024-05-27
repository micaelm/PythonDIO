from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Double
from sqlalchemy import select

# Declarado a instancia de declarative_base na variável base
Base = declarative_base()

class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Double)

    cliente = relationship('Cliente', back_populates='contas')

    def __repr__(self):
        return f'Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})'


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), nullable=False)
    endereco = Column(String(11))

    contas = relationship('Conta', back_populates='cliente')

    def __repr__(self):
        return f'Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})'


# Criamos a conexão com banco de dados
engine = create_engine('sqlite://')

# criando classe como tabela no banco de dados
Base.metadata.create_all(engine)

# usamos para recuperar informações persistidas no banco
inspetor = inspect(engine)

# verificando se existe a tabela no banco
print(inspetor.has_table('conta'))

with Session(engine) as session:
    # Criando clientes fictícios
    cliente1 = Cliente(
        nome='João',
        cpf='123456789',
        endereco='Rua A, 123'
    )
    
    cliente2 = Cliente(
        nome='Maria',
        cpf='987654321',
        endereco='Rua B, 456'
    )
    
    cliente3 = Cliente(
        nome='Carlos',
        cpf='456123789',
        endereco='Rua C, 789'
    )
    
    cliente4 = Cliente(
        nome='Ana',
        cpf='321654987',
        endereco='Rua D, 101'
    )

    # Enviando clientes para o BD
    session.add_all([cliente1, cliente2, cliente3, cliente4])
    session.commit()

    # Criando contas para os clientes criados
    conta1 = Conta(
        tipo='corrente',
        agencia='005',
        num=1516,
        saldo=1500.00,
        id_cliente=cliente1.id
    )

    conta2 = Conta(
        tipo='poupança',
        agencia='006',
        num=1617,
        saldo=3000.00,
        id_cliente=cliente2.id
    )

    conta3 = Conta(
        tipo='corrente',
        agencia='007',
        num=1718,
        saldo=2500.00,
        id_cliente=cliente3.id
    )

    conta4 = Conta(
        tipo='poupança',
        agencia='008',
        num=1819,
        saldo=1000.00,
        id_cliente=cliente4.id
    )

    conta5 = Conta(
        tipo='corrente',
        agencia='009',
        num=1910,
        saldo=500.00,
        id_cliente=cliente4.id
    )

    # Enviando contas para o BD
    session.add_all([conta1, conta2, conta3, conta4, conta5])

    # Aplicando a persistência
    session.commit()

    # Executando a consulta
    stmt = select(Conta).where(Conta.tipo.in_(['corrente']))

    # Como ele é um pouquinho mais complexo, é preciso usar o for
    for conta in session.scalars(stmt):
        print(conta)
