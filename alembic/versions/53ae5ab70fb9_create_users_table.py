"""Create users table

Revision ID: 53ae5ab70fb9
Revises: 
Create Date: 2021-11-05 17:58:39.246757

"""
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53ae5ab70fb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
