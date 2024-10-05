class Carro():
    """Documentação"""

    def __init__(self, brand, model, year, plate, indentification, color, side_color, speed, consumption, kind_fuel):
        """Documentação"""

        self.marca = brand
        self.modelo = model
        self.ano = year
        self.placa = plate
        self.indentificacao = indentification
        self.cor = color
        self.cor_lateral = side_color
        self.velocidade = speed
        self.consumo = consumption
        self.tipo_compustivel = kind_fuel

    def __str__(self):
        """Documentacao"""

        retorno = "Carro: {} - {}\n".format(self.marca, self.modelo)
        retorno += "Intentificação: {} - {}\n".format(self.placa, self.indentificacao)
        retorno += "Ano: {}\n".format(self.ano, self.velocidade)
        retorno += "Cor: {} - {} \n".format(self.cor, self.cor_lateral)
        retorno += "Consumo: {}\n".format(self.consumo)
        retorno += "Combustível: {}\n".format(self.tipo_compustivel)
        return retorno
