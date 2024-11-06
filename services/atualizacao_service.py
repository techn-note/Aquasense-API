from models.atualizacao import Atualizacao
from schemas.atualizacao_schema import AtualizacaoSchema
from marshmallow import ValidationError

atualizacao_schema = AtualizacaoSchema()

def create_atualizacao_service(mensagem, data, tipo, tanque):
    atualizacao_data = {
        "mensagem": mensagem,
        "data": data,
        "tipo": tipo,
        "tanque": tanque
    }

    try:
        validated_data = atualizacao_schema.load(atualizacao_data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = Atualizacao.create_atualizacao(validated_data)
    return {"atualizacao_id": str(result.inserted_id)}, 201

def get_atualizacao_service(atualizacao_id):
    atualizacao = Atualizacao.get_atualizacao(atualizacao_id)
    
    if not atualizacao:
        return {"error": "Atualização não encontrada"}, 404
    
    return atualizacao_schema.dump(atualizacao), 200

def get_all_atualizacoes_service():
    atualizacoes = Atualizacao.get_all_atualizacoes()
    return atualizacao_schema.dump(atualizacoes, many=True), 200

def update_atualizacao_service(atualizacao_id, update_data):
    try:
        validated_data = atualizacao_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Atualizacao.update_atualizacao(atualizacao_id, validated_data)
    
    if updated.matched_count == 0:
        return {"error": "Atualização não encontrada"}, 404
    
    return {"message": "Atualização atualizada com sucesso"}, 200

def delete_atualizacao_service(atualizacao_id):
    deleted = Atualizacao.delete_atualizacao(atualizacao_id)
    
    if deleted.deleted_count > 0:
        return {"message": "Atualização deletada com sucesso"}, 200
    else:
        return {"error": "Atualização não encontrada"}, 404

