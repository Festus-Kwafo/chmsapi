"""relationship bug fix

Revision ID: 49f28678b3ea
Revises: f3c49e62b4e2
Create Date: 2024-02-13 19:20:20.598158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49f28678b3ea'
down_revision: Union[str, None] = 'f3c49e62b4e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('constituency', sa.Column('leader', sa.String(length=50), nullable=False))
    op.create_foreign_key(None, 'constituency', 'member', ['leader'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'constituency', type_='foreignkey')
    op.drop_column('constituency', 'leader')
    # ### end Alembic commands ###
