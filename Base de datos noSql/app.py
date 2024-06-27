import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

tabla = dynamodb.Table('tabla-german-murillo')

# La clave debe ser pasada con 'Key' en mayúscula
response = tabla.get_item(Key={"id": "1"})

# Verifica si el item está en la respuesta
if 'Item' in response:
    #print(response['Item']['nombre'])
    print(response['Item'])
else:
    print("Item no encontrado")
    
response = tabla.scan()

print(response['Items'])


nuevo_elemento_1 = {
    'id': '3',
    'nombre': 'Carlos',
    'edad': 40,
    'ciudad': 'Bogotá'
}

# Insertar el nuevo objeto en la tabla
response_1 = tabla.put_item(Item=nuevo_elemento_1)

print("Inserción del elemento con id '3':")
# print(response_1)

actualizar = tabla.update_item(
    Key={'id': '2'},
    UpdateExpression='SET edad = :val1',
    ExpressionAttributeValues={
        ':val1': 35  # Nuevo valor para 'edad'
    },
    ReturnValues='UPDATED_NEW'
)

print("Actualización del elemento con id '2':")
# print(response_1)
