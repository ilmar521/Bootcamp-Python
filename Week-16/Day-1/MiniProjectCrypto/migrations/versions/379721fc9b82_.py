"""empty message

Revision ID: 379721fc9b82
Revises: 
Create Date: 2023-04-25 17:44:05.674083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '379721fc9b82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crypto',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('symbol', sa.String(length=64), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('first_historical_data', sa.String(length=64), nullable=True),
    sa.Column('last_historical_data', sa.String(length=64), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_crypto',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('crypto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['crypto_id'], ['crypto.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_crypto')
    op.drop_table('user')
    op.drop_table('crypto')
    # ### end Alembic commands ###