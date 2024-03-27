from gtts import gTTS
from openai import OpenAI
from Key import Api_key

key = Api_key()
client = OpenAI(api_key= key.key)

data = './tss_assistent/output.mp3'

tts = gTTS(text="안녕하세요",lang='ko')
tts.save(f"{data}")
audio_file = open(f"{data}","rb")
transcript = client.audio.transcriptions.create(model="whisper-1",file = audio_file)

print(transcript.text)


