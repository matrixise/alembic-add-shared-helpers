"""use_function

Revision ID: 53653e1d9474
Revises: 
Create Date: 2021-10-20 11:40:37.837300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53653e1d9474'
down_revision = None
branch_labels = None
depends_on = None


import my_helpers

def upgrade():
    print(my_helpers.function())


def downgrade():
    pass
