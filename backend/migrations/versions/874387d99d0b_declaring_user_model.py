"""Declaring user model

Revision ID: 874387d99d0b
Revises: 
Create Date: 2022-04-09 17:15:57.791026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '874387d99d0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
