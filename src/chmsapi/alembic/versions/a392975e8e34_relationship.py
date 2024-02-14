"""relationship

Revision ID: a392975e8e34
Revises: 76c6470a73a1
Create Date: 2024-02-13 19:17:09.618675

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a392975e8e34'
down_revision: Union[str, None] = '76c6470a73a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('member', 'department_id',
                    existing_type=mysql.VARCHAR(length=50),
                    nullable=False)
    op.drop_constraint('member_ibfk_3', 'member', type_='foreignkey')
    op.drop_constraint('member_ibfk_4', 'member', type_='foreignkey')
    op.create_foreign_key(None, 'member', 'department', ['department_id'], ['id'])
    op.create_foreign_key(None, 'member', 'cell', ['cell_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'member', type_='foreignkey')
    op.drop_constraint(None, 'member', type_='foreignkey')
    op.create_foreign_key('member_ibfk_4', 'member', 'cell', ['cell_id'], ['id'], onupdate='CASCADE',
                          ondelete='CASCADE')
    op.create_foreign_key('member_ibfk_3', 'member', 'department', ['department_id'], ['id'], onupdate='CASCADE',
                          ondelete='CASCADE')
    op.alter_column('member', 'department_id',
                    existing_type=mysql.VARCHAR(length=50),
                    nullable=True)
    # ### end Alembic commands ###
