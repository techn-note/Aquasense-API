from datetime import datetime
from schemas.atualizacao_schema import AtualizacaoSchema
from services.sensores_service import get_latest_sensor_data_service
from models.atualizacao import Atualizacao
from marshmallow import ValidationError

atualizacao_schema = AtualizacaoSchema()

PARAMETROS_LIMITE = {
    "Temperatura": {"min": 18.0, "max": 24.0},
    "Ph": {"min": 6.8, "max": 7.2},
    "Volume": {"min": 10.0, "max": 100.0},
    "Oxigenacao": {"min": 5.0, "max": 10.0}
}

def create_atualizacao_service(tanque):
    alertas = []
    tipo_mensagem = "Padrao"

    for tipo, limites in PARAMETROS_LIMITE.items():
        response, status_code = get_latest_sensor_data_service(tipo, tanque)

        if status_code == 404:
            continue

        if status_code == 200:
            valor = response["valor"]

            if valor < limites["min"]:
                alertas.append(f"{tipo} muito baixa!")
                tipo_mensagem = "Alerta"
                break
            elif valor > limites["max"]:
                alertas.append(f"{tipo} muito elevada!")
                tipo_mensagem = "Alerta"
                break


    if not alertas:
        if not any([get_latest_sensor_data_service(tipo, tanque)[1] == 200 for tipo in PARAMETROS_LIMITE]):

            mensagem = "Sem sensores para analisar"
        else:

            mensagem = "Tudo certo por aqui!"
        tipo_mensagem = "Padrao"
    else:
        mensagem = alertas[0]


    atualizacao_data = {
        "mensagem": mensagem,
        "data": datetime.now().isoformat(),
        "tipo": tipo_mensagem,
        "tanque": tanque
    }

    try:
        validated_data = atualizacao_schema.load(atualizacao_data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    result = Atualizacao.create_atualizacao(validated_data)
    return {"atualizacao_id": str(result.inserted_id), "mensagem": mensagem}, 201


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


def get_latest_atualizacao_service(tanque):
    atualizacao = Atualizacao.get_latest_atualizacao(tanque)
    
    if not atualizacao:
        return {"mensagem": "Nenhuma atualização disponível para este tanque."}, 200
    
    return atualizacao_schema.dump(atualizacao), 200
