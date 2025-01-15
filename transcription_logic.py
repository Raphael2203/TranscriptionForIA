from pytubefix import YouTube
import ffmpeg
import speech_recognition as sr

#Baixar o vídeo e extrair o áudio
def baixar_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    output_file = video.download(filename='audio.mp4')
    return output_file

#Converter áudio para formato adequado
def converter_audio(input_file):
    output_file = 'audio.wav'
    ffmpeg.input(input_file).output(output_file).overwrite_output().run()
    return output_file

#Transcrever áudio com SpeechRecognition
def transcrever_audio(file_patch):
     rec = sr.Recognizer()
     with sr.AudioFile(file_patch) as source:
         audio_data = rec.record(source)
         text = rec.recognize_google(audio_data, language='pt-BR')
         return text

