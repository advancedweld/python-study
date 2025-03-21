"""empty message

Revision ID: 6ffbb9a77890
Revises: 24e5e2f699ec
Create Date: 2025-02-18 16:58:19.853032

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ffbb9a77890'
down_revision = '24e5e2f699ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('pwd',
               existing_type=mysql.VARCHAR(length=102),
               type_=sa.String(length=255),
               existing_comment='密码',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('pwd',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=102),
               existing_comment='密码',
               existing_nullable=True)

    # ### end Alembic commands ###
