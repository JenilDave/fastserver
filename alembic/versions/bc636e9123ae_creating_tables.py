"""creating  tables

Revision ID: bc636e9123ae
Revises: ea4c2d962967
Create Date: 2023-02-18 14:03:47.442513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc636e9123ae'
down_revision = 'ea4c2d962967'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.BigInteger(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='dbo'
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('admin', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='dbo'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users', schema='dbo')
    op.drop_table('products', schema='dbo')
    # ### end Alembic commands ###
