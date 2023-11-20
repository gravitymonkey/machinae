import pyaudio
import numpy as np
import aubio

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=pyaudio.paFloat32,
                channels=1,  # mono
                rate=44100,  # sample rate
                input=True,
                frames_per_buffer=1024)

# Aubio's pitch detection
pDetection = aubio.pitch("default", 2048, 1024, 44100)
pDetection.set_unit("midi")
pDetection.set_silence(-80)

while True:
    try:
        data = stream.read(1024)
        samples = np.fromstring(data, dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        # Do something with the pitch
        print("Current pitch:", pitch)
    except KeyboardInterrupt:
        break

# Close the stream
stream.stop_stream()
stream.close()
p.terminate()

