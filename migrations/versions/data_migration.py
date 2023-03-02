from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'data_migration'
down_revision = '3d73052ed6db'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table('user',
                       column('id', sa.Integer()),
                       column('username', sa.String(length=80)),
                       column('email', sa.String(length=255)),
                       column('is_staff', sa.Boolean()),
                       )

    op.bulk_insert(user_table, [{"id": 3, "username": "blog_admin", "email": "admin@blog.com", "is_staff": True}])


def downgrade():
    pass
