from memory import session, Session
from datetime import datetime
import uuid

# Проверка токена сессии
def auth_token(token:str) -> int:
    current_datetime = datetime.now()
    current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    token = uuid.UUID(token)

    result =  session.query(Session).filter(
        Session.token == token and
        Session.deactivation_date > current_datetime_str
    ).first()
    if result != None:
        return result.user_id
    else:
        return 0

# Создание сессии
def create_session(user_id: int) -> str:
    current_datetime = datetime.now()
    uuid_token = uuid.uuid4()

    session = Session(token = uuid_token, user_id=user_id, deactivation_date=current_datetime)
    session.save()
    return str(uuid_token)


