"""Add event_id foreign key to Member

Revision ID: 49e6bc32f23c
Revises: 72a444f25a5f
Create Date: 2024-11-10 19:40:58.696685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49e6bc32f23c'
down_revision = '72a444f25a5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('event_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('event_name', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('members',
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('member_name', sa.String(length=64), nullable=False),
    sa.Column('line_user_id', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Enum('UNPAID', 'PAID', 'ABSENCE', name='status'), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.event_id'], ),
    sa.PrimaryKeyConstraint('member_id')
    )
    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_members_line_user_id'), ['line_user_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_members_member_name'), ['member_name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('members', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_members_member_name'))
        batch_op.drop_index(batch_op.f('ix_members_line_user_id'))

    op.drop_table('members')
    op.drop_table('events')
    # ### end Alembic commands ###