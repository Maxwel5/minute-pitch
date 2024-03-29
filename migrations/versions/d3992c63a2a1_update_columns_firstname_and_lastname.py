"""Update columns firstname and lastname

Revision ID: d3992c63a2a1
Revises: 7374c09354f5
Create Date: 2019-09-19 17:13:14.469209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3992c63a2a1'
down_revision = '7374c09354f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('users_firstname_key', 'users', type_='unique')
    op.drop_constraint('users_lastname_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_lastname_key', 'users', ['lastname'])
    op.create_unique_constraint('users_firstname_key', 'users', ['firstname'])
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
