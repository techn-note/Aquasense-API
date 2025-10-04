from models.peixe import Peixe
from schemas.peixe_schema import PeixeSchema
from marshmallow import ValidationError

peixe_schema = PeixeSchema()

def create_peixe_service(nome, idade, especie, peso, quantidade, user_id):
    peixe_data = {
        "nome": nome,
        "idade": idade,
        "especie": especie,
        "peso": peso,
        "quantidade": quantidade,
        "user_id": user_id
    }

    try:
        validated_data = peixe_schema.load(peixe_data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = Peixe.create_peixe(validated_data)
    return {"peixe_id": str(result.inserted_id)}, 201


def get_peixe_service(peixe_id, user_id):
    peixe = Peixe.get_peixe(peixe_id, user_id=user_id)
    
    if not peixe:
        return {"error": "Peixe não encontrado"}, 404
    
    return peixe_schema.dump(peixe), 200


def get_peixe_service_name(name, user_id):
    try:
        peixe = Peixe.get_peixe_name(name, user_id=user_id)

        if not peixe:
            return {"error": "Peixe não encontrado"}, 404
        
        peixe_data = peixe_schema.dump(peixe)
        peixe_data['_id'] = str(peixe.get('_id'))
        
        return peixe_data, 200
    except Exception as e:
        return {"error": f"Erro ao buscar peixe: {str(e)}"}, 500


def get_all_peixes_service(user_id):
    peixes = Peixe.get_all_peixes(user_id=user_id)
    return peixe_schema.dump(peixes, many=True), 200


def update_peixe_service(peixe_id, update_data, user_id):
    try:
        validated_data = peixe_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Peixe.update_peixe(peixe_id, validated_data, user_id=user_id)
    
    if updated.matched_count == 0:
        return {"error": "Peixe não encontrado"}, 404
    
    return {"message": "Peixe atualizado com sucesso"}, 200


def delete_peixe_service(peixe_id, user_id):
    deleted = Peixe.delete_peixe(peixe_id, user_id=user_id)
    
    if deleted.deleted_count > 0:
        return {"message": "Peixe deletado com sucesso"}, 200
    else:
        return {"error": "Peixe não encontrado"}, 404
