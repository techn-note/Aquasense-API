from marshmallow import Schema, fields, validate, validates, ValidationError
from models.peixe import Peixe

class PeixeSchema(Schema):
    id = fields.Str(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=1))
    idade = fields.Int(required=True, validate=validate.Range(min=0))
    especie = fields.Str(required=True, validate=validate.Length(min=1))
    peso = fields.Float(required=True, validate=validate.Range(min=0))
    quantidade = fields.Int(required=True, validate=validate.Range(min=1))

    @validates('nome')
    def validate_nome(self, nome):
        if nome.strip() == "":
            raise ValidationError("O nome do peixe não pode estar vazio ou conter apenas espaços em branco.")