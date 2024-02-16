"""edit tables3

Revision ID: 84fb5ced2e19
Revises: eaf07bcb5c1b
Create Date: 2024-02-16 16:16:12.677627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84fb5ced2e19'
down_revision: Union[str, None] = 'eaf07bcb5c1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cell', sa.Column('leader_id', sa.String(length=50), nullable=False))
    op.create_foreign_key(None, 'cell', 'member', ['leader_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cell', type_='foreignkey')
    op.drop_column('cell', 'leader_id')
    # ### end Alembic commands ###