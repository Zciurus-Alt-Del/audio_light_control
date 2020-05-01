# There is LICENSE and a README file available in the repository on github (https://github.com/Zciurus-Alt-Del/audio_light_control/)
# Both should be taken note of before running this script
import sounddevice as sd
import numpy



# Uncomment this option to use a specific microphone rather than your default device
# (list your audiodevices with `python3 -m sounddevice`)
#sd.default.device[0] = 2


treshold = 30

# Replace these functions by your means of controlling your lights
def on():
    pass


def off():
    pass


previous_level = 0
def read_volume(data_in, data_out, frames, t, stat):
    global previous_level
    level = numpy.linalg.norm(data_in)*10
    print('\t', level, '\t', "|" * int(level))

    # Modify this if-statement to adjust the trigger
    if level - previous_level > treshold:
        on()
    else:
        off()

    previous_level = level


if __name__ == "__main__":
    while True:
        with sd.Stream(callback=read_volume):
            sd.sleep(10000)
