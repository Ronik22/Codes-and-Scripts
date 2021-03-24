# Records audio until user presses Ctrl+c and then saves the audio

import tempfile
import queue
import sys
import sounddevice as sd
import soundfile as sf
import numpy  
assert numpy  

q = queue.Queue()

samplerate = None
device = None
filename = None
channels = 1
subtype = None

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())


try:
    if samplerate is None:
        device_info = sd.query_devices(device, 'input')
        samplerate = int(device_info['default_samplerate'])
    if filename is None:
        filename = tempfile.mktemp(prefix='recorded_audio_', suffix='.wav', dir='')

    with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=channels, subtype=subtype) as file:
        with sd.InputStream(samplerate=samplerate, device=device, channels=channels, callback=callback):
            print('Recording started\nPress Ctrl+C to stop the recording')
            while True:
                file.write(q.get())
                
except KeyboardInterrupt:
    print('\nRecording finished: ' + repr(filename))
