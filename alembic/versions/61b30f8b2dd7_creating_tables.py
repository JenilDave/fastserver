"""creating tables

Revision ID: 61b30f8b2dd7
Revises: 
Create Date: 2023-02-18 12:51:51.725038

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '61b30f8b2dd7'
down_revision = None
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
    op.drop_table('calculateAge')
    op.drop_table('xml_data')
    op.drop_table('SpatialTable')
    op.drop_table('myNamesTable')
    op.drop_table('StudentAddress')
    op.drop_table('StudentStatsHistory')
    op.drop_table('StudentStats')
    op.drop_table('Student')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Student',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('FirstName', sa.VARCHAR(length=40, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('MiddleName', sa.VARCHAR(length=35, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('LastName', sa.VARCHAR(length=35, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Branch', sa.VARCHAR(length=35, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Marks', sa.DECIMAL(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('Id', name='PK__Student__3214EC07EDDCD2CC')
    )
    op.create_table('StudentStats',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('StudentId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FullName', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Branch', sa.VARCHAR(length=35, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Percentage', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Location', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['StudentId'], ['Student.Id'], name='FK__StudentSt__Stude__114A936A'),
    sa.PrimaryKeyConstraint('Id', name='PK__StudentS__3214EC07C0991C3C')
    )
    op.create_table('StudentStatsHistory',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=300, increment=1), autoincrement=True, nullable=False),
    sa.Column('ReferenceId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('FullName', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('Branch', sa.VARCHAR(length=35, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Percentage', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('Location', sa.VARCHAR(length=200, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('IsLatest', mssql.BIT(), autoincrement=False, nullable=True),
    sa.Column('UpdatedOn', mssql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['ReferenceId'], ['StudentStats.Id'], name='FK__StudentSt__Refer__208CD6FA'),
    sa.PrimaryKeyConstraint('Id', name='PK__StudentS__3214EC07A4A17512')
    )
    op.create_table('StudentAddress',
    sa.Column('Id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1), autoincrement=True, nullable=False),
    sa.Column('StudentId', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('City', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('State', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Country', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('Pincode', sa.DECIMAL(precision=18, scale=0), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['StudentId'], ['Student.Id'], name='FK__StudentAd__Stude__09A971A2'),
    sa.PrimaryKeyConstraint('Id', name='PK__StudentA__3214EC07E46CD027')
    )
    op.create_table('myNamesTable',
    sa.Column('first_name', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('full_name', sa.VARCHAR(length=101, collation='SQL_Latin1_General_CP1_CI_AS'), sa.Computed("(([first_name]+' ')+[last_name])", persisted=False), autoincrement=False, nullable=True)
    )
    op.create_table('SpatialTable',
    sa.Column('ID', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('all_points', sa.NullType(), autoincrement=False, nullable=True)
    )
    op.create_table('xml_data',
    sa.Column('data', mssql.XML(), autoincrement=False, nullable=True)
    )
    op.create_table('calculateAge',
    sa.Column('fullname', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('DOB', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('AGE', sa.INTEGER(), sa.Computed('(datediff(year,[DOB],getdate()))', persisted=False), autoincrement=False, nullable=True)
    )
    op.drop_table('users', schema='dbo')
    op.drop_table('products', schema='dbo')
    # ### end Alembic commands ###