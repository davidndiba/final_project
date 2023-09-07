"""Added cars table and fixed sellers table

Revision ID: a58940c76170
Revises: eb606623cd1e
Create Date: 2023-09-07 10:30:24.173527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a58940c76170'
down_revision = 'eb606623cd1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['sellers.id'], name=op.f('fk_cars_seller_id_sellers')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('fk_buyers_seller_id_users', 'buyers', type_='foreignkey')
    op.drop_constraint('fk_buyers_buyer_id_users', 'buyers', type_='foreignkey')
    op.create_foreign_key(op.f('fk_buyers_user_id_users'), 'buyers', 'users', ['user_id'], ['id'])
    op.drop_column('buyers', 'buyer_id')
    op.drop_column('buyers', 'seller_id')
    op.add_column('users', sa.Column('user_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('phone_number', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'last_Name')
    op.drop_column('users', 'phone_Number')
    op.drop_column('users', 'first_Name')
    op.drop_column('users', 'user_Name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('first_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('phone_Number', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('last_Name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'user_name')
    op.add_column('buyers', sa.Column('seller_id', sa.INTEGER(), nullable=False))
    op.add_column('buyers', sa.Column('buyer_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(op.f('fk_buyers_user_id_users'), 'buyers', type_='foreignkey')
    op.create_foreign_key('fk_buyers_buyer_id_users', 'buyers', 'users', ['buyer_id'], ['id'])
    op.create_foreign_key('fk_buyers_seller_id_users', 'buyers', 'users', ['seller_id'], ['id'])
    op.drop_table('cars')
    # ### end Alembic commands ###
