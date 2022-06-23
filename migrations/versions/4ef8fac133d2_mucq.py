"""MucQ

Revision ID: 4ef8fac133d2
Revises: f477a8c60e54
Create Date: 2022-06-20 08:55:53.827201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef8fac133d2'
down_revision = 'f477a8c60e54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'products', 'user', ['user_id'], ['id'])
    op.drop_column('products', 'likes')
    op.drop_column('products', 'product_image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('product_image', sa.VARCHAR(length=20), nullable=False))
    op.add_column('products', sa.Column('likes', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    # ### end Alembic commands ###