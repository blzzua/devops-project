"""add html render

Revision ID: 9d9ef8c620d5
Revises: 53ae5ab70fb9
Create Date: 2021-11-06 21:40:10.579117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d9ef8c620d5'
down_revision = '53ae5ab70fb9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
            sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")