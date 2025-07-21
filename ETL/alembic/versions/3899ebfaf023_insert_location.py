"""Insert Location

Revision ID: 3899ebfaf023
Revises: f78dee95ba59
Create Date: 2025-06-07 18:19:24.538074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3899ebfaf023'
down_revision: Union[str, None] = 'f78dee95ba59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""INSERT INTO location (city, country, latitude, longitude, is_active)
                  VALUES ('Kyiv', 'Ukraine', 50.3755194, 30.5361674, true);""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DELETE FROM location WHERE city = 'Kyiv';""")
