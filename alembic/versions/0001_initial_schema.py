"""Initial schema - all tables

Revision ID: 0001
Revises:
Create Date: 2026-03-27
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '0001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'departments',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('name'),
    )

    op.create_table(
        'job_titles',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('title', sa.String(150), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('title'),
    )

    op.create_table(
        'roles',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('name'),
    )

    op.create_table(
        'templates',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('html_content', sa.Text(), nullable=False),
        sa.Column('is_default', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('name'),
    )

    op.create_table(
        'brand_settings',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('company_name', sa.String(200), nullable=False),
        sa.Column('unit_name', sa.String(200), nullable=False),
        sa.Column('website_url', sa.String(500), nullable=False),
        sa.Column('logo_url', sa.String(500), nullable=False),
        sa.Column('primary_color', sa.String(20), nullable=False),
        sa.Column('secondary_color', sa.String(20), nullable=False),
        sa.Column('disclaimer_html', sa.Text(), nullable=False, server_default=sa.text("''")),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )

    op.create_table(
        'employees',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('full_name', sa.String(200), nullable=False),
        sa.Column('corporate_email', sa.String(254), nullable=False),
        sa.Column('phone', sa.String(30), nullable=True),
        sa.Column('mobile_phone', sa.String(30), nullable=True),
        sa.Column('linkedin_url', sa.String(500), nullable=True),
        sa.Column('job_title_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('department_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['department_id'], ['departments.id']),
        sa.ForeignKeyConstraint(['job_title_id'], ['job_titles.id']),
        sa.UniqueConstraint('corporate_email'),
    )

    op.create_table(
        'system_users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('email', sa.String(254), nullable=False),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id']),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email'),
    )

    op.create_table(
        'email_signatures',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('employee_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('template_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('html_content', sa.Text(), nullable=False),
        sa.Column('full_name', sa.String(200), nullable=False),
        sa.Column('job_title', sa.String(150), nullable=False),
        sa.Column('department', sa.String(100), nullable=False),
        sa.Column('corporate_email', sa.String(254), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['employee_id'], ['employees.id']),
        sa.ForeignKeyConstraint(['template_id'], ['templates.id']),
    )

    op.execute(
        sa.text(
            "INSERT INTO brand_settings "
            "(id, company_name, unit_name, website_url, logo_url, primary_color, secondary_color, disclaimer_html) "
            "VALUES (gen_random_uuid(), \'BT Blue\', \'BT Blue\', \'https://btblue.com.br\', "
            "        \'https://btblue.com.br/logo.png\', \'#0057A8\', \'#FF6B00\', \'\')"
        )
    )


def downgrade() -> None:
    op.drop_table('email_signatures')
    op.drop_table('system_users')
    op.drop_table('employees')
    op.drop_table('brand_settings')
    op.drop_table('templates')
    op.drop_table('roles')
    op.drop_table('job_titles')
    op.drop_table('departments')
