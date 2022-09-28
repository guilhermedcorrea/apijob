"""empty message

Revision ID: 9a3d00b68ceb
Revises: 
Create Date: 2022-09-28 01:02:31.048762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a3d00b68ceb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marcaproduto',
    sa.Column('idmarca', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=100), nullable=True),
    sa.Column('datacadastro', sa.DateTime(), nullable=True),
    sa.Column('bitativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('idmarca')
    )
    op.create_table('usuarios',
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('bitusuario', sa.Boolean(), nullable=False),
    sa.Column('bitlogado', sa.Boolean(), nullable=False),
    sa.Column('datalogado', sa.DateTime(), nullable=True),
    sa.Column('datacadastro', sa.DateTime(), nullable=True),
    sa.Column('bitativo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.create_table('produto',
    sa.Column('idproduto', sa.Integer(), nullable=False),
    sa.Column('skuproduto', sa.String(length=300), nullable=True),
    sa.Column('nomeproduto', sa.String(length=1000), nullable=True),
    sa.Column('idmarca', sa.Integer(), nullable=True),
    sa.Column('urlpaginaproduto', sa.String(length=2000), nullable=True),
    sa.Column('peso', sa.Float(), nullable=True),
    sa.Column('altura', sa.Float(), nullable=True),
    sa.Column('largura', sa.Float(), nullable=True),
    sa.Column('comprimento', sa.Float(), nullable=True),
    sa.Column('bitativo', sa.Boolean(), nullable=True),
    sa.Column('dataalterado', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['idmarca'], ['marcaproduto.idmarca'], ),
    sa.PrimaryKeyConstraint('idproduto')
    )
    op.create_table('cotacaofrete',
    sa.Column('idfrete', sa.Integer(), nullable=False),
    sa.Column('idmarca', sa.Integer(), nullable=True),
    sa.Column('idproduto', sa.Integer(), nullable=True),
    sa.Column('cep', sa.String(length=20), nullable=True),
    sa.Column('categoriafrete', sa.String(length=50), nullable=True),
    sa.Column('valorFrete', sa.Float(), nullable=True),
    sa.Column('prazo', sa.Integer(), nullable=True),
    sa.Column('transportadora', sa.String(length=200), nullable=True),
    sa.Column('dacotacao', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['idmarca'], ['marcaproduto.idmarca'], ),
    sa.ForeignKeyConstraint(['idproduto'], ['produto.idproduto'], ),
    sa.PrimaryKeyConstraint('idfrete')
    )
    op.create_table('logusuario',
    sa.Column('idlog', sa.Integer(), nullable=False),
    sa.Column('idusuario', sa.Integer(), nullable=True),
    sa.Column('freteid', sa.Integer(), nullable=True),
    sa.Column('prazo', sa.Integer(), nullable=True),
    sa.Column('valor', sa.Float(), nullable=True),
    sa.Column('transportadora', sa.String(length=100), nullable=True),
    sa.Column('idproduto', sa.Integer(), nullable=True),
    sa.Column('datalog', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['freteid'], ['cotacaofrete.idfrete'], ),
    sa.ForeignKeyConstraint(['idusuario'], ['usuarios.id_usuario'], ),
    sa.PrimaryKeyConstraint('idlog')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logusuario')
    op.drop_table('cotacaofrete')
    op.drop_table('produto')
    op.drop_table('usuarios')
    op.drop_table('marcaproduto')
    # ### end Alembic commands ###