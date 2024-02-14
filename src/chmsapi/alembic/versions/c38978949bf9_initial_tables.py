"""initial tables

Revision ID: c38978949bf9
Revises: 
Create Date: 2024-02-12 19:06:57.395696

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c38978949bf9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('cell',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('location', sa.String(length=100), nullable=False),
                    sa.Column('date_started', sa.DATETIME(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('constituency',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('location', sa.String(length=100), nullable=False),
                    sa.Column('date_started', sa.DATETIME(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('department',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('member',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('first_name', sa.String(length=50), nullable=False, comment='First Name'),
                    sa.Column('last_name', sa.String(length=50), nullable=False, comment='Last Name'),
                    sa.Column('email', sa.String(length=50), nullable=False, comment='email address'),
                    sa.Column('dob', sa.DATETIME(), nullable=False),
                    sa.Column('phone_number', sa.String(length=11), nullable=True, comment='Phone number'),
                    sa.Column('gender', mysql.ENUM('MALE', 'FEMALE'), nullable=False),
                    sa.Column('nationality', sa.String(length=50), nullable=False, comment=' Nationality'),
                    sa.Column('marital_status', mysql.ENUM('SINGLE', 'MARRIED', 'DIVORCED'), nullable=False),
                    sa.Column('address', mysql.LONGTEXT(), nullable=True, comment='Address'),
                    sa.Column('gps_address', sa.String(length=50), nullable=True, comment='Ghana Post Address'),
                    sa.Column('educational_level', mysql.ENUM('TERTIARY', 'SECONDARY', 'PRIMARY'), nullable=False),
                    sa.Column('membership_status', mysql.ENUM('MEMBER', 'LEADER'), nullable=False),
                    sa.Column('leadership_role',
                              mysql.ENUM('DEACON', 'DEACONESS', 'SHEPHERD', 'ELDER', 'PASTOR', 'LADY_PASTOR',
                                         'REVEREND'), nullable=False, comment='Leadership role in the church'),
                    sa.Column('date_joined', sa.DATETIME(), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_index(op.f('ix_member_email'), 'member', ['email'], unique=True)
    op.create_index(op.f('ix_member_nationality'), 'member', ['nationality'], unique=False)
    op.create_table('user',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('email', sa.String(length=50), nullable=False, comment='Mail'),
                    sa.Column('password', sa.String(length=255), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False, comment='Super authority'),
                    sa.Column('is_staff', sa.Boolean(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('join_time', sa.DateTime(), nullable=False, comment='Registration time'),
                    sa.Column('last_login_time', sa.DateTime(), nullable=True, comment='Last login last time'),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_member_nationality'), table_name='member')
    op.drop_index(op.f('ix_member_email'), table_name='member')
    op.drop_table('member')
    op.drop_table('department')
    op.drop_table('constituency')
    op.drop_table('cell')
    op.drop_table('attendance')
    # ### end Alembic commands ###
