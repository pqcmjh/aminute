"""empty message

Revision ID: c072e55bc4c7
Revises: ff12276c797c
Create Date: 2018-08-28 21:01:13.301771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c072e55bc4c7'
down_revision = 'ff12276c797c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('house', sa.Column('current_date', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('house', 'current_date')
    # ### end Alembic commands ###
