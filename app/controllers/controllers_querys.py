from datetime import datetime
from functools import wraps
from sqlalchemy import text
import re
from extensions import db


#Recebe Parametros vindos da Rota '/api/v1/fretes/add' de cotação e dos Crawlers montados em cima do 'https://melhorenvio.com.br/' (Cotação do frete)
# E do www.kabum.com.br (Onde é feita a extração dos produtos que serão usados nas cotações)
def call_procedute_insert_database(f):
    @wraps(f)
    def call_procedure_produtos(*args, **kwargs):
        print('Calling decorated function')
        return f(*args, **kwargs)
    return call_procedure_produtos


@call_procedute_insert_database
def log_cadastro(*args, **kwargs):
    """Recebe Parametros de entrada"""

    print('Called example function')


class ProdutoFrete:
    def __init__(self, sku, cep, prazo, quantidade, preco):
        self.dataatual = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
        self.sku = sku
        self.cep = cep
        self.prazo = prazo
        self.quantidade = quantidade
        self.preco = preco


    def remove_caracteres_cep(self, *args, **kwargs):
        refs = re.compile(r"\d+")
        try:
            cep = kwargs.get('cep')
            filter_cep = re.search(refs, cep)
            cep_values = filter_cep.replace(" ","").strip()
            return cep_values
        except:
            raise "notFound"


class Produto:
    def __init__(self,sku, idproduto, dias, data):
        self.dataatual = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
        self.sku = sku
        self.idproduto = idproduto
        self.dias = dias
        self.data = data

    def select_sku(self, sku):
        """
            recebe SKU vindo do Endpoint /api/v1/fretes/add Checa na tabela se existe
            Caso nao exista Invoca a função 'call_procedure_produtos' que executa a procedure que realiza o Cadastro "Lança uma exceção Pedindo para tentar novamente"
            "Caso nao consiga cadastrar o item lança uma nova exceção status 500"
            Em caso de erro ou a função Lambda retorno None é lançada uma exceção Invocada pelo Abort lançando 'erro 500' 
        """
        with db.engine.connect() as conn:
            query_sku = (text("""SELECT idproduto, skuproduto, peso, altura, 
                largura, bitativo, dataalterado
                WHERE skuproduto IN ('{}')
                FROM public.produto""".format(sku)))

            exec_query = conn.execute(exec).all()
            if next(filter(lambda x: x[0] == self.sku, exec_query), None):
                dict_item = {}
                dict_item['SKU'] = exec_query.get('skuproduto')
                dict_item['IDPRODUTO'] = exec_query.get('idproduto')
                dict_item['PESO'] = exec_query.get('peso')
                dict_item['ALTURA'] = exec_query.get('altura')
                dict_item['LARGURA'] = exec_query.get('largura')
                #dict_item['COMPRIMENTO'] = exec_query.get('')
                dict_item['dataalterado'] = exec_query.get('dataalterado')


                yield dict_item


    def insert_valores(self, *args, **kwargs):
        pass


    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, valor):
        if isinstance(valor, str):
            self._sku = valor
            return valor
        else:
            self._sku = 'naoencontrado'

    @property
    def cep(self):
        return self._cep

    @sku.setter
    def sku(self, valor):
        if isinstance(valor, str):
            self._cep = valor
            return valor
        else:
            self._cep = 'naoencontrado'


    @property
    def dias(self):
        return self._dias

    @sku.setter
    def sku(self, valor):
        if isinstance(valor, str):
            self._dias = valor
            return valor
        else:
            self._dias= 'naoencontrado'


        




    








           


    def insert_valores(self):
        pass


    