# audio_strobe
A simple Python script that can make smart lights flicker to the rythm of music playing on your Windows-PC.

If you have a way to control your lights from your PC, then this script will do the rest for you.

# Setup
## Controlling your Lights
**You will already need to have a way to control your lights from your PC.**

In my case the lights are controlled by a RaspberryPi that turns the lights on/off if I open a specific website that it is hosting.
However, **this step will vary heavily for you.**
You will need one function that - when called - turns the lights on and one function that turns them off. If possible, these functions should be executed in parallel to the script.

Once you found a way, edit `main.py` and replace the function `on()` by your means of turning the lights on and respectively the same for the function `off`().

This is how it looks for me:
```
...
import os

def on():
    os.system('cmd /Q /C curl http://192.168.0.105/on')
	
def off():
    os.system('cmd /Q /C curl http://192.168.0.105/off')
...
```

Note that I execute the commands in a new command window instead of executing `curl` directly. This is done so they do not block the script at runtime.

The hardest part is done!

## Dependencies
This script depends on the library **sounddevice**. Use `pip install sounddevice` to install it.

## Quick Test
If you run the script at this point, your lights should already react to the audio of your default microphone.

In the following, I will go show how you can use your system audio instead of a microphone input.

# Using System Audio
Since there is no easy way to directly grab system audio under Windows, you will need some third-party software to get it working.
## Virtual Cable
VB-Cable Virtual Cable is a free piece of software that creates a virtual audio cable on your PC.
Basically, Windows will show you a new "Speaker" called CABLE-Input. Any audio that is played on this device will instead be forwarded to a virtual microphone called CABLE-Output.

Download Virtual-Cable from [VB-Audios Website](https://www.vb-audio.com/Cable/index.htm) and follow their instructions on how to install it.

Next, edit `main.py` by uncommenting line 11 and chosing CABLE-Output as the default device. You can find out the ID of CABLE-Output by typing `python -m sounddevice` into the command prompt.
If you now select CABLE-Input as your playback device in Windows and play some music, your light should flicker as expected.

However you won't hear the music at this point, because - by default - Windows can only play audio on a single device at a time. Follow the next paragraph to fix that.

## Audio Router
Audio Router is another free program that allows you to route your system audio more liberally than Windows allows you to.
Most importantly for this project, you can configure your audio to be played on multiple devices at once.

Download Audio Router from [their github repository](https://github.com/audiorouterdev/audio-router/releases) and install it. Before you open it, change your default playback device to your physical speakers in the Windows audio settings.

Open Audio Router and find the program that you will use to play the music. Click the small arrow underneath it, click `Duplicate` and select CABLE-Input.

Done!

The music played by that program should now both be audible and recognized by the script.




