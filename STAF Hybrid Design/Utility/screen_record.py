from subprocess import Popen
from subprocess import call

cmd = 'ffmpeg -y -rtbufsize 2000M -f dshow  -i video="screen-capture-recorder" -s 1920x1080 -b:v 512k -r 20 -vcodec libx264 test.avi'

def terminate(process):
    if process.poll() is None:
        call('taskkill /F /T /PID ' + str(process.pid))

videoRecording = Popen(cmd) # start recording

terminate(videoRecording)