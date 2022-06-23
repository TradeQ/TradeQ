"""empty message

Revision ID: fc7ae464d305
Revises: 07b296d78248
Create Date: 2022-06-21 13:57:38.769904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc7ae464d305'
down_revision = '07b296d78248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key(None, 'products', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
