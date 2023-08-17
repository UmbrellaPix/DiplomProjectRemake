from modules.memory.memory import session, Session, User
from datetime import datetime
import uuid

# Проверка токена сессии
def auth_token(token:str) -> bool:
    
    current_datetime = datetime.now()
    current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    try:
        token = uuid.UUID(token)
        result =  session.query(Session).filter(
            Session.token == token and
            Session.deactivation_date > current_datetime_str
        ).first()
        if result != None:
            return True
        else:
            return False
    except ValueError:
        return False

# Создание сессии
def create_session(user_id: int) -> str:
    current_datetime = datetime.now()
    uuid_token = uuid.uuid4()

    session = Session(token = uuid_token, user_id=user_id, deactivation_date=current_datetime)
    session.save()
    return str(uuid_token)

# Авторизация аккаунта
def auth_login(login:str, password:str) -> int:
    result = session.query(User).filter(
        (User.login == login) & 
        (User.password == password)
    ).first()
    if result != None:
        return result.id
    else:
        return 0


