"""new tables

Revision ID: dac156270541
Revises: 20b70c635f6c
Create Date: 2024-02-16 11:44:04.008304

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'dac156270541'
down_revision: Union[str, None] = '20b70c635f6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cell_constituency',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('cell_id', sa.String(length=50), nullable=False),
                    sa.Column('constituency_id', sa.String(length=50), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('cell_id'),
                    sa.UniqueConstraint('constituency_id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('cell_leaders',
                    sa.Column('id', sa.String(length=50), nullable=False),
                    sa.Column('cell_id', sa.String(length=50), nullable=False),
                    sa.Column('leader_id', sa.String(length=50), nullable=False),
                    sa.Column('created_date', sa.DateTime(), nullable=False),
                    sa.Column('updated_date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('cell_id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('leader_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cell_leaders')
    op.drop_table('cell_constituency')
    # ### end Alembic commands ###
