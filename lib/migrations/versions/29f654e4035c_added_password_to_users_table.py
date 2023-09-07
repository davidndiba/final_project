"""added password to users table

Revision ID: 29f654e4035c
Revises: eb606623cd1e
Create Date: 2023-09-06 19:10:26.964501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29f654e4035c'
down_revision = 'eb606623cd1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('phone_number', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'last_Name')
    op.drop_column('users', 'first_Name')
    op.drop_column('users', 'user_Name')
    op.drop_column('users', 'phone_Number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_Number', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('user_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('first_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('last_Name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'user_name')
    # ### end Alembic commands ###
