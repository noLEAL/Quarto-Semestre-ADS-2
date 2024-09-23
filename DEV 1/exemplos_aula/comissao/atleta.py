from _datetime import datetime

class Atleta():

    def __init__(self, name, birth_date, sport, payment: bool, responsible=None):
        """Documentaçao"""

        try:
            birth_date = datetime.fromisoformat(birth_date)
            if ((datetime.today() - birth_date).days / 365.25) < 18:
                if responsible is None:
                    raise TypeError("Menor de idade sem responsável")
            self.nome = name
            self.pagamento = payment
            if payment is True:
                self.valor = 100
            else:
                raise TypeError("Atleta sem pagamento, Agendar com o responsável")
            self.data_nascimento = birth_date
            self.esporte = sport
            self.responsavel = responsible
        except Exception as e:
            raise e

    def __str__(self):
        """Documentação"""

        if self.responsavel is None:
            return f"{self.nome} - {self.esporte}"
        else:
            return f"{self.nome} - {self.esporte} - {self.responsavel}"