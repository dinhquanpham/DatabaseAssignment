from pydantic import Base

class UserCreateRequest(Base):
    id: int
    email: str
    password: str
    is_active: bool | None

