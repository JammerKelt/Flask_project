"""Create users table

Revision ID: 25aa4b76fba6
Revises: 
Create Date: 2018-10-01 06:15:05.594934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25aa4b76fba6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.String),
        sa.Column("password", sa.String)
    )


def downgrade():
    op.drop_table("user")
