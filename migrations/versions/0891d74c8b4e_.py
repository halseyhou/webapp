"""empty message

Revision ID: 0891d74c8b4e
Revises: 
Create Date: 2022-10-06 21:03:20.175478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0891d74c8b4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('account_created', sa.String(length=256), nullable=False),
    sa.Column('account_updated', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    # ### end Alembic commands ###
