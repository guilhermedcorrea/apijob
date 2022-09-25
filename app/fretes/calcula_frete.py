import re
from itertools import groupby

class RetetornaCalculoFrete:
    def __init__(self, sku, quant, peso, alt,larg,comp):
        self.sku = sku
        self.quant = quant
        self.peso = peso
        self.alt = alt
        self.larg = larg
        self.comp = comp


    def soma_valores(self):
        pass
    

    #Getters e Setters
    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, valor):
        if isinstance(valor, str):
            self._sku = valor
            return valor
        else:
            self._sku = 0

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, valor):
        if isinstance(valor, str):
            self._quant = valor
            return valor
        else:
            self._quant = float(0)


    

    
