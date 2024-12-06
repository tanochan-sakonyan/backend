"""Initial migration with updated Status Enum

Revision ID: 9f121debca01
Revises: 
Create Date: 2024-12-06 18:23:21.211382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f121debca01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('line_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_group_id', sa.String(length=64), nullable=False),
    sa.Column('line_group_name', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('line_groups', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_line_groups_line_group_id'), ['line_group_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_line_groups_line_group_name'), ['line_group_name'], unique=False)

    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('line_user_id', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('paypay_url', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('line_user_id')
    )
    op.create_table('events',
    sa.Column('event_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('event_name', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('line_group_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('line_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_user_id', sa.String(length=64), nullable=False),
    sa.Column('line_user_name', sa.String(length=64), nullable=False),
    sa.Column('line_group_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['line_group_id'], ['line_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('line_users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_line_users_line_user_id'), ['line_user_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_line_users_line_user_name'), ['line_user_name'], unique=False)

    op.create_table('members',
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('member_name', sa.String(length=64), nullable=False),
    sa.Column('line_user_id', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Enum('PAID', 'UNPAID', 'ABSENCE', name='status'), nullable=False),
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
    with op.batch_alter_table('line_users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_line_users_line_user_name'))
        batch_op.drop_index(batch_op.f('ix_line_users_line_user_id'))

    op.drop_table('line_users')
    op.drop_table('events')
    op.drop_table('users')
    with op.batch_alter_table('line_groups', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_line_groups_line_group_name'))
        batch_op.drop_index(batch_op.f('ix_line_groups_line_group_id'))

    op.drop_table('line_groups')
    # ### end Alembic commands ###