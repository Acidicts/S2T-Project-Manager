import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr
import pyaudio
import os


r = sr.Recognizer()


def record_audio(filename, duration, fs=44100):
    chunk = 1024
    form = pyaudio.paInt16
    channels = 2

    audio = pyaudio.PyAudio()
    stream = audio.open(format=form, channels=channels, rate=fs, input=True, frames_per_buffer=chunk)

    print("Recording...")
    frames = []
    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(form))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

    if os.path.exists('temp.wav'):
        os.remove('temp.wav')
    record_audio('temp.wav', 10)  # Record for 10 seconds

    # open the file
    with sr.AudioFile('temp.wav') as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text
