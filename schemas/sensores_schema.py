from marshmallow import Schema, fields, validate, validates, ValidationError
from models.tank import Tank
from models.sensores import Sensor

class SensorSchema(Schema):
    id = fields.Str(dump_only=True)
    tipo = fields.Str(required=True, validate=validate.Length(min=1))
    data = fields.Str(required=True)
    valor = fields.Float(required=True, validate=validate.Range(min=0))
    tanque = fields.Str(required=True)

    @validates('tipo')
    def validate_tipo(self, tipo):
        if tipo.strip() == "":
            raise ValidationError("O tipo de sensor não pode estar vazio ou conter apenas espaços em branco.")

    @validates('valor')
    def validate_valor(self, valor):
        if valor < 0:
            raise ValidationError("O valor do sensor deve ser maior ou igual a zero.")