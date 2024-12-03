from models.peixe import Peixe
from schemas.peixe_schema import PeixeSchema
from marshmallow import ValidationError

peixe_schema = PeixeSchema()

def create_peixe_service(nome, idade, especie, peso, quantidade):
    peixe_data = {
        "nome": nome,
        "idade": idade,
        "especie": especie,
        "peso": peso,
        "quantidade": quantidade
    }

    try:
        validated_data = peixe_schema.load(peixe_data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = Peixe.create_peixe(validated_data)
    return {"peixe_id": str(result.inserted_id)}, 201

def get_peixe_service(peixe_id):

    peixe = Peixe.get_peixe(peixe_id)
    
    if not peixe:
        return {"error": "Peixe not found"}, 404
    
    
def get_peixe_service_name(name):
    try:
        peixe = Peixe.get_peixe_name(name)
        
        if not peixe:
            return {"error": "Fish not found"}, 404
        
        return peixe_schema.dump(peixe), 200
    except Exception as e:
        return {"error": f"Erro ao buscar peixe: {str(e)}"}, 500
    

    return peixe_schema.dump(peixe), 200

def get_all_peixes_service():

    peixes = Peixe.get_all_peixes()
    

    return peixe_schema.dump(peixes, many=True), 200

def update_peixe_service(peixe_id, update_data):

    try:
        validated_data = peixe_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400


    updated = Peixe.update_peixe(peixe_id, validated_data)
    
    if updated.matched_count == 0:
        return {"error": "Peixe not found"}, 404
    
    return {"message": "Peixe updated successfully"}, 200

def delete_peixe_service(peixe_id):
    deleted = Peixe.delete_peixe(peixe_id)
    
    if deleted.deleted_count > 0:
        return {"message": "Peixe Deletado com Sucesso"}, 200
    else:
        return {"error": "Peixe não encontrado"}, 404