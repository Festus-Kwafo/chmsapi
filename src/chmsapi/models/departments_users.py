from sqlalchemy import String, ForeignKey, Column, Table, Integer
from src.chmsapi.models.base import MappedBase

departments_users = Table('departments_users', MappedBase.metadata,
                          Column('department_id', String(50), ForeignKey('department.id', ondelete='CASCADE')),
                          Column('user_id', String(50), ForeignKey('user.id', ondelete='CASCADE')))
