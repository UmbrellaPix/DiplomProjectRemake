from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, Boolean, Uuid, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание подключения к базе данных
_engine = create_engine('sqlite:///database.db')
_Base = declarative_base()
session = sessionmaker(bind=_engine)()

# Базовый абстрактный класс для таблиц
class _BaseTable(_Base):
    __abstract__  = True

    def __init__(self):
        self.session = session

    def save(self):
        self.session.add(self)
        self.session.commit()
        self.session.close()


class User(_BaseTable):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    permission = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    department = Column(String)
    is_delete = Column(Boolean)

    def __init__(self, 
                 login, 
                 password, 
                 permission, 
                 first_name,
                 last_name,
                 patronymic,
                 department,
                 is_delete = False
                 ):
        super().__init__()
        self.login = login
        self.password = password
        self.permission = permission
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.department = department
        self.is_delete = is_delete


class Session(_BaseTable):
    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    token = Column(Uuid)
    user_id = Column(Integer)
    deactivation_date = Column(DateTime)

    def __init__(self, token, user_id, deactivation_date):
        super().__init__()
        self.token = token
        self.user_id = user_id
        self.deactivation_date = deactivation_date

    
class File(_BaseTable):
    __tablename__ = 'file'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file = Column(LargeBinary)
    task_id = Column(Integer)
    is_delete = (Boolean)

    def __init__(self, name, file, task_id, is_delete = False):
        super().__init__()
        self.name = name
        self.file = file
        self.task_id = task_id
        self.is_delete = is_delete


class Task(_BaseTable):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    executor = Column(Integer)
    deadline = Column(String)
    description = Column(String)
    is_delete = Column(Boolean)

    def __init__(self, name, executor, deadline, description, is_delete = False):
        super().__init__()
        self.name = name
        self.executor = executor
        self.deadline = deadline
        self.description = description
        self.is_delete = is_delete

# Создание таблиц если они не существуют
_Base.metadata.create_all(bind = _engine)



