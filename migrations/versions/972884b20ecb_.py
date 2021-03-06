"""empty message

Revision ID: 972884b20ecb
Revises: 4f04b9e9fe90
Create Date: 2020-05-17 18:22:02.396504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '972884b20ecb'
down_revision = '4f04b9e9fe90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts_has_tags',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts_has_tags')
    # ### end Alembic commands ###
