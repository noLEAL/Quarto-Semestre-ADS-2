from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# def CodValidator(valor):
#     if valor == "0000000000":
#         raise  ValidationError(_("Valor invalido"), params={"valor": valor}, code='invalid')