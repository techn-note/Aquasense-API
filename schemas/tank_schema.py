from marshmallow import Schema, fields, validate, validates, ValidationError
from models.tank import Tank 

class TankSchema(Schema):
    id = fields.Str(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=1))
    capacidade = fields.Float(required=True, validate=validate.Range(min=0))

    @validates('nome')
    def validate_nome(self, nome):
        if nome.strip() == "":
            raise ValidationError("O nome do tank não pode estar vazio ou conter apenas espaços em branco.")

    @validates('capacidade')
    def validate_capacidade(self, capacidade):
        if capacidade <= 0:
            raise ValidationError("A capacidade do tank deve ser maior que zero.")
