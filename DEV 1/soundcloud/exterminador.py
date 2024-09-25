
class Exterminador:
    @staticmethod
    def exterminar_string(string: str):
        """função responsavel para filtrar uma string onde seja so possivel receber 1 a 100 caracteres"""
        if 1 > len(string) > 100:
            return True