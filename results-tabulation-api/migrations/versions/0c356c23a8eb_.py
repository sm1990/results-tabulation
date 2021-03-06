"""empty message

Revision ID: 0c356c23a8eb
Revises: dac224818b28
Create Date: 2019-09-23 12:31:26.019363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c356c23a8eb'
down_revision = 'dac224818b28'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tallySheetVersionRow_CE_201_ballotBox',
    sa.Column('tallySheetVersionRowId', sa.Integer(), nullable=False),
    sa.Column('ballotBoxStationaryItemId', sa.Integer(), nullable=False),
    sa.Column('invoiceStage', sa.Enum('Issued', 'Received', name='invoicestageenum'), nullable=False),
    sa.ForeignKeyConstraint(['ballotBoxStationaryItemId'], ['ballotBox.stationaryItemId'], ),
    sa.ForeignKeyConstraint(['tallySheetVersionRowId'], ['tallySheetVersionRow_CE_201.tallySheetVersionRowId'], ),
    sa.PrimaryKeyConstraint('tallySheetVersionRowId', 'ballotBoxStationaryItemId', 'invoiceStage')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tallySheetVersionRow_CE_201_ballotBox')
    ### end Alembic commands ###
