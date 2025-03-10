"""Added email to User and created_at to Board.

Revision ID: d2035fa723b9
Revises: 
Create Date: 2024-11-14 16:40:13.009567

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2035fa723b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.String(length=200), nullable=False))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.create_unique_constraint(None, ['email'])
        batch_op.create_unique_constraint(None, ['address'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('address')

    # ### end Alembic commands ###
