"""empty message

Revision ID: f398b261d9c6
Revises: 9d6adad83936
Create Date: 2021-03-23 10:30:53.499533

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f398b261d9c6'
down_revision = '9d6adad83936'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('metric2', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('metric2', sa.Column('name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
