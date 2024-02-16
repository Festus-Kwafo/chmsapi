from sqlalchemy import Table, Column, ForeignKey, String
from src.chmsapi.models.base import MappedBase

members_departments = Table('members_departments', MappedBase.metadata,
                            Column('member_id', String(50), ForeignKey('member.id', ondelete='CASCADE'), primary_key=True),
                            Column('department_id', String(50), ForeignKey('department.id', ondelete='CASCADE'), primary_key=True))