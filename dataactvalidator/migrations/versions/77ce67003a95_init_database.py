"""init database

Revision ID: 77ce67003a95
Revises: 
Create Date: 2016-03-17 10:55:12.500468

"""

# revision identifiers, used by Alembic.
revision = '77ce67003a95'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field_type',
    sa.Column('field_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('field_type_id')
    )
    op.create_table('file_type',
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('file_id')
    )
    op.create_table('multi_field_rule_type',
    sa.Column('multi_field_rule_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('multi_field_rule_type_id')
    )
    op.create_table('rule_type',
    sa.Column('rule_type_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('rule_type_id')
    )
    op.create_table('tas_lookup',
    sa.Column('tas_id', sa.Integer(), nullable=False),
    sa.Column('allocation_transfer_agency', sa.Text(), nullable=True),
    sa.Column('agency_identifier', sa.Text(), nullable=True),
    sa.Column('beginning_period_of_availability', sa.Text(), nullable=True),
    sa.Column('ending_period_of_availability', sa.Text(), nullable=True),
    sa.Column('availability_type_code', sa.Text(), nullable=True),
    sa.Column('main_account_code', sa.Text(), nullable=True),
    sa.Column('sub_account_code', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('tas_id')
    )
    op.create_table('file_columns',
    sa.Column('file_column_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('field_types_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('required', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['field_types_id'], ['field_type.field_type_id'], ),
    sa.ForeignKeyConstraint(['file_id'], ['file_type.file_id'], ),
    sa.PrimaryKeyConstraint('file_column_id')
    )
    op.create_table('multi_field_rule',
    sa.Column('multi_field_rule_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=True),
    sa.Column('multi_field_rule_type_id', sa.Integer(), nullable=True),
    sa.Column('rule_text_1', sa.Text(), nullable=True),
    sa.Column('rule_text_2', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file_type.file_id'], ),
    sa.ForeignKeyConstraint(['multi_field_rule_type_id'], ['multi_field_rule_type.multi_field_rule_type_id'], ),
    sa.PrimaryKeyConstraint('multi_field_rule_id')
    )
    op.create_table('rule',
    sa.Column('rule_id', sa.Integer(), nullable=False),
    sa.Column('file_column_id', sa.Integer(), nullable=True),
    sa.Column('rule_type_id', sa.Integer(), nullable=True),
    sa.Column('rule_text_1', sa.Text(), nullable=True),
    sa.Column('rule_text_2', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['file_column_id'], ['file_columns.file_column_id'], ),
    sa.ForeignKeyConstraint(['rule_type_id'], ['rule_type.rule_type_id'], ),
    sa.PrimaryKeyConstraint('rule_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule')
    op.drop_table('multi_field_rule')
    op.drop_table('file_columns')
    op.drop_table('tas_lookup')
    op.drop_table('rule_type')
    op.drop_table('multi_field_rule_type')
    op.drop_table('file_type')
    op.drop_table('field_type')
    ### end Alembic commands ###
