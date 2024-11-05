from marshmallow import Schema, fields, validate, validates, ValidationError, pre_load
from models.tank import Tank
from datetime import datetime


class TankSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    capacity = fields.Float(required=True, validate=validate.Range(min=0))
    number = fields.Number(required=True, validate=validate.Range(min=0))

    @validates("name")
    def validate_name(self, name):
        if name.strip() == "":
            raise ValidationError(
                "O nome do tank não pode estar vazio ou conter apenas espaços em branco."
            )

    @validates("capacity")
    def validate_capacidade(self, capacity):
        if capacity <= 0:
            raise ValidationError("A capacidade do tank deve ser maior que zero.")

    @validates("number")
    def validate_number(self, number):
        if number <= 0:
            raise ValidationError("O número do tank deve ser maior que zero.")
    
