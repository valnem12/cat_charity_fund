"""3nd migration

Revision ID: e91abeb7a83c
Revises: 582a74ba81be
Create Date: 2022-09-18 13:52:49.962409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91abeb7a83c'
down_revision = '582a74ba81be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.CheckConstraint('full_amount > 0'),
    sa.CheckConstraint('invested_amount <= full_amount'),
    sa.CheckConstraint('invested_amount >= 0'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donation')
    # ### end Alembic commands ###