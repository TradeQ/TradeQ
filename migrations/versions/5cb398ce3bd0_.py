"""empty message

Revision ID: 5cb398ce3bd0
Revises: 8040818b45da
Create Date: 2022-06-20 07:16:33.298488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb398ce3bd0'
down_revision = '8040818b45da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'products', 'user', ['user_id'], ['id'])
    op.drop_column('products', 'product_image')
    op.drop_column('products', 'likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('likes', sa.INTEGER(), nullable=False))
    op.add_column('products', sa.Column('product_image', sa.VARCHAR(length=20), nullable=False))
    op.drop_constraint(None, 'products', type_='foreignkey')
    # ### end Alembic commands ###