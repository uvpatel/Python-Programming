import sounddevice
from scipy.io.wavfile import write
fs = 44100 # sample_rate
second = int(input("Enter the time duration in Second: "))
print("Recording....\n")
record_Voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_Voice)
print("Finished..\nPlease check it...")