"""Initial migration

Revision ID: e619f1bd1eee
Revises:
Create Date: 2023-12-03 03:03:01.566414
"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e619f1bd1eee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'address',
        sa.Column('lat', sa.String(), nullable=True),
        sa.Column('lng', sa.String(), nullable=True),
        sa.Column('street', sa.String(), nullable=True),
        sa.Column('neighborhood', sa.String(), nullable=True),
        sa.Column('city', sa.String(), nullable=True),
        sa.Column('state', sa.String(), nullable=True),
        sa.Column('number', sa.Integer(), nullable=True),
        sa.Column('postal_code', sa.String(), nullable=True),
        sa.Column('additional', sa.String(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_by', sa.Integer(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['updated_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'user',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address_id', sa.Integer(), nullable=True),
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_by', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_by', sa.Integer(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['address_id'],
            ['address.id'],
        ),
        sa.ForeignKeyConstraint(
            ['updated_by'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('address')
    # ### end Alembic commands ###