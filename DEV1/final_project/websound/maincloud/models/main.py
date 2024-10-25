from maincloud.models.base import BaseModel


class Main(BaseModel):
    """Documentação da classe"""

    def clean(self):
        return "off"