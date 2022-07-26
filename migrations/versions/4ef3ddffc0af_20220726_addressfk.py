"""20220726_addressFK

Revision ID: 4ef3ddffc0af
Revises: d2cd07097337
Create Date: 2022-07-26 14:05:57.913977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef3ddffc0af'
down_revision = 'd2cd07097337'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'address', ['address'], ['address_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'address')
    # ### end Alembic commands ###
