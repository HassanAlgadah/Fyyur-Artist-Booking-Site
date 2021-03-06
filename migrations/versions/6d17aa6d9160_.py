"""empty message

Revision ID: 6d17aa6d9160
Revises: f94d01262abb
Create Date: 2020-05-11 08:13:34.204914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d17aa6d9160'
down_revision = 'f94d01262abb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
