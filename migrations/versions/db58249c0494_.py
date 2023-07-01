"""empty message

Revision ID: db58249c0494
Revises: 9f3ee8f9c7b2
Create Date: 2023-07-01 09:20:34.838033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db58249c0494'
down_revision = '9f3ee8f9c7b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('teacher', sa.String(length=50), nullable=True))

    with op.batch_alter_table('electives', schema=None) as batch_op:
        batch_op.add_column(sa.Column('teacher', sa.String(length=50), nullable=True))

    with op.batch_alter_table('groups', schema=None) as batch_op:
        op.execute("CREATE TYPE group_type_enum AS ENUM ('B', 'M')")
        batch_op.add_column(sa.Column('type', sa.Enum('B', 'M', name='group_type_enum'), nullable=True))
        batch_op.add_column(sa.Column('year', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('number', sa.Integer(), nullable=True))
        batch_op.drop_column('group_year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group_year', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('number')
        batch_op.drop_column('year')
        batch_op.drop_column('type')

    with op.batch_alter_table('electives', schema=None) as batch_op:
        batch_op.drop_column('teacher')

    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.drop_column('teacher')

    # ### end Alembic commands ###