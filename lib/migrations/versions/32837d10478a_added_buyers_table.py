"""Added buyers table

Revision ID: 32837d10478a
Revises: eb606623cd1e
Create Date: 2023-09-06 19:36:45.724105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32837d10478a'
down_revision = 'eb606623cd1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'buyers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('buyer_id', sa.Integer(), nullable=False),
        sa.Column('seller_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['buyer_id'], ['users.id'], name='fk_buyers_buyer_id_users'),
        sa.ForeignKeyConstraint(['seller_id'], ['users.id'], name='fk_buyers_seller_id_users'),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_Number', sa.INTEGER(), nullable=True))
    op.add_column('users', sa.Column('first_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('user_Name', sa.VARCHAR(), nullable=True))
    op.add_column('users', sa.Column('last_Name', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone_number')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_column('users', 'user_name')
    # ### end Alembic commands ###
