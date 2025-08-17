"""add_more_locations

Revision ID: 44939183aaf6
Revises: 3899ebfaf023
Create Date: 2025-08-15 14:42:46.613262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44939183aaf6'
down_revision: Union[str, None] = '3899ebfaf023'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""INSERT INTO location (city, country, latitude, longitude, is_active)
                  VALUES 
                    ('Lviv', 'Ukraine', 49.8327706, 23.9298344, true),
                    ('Vilnius', 'Lithuania', 54.7006341, 24.923392, true),
                    ('Stockholm', 'Sweden', 59.303674, 17.774343, true),
                    ('Helsinki', 'Finland', 60.1100963, 24.6890459, true),
                    ('Berlin', 'Germany', 52.5068041, 13.0950873, true),
                    ('London', 'UK', 51.528607, -0.4312443, true),
                    ('Paris', 'France', 48.8586604, 2.0351995, true),
                    ('Madrid', 'Spain', 40.4380986, -3.8443488, true),
                    ('Athens', 'Greece', 37.9909438, 23.6559374, true),
                    ('Istanbul', 'Türkiye', 40.9996213, 27.7634529, true);""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DELETE FROM location WHERE city in ('Lviv', 'Vilnius', 'Stockholm', 'Helsinki', 'Berlin',
                                                      'London', 'Paris', 'Madrid', 'Athens', 'Istanbul');""")
