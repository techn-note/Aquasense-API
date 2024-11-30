from marshmallow import Schema, fields, validate, validates, ValidationError
from models.atualizacao import Atualizacao

class AtualizacaoSchema(Schema):
    id = fields.Str(dump_only=True)
    mensagem = fields.Str(required=True, validate=validate.Length(min=1))
    data = fields.Str(required=True)
    tipo = fields.Str(required=True, validate=validate.OneOf(['Alerta', 'Padrao']))
    tanque = fields.Str(required=True, validate=validate.Length(min=1))

    @validates('mensagem')
    def validate_mensagem(self, mensagem):
        if mensagem.strip() == "":
            raise ValidationError("A mensagem não pode estar vazia ou conter apenas espaços em branco.")