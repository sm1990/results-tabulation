"""empty message

Revision ID: 3c39e8314e54
Revises: bf706f2aa738
Create Date: 2019-11-12 12:44:45.265053

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3c39e8314e54'
down_revision = 'bf706f2aa738'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('election_candidate', 'qualifiedForPreferences',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('invoice', 'confirmed',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('invoice', 'delete',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('invoice_stationaryItem', 'received',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('proof', 'finished',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.add_column('submission', sa.Column('notifiedStampId', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('notifiedVersionId', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('releasedStampId', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('releasedVersionId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'submission', 'stamp', ['releasedStampId'], ['stampId'])
    op.create_foreign_key(None, 'submission', 'submissionVersion', ['releasedVersionId'], ['submissionVersionId'])
    op.create_foreign_key(None, 'submission', 'stamp', ['notifiedStampId'], ['stampId'])
    op.create_foreign_key(None, 'submission', 'submissionVersion', ['notifiedVersionId'], ['submissionVersionId'])
    op.alter_column('tallySheetVersion', 'isComplete',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tallySheetVersion', 'isComplete',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_column('submission', 'releasedVersionId')
    op.drop_column('submission', 'releasedStampId')
    op.drop_column('submission', 'notifiedVersionId')
    op.drop_column('submission', 'notifiedStampId')
    op.alter_column('proof', 'finished',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('invoice_stationaryItem', 'received',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('invoice', 'delete',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('invoice', 'confirmed',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.alter_column('election_candidate', 'qualifiedForPreferences',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    ### end Alembic commands ###
