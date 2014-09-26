"""create new models

Revision ID: 3bfca079f84d
Revises: 2d09d1fbf56b
Create Date: 2014-08-12 22:14:24.540282

"""

# revision identifiers, used by Alembic.
revision = '3bfca079f84d'
down_revision = '2d09d1fbf56b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.create_table('pystock_currency',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('code', sa.String(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_monetary_source',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_dividend',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('announce_date', sa.DateTime(), nullable=True),
        sa.Column('exdividend_date', sa.DateTime(), nullable=True),
        sa.Column('record_date', sa.DateTime(), nullable=True),
        sa.Column('payment_date', sa.DateTime(), nullable=True),
        sa.Column('amount', sa.DECIMAL(), nullable=True),
        sa.Column('asset_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['asset_id'], ['pystock_asset.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_fxrates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('monetary_source_id', sa.Integer(), nullable=True),
        sa.Column('from_currency_id', sa.Integer(), nullable=True),
        sa.Column('to_curreny_id', sa.Integer(), nullable=True),
        sa.Column('buy_rate', sa.DECIMAL(), nullable=True),
        sa.Column('sell_rate', sa.DECIMAL(), nullable=True),
        sa.ForeignKeyConstraint(['from_currency_id'], ['pystock_currency.id'], ),
        sa.ForeignKeyConstraint(['monetary_source_id'], ['pystock_monetary_source.id'], ),
        sa.ForeignKeyConstraint(['to_curreny_id'], ['pystock_currency.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_split',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('announce_date', sa.DateTime(), nullable=True),
        sa.Column('split_date', sa.DateTime(), nullable=True),
        sa.Column('ratio', sa.Integer(), nullable=True),
        sa.Column('asset_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['asset_id'], ['pystock_asset.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ## end Alembic commands ###


def downgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.drop_table('pystock_split')
    op.drop_table('pystock_fxrates')
    op.drop_table('pystock_dividend')
    op.drop_table('pystock_monetary_source')
    op.drop_table('pystock_currency')
    # ## end Alembic commands ###