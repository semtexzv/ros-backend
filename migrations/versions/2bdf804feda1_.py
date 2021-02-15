"""empty message

Revision ID: 2bdf804feda1
Revises: dd6d7004dda2
Create Date: 2021-02-15 20:49:22.007003

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2bdf804feda1'
down_revision = 'dd6d7004dda2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('performance_profile', sa.Column('system_id', sa.Integer(), nullable=False))
    op.drop_constraint('performance_profile_inventory_id_report_date_key', 'performance_profile', type_='unique')
    op.create_unique_constraint(None, 'performance_profile', ['report_date'])
    op.create_foreign_key(None, 'performance_profile', 'systems', ['system_id'], ['id'])
    op.drop_column('performance_profile', 'inventory_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('performance_profile', sa.Column('inventory_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'performance_profile', type_='foreignkey')
    op.drop_constraint(None, 'performance_profile', type_='unique')
    op.create_unique_constraint('performance_profile_inventory_id_report_date_key', 'performance_profile', ['inventory_id', 'report_date'])
    op.drop_column('performance_profile', 'system_id')
    # ### end Alembic commands ###
