"""addSubMetaData

Revision ID: b8cf7fa342bb
Revises: 608afa719fb8
Create Date: 2016-04-04 09:38:39.555000

"""

# revision identifiers, used by Alembic.
revision = 'b8cf7fa342bb'
down_revision = '608afa719fb8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_error_data():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('agency_name', sa.Text(), nullable=True))
    op.add_column('submission', sa.Column('reporting_end_date', sa.Date(), nullable=True))
    op.add_column('submission', sa.Column('reporting_start_date', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade_job_tracker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'reporting_start_date')
    op.drop_column('submission', 'reporting_end_date')
    op.drop_column('submission', 'agency_name')
    ### end Alembic commands ###

