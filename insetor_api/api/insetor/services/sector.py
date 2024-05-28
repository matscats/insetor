from api.insetor.models.sector import Sector
from django.core.exceptions import ValidationError


def _handle_code_out_of_bound(code: int) -> ValidationError:
    raise ValidationError("O código deve ser um número entre 0 e 999")


def create_sector(name: str, code: int) -> Sector:
    # Aqui podemos adicionar alguma lógica customizada para validação, por exemplo, vamos
    # garantir que o código do setor não pode ser um número maior do que 999 ou menor do que
    # 0
    if code < 0 or code > 999:
        return _handle_code_out_of_bound(code)

    sector = Sector.objects.create(name=name, code=code)

    return sector
