import json
import boto3
from datetime import datetime #para salvar diversos arquivos na mesma pasta (nome-sobrenome)
import httpx
import asyncio
from urllib.parse import quote

s3 = boto3.client('s3')

def lambda_handler(event, context):
    intent_name = event["sessionState"]["intent"]["name"]
    textoFinal = 'oi'

    if(intent_name == 'RegisterJobIntent'):
        # Acessando os slots do evento
        slots = event['interpretations'][0]['intent']['slots']
        
        primeiroNome = slots['primeiroNome']['value']['interpretedValue']
        sobrenome = slots['sobrenome']['value']['interpretedValue']
        vaga = slots['vaga']['value']['interpretedValue']
        celular = slots['celular']['value']['interpretedValue']
        email = slots['email']['value']['interpretedValue']
        cidade = slots['cidade']['value']['interpretedValue']
    
        bucketName = 'projeto6-7'
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
        key = f'{primeiroNome}-{sobrenome}/{timestamp}-dados.json' #pode ser .txt
        
        # Configurar parâmetros para o objeto no S3
        params = {
            'Bucket': bucketName,
            'Key': key,
            'Body': json.dumps({
                'vaga': vaga,
                'primeiroNome': primeiroNome,
                'sobrenome': sobrenome,
                'celular': celular,
                'email': email,
                'cidade': cidade
            }),
            'ContentType': 'application/json'
        }
    
        try:
            # Colocar objeto no S3
            response = s3.put_object(**params)
            print(f'Dados armazenados com sucesso no S3: {response}')
            
            textoFinal = f'Muito obrigado pela sua inscrição, {primeiroNome}! Desejo boa sorte na sua candidatura!'
        except Exception as e:
            print(f'Erro ao armazenar dados no S3: {e}')
            
            
    if(intent_name == 'CheckIntent'):
        # Acessando os slots do evento
        slots = event['interpretations'][0]['intent']['slots']
        
        primeiroNome = slots['primeiroNome']['value']['interpretedValue']
        sobrenome = slots['sobrenome']['value']['interpretedValue']
        
        bucketName = 'projeto6-7'
        prefix = f'{primeiroNome}-{sobrenome}/'
        
        try:
            # Listar objetos no S3 com base no prefixo
            response = s3.list_objects_v2(Bucket=bucketName, Prefix=prefix)
            
            # Verificar se há objetos encontrados
            if 'Contents' in response:
                data = []
                for obj in response['Contents']:
                    key = obj['Key']
                    # Obter o objeto do S3 com base na chave encontrada
                    obj_response = s3.get_object(Bucket=bucketName, Key=key)
                    obj_data = obj_response['Body'].read().decode('utf-8')
                    json_data = json.loads(obj_data)
                    data.append(json_data)
                
                print(f'Dados recuperados do S3: {data}')
                
                vacancy = f"Olá {data[0]['primeiroNome']}, você se cadastrou nas vagas: \n"      

                for _data in data:
                    vacancy = vacancy + _data['vaga'] + "; \n"

                textoFinal = vacancy
                
            else:
                print(f'Nenhum objeto encontrado no S3 com prefixo {prefix}')
                
        except Exception as e:
            print(f'Erro ao obter objetos do S3: {e}')
            
            
    if(intent_name == 'ConvertToAudioIntent'):
        print(event)
        message = event['inputTranscript']
        
        texto_formatado = message.strip().lower()
        texto_formatado = texto_formatado.replace(' ', '-')
        texto_codificado = quote(texto_formatado)
        
        api_url = f"https://s9uqg4t7c9.execute-api.us-east-1.amazonaws.com/api-tts-dev-post?phrase={texto_codificado}"

        api_response = asyncio.run(consumindo_api(api_url))
        textoFinal = api_response['url_to_audio']


    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name,
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": textoFinal
            }
        ]
    }
        
    return response
    

async def consumindo_api(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()