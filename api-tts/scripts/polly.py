import boto3
import os

def generate_audio(phrase, phrase_id):
    polly_client = boto3.client('polly')
    s3_client = boto3.client('s3')
    
    s3_bucket_name = os.environ['S3BUCKETNAME']

    audio_file_name = f"{phrase_id}.mp3"
    
    #Gera áudio
    try:
        response = polly_client.synthesize_speech(Engine='standard', Text=phrase, OutputFormat='mp3', VoiceId='Camila')
    except Exception as e:
        print(f"Error synthesizing speech: {e}")
        raise e

    #Salva
    try:
        with open('/tmp/speech.mp3', 'wb') as file:
            file.write(response['AudioStream'].read())
        print("Audio file written to /tmp/speech.mp3")
    except Exception as e:
        print(f"Error writing audio file: {e}")
        raise e

    #Envia para S3
    try:
        s3_client.upload_file('/tmp/speech.mp3', s3_bucket_name, audio_file_name)
        print(f"Audio file uploaded to S3 bucket: {s3_bucket_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        raise e

    s3_audio_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{audio_file_name}"

    return s3_audio_url
