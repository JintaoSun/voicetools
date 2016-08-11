# coding: utf-8
import os
import sys
import wave
import pyaudio
from io import BytesIO
HOME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(HOME)

from raspi_assistant.utils import init_logging_handler
from raspi_assistant.handler import BaseHandler, ActionHandler
from tempfile import TemporaryFile


def main():
    logger = init_logging_handler()
    handler = BaseHandler('24.08be72600a465c9ea5a03bbb1615fbb2.2592000.1473492202.282335-8403190')
    func, result = handler.process(['给我讲个笑话', ])
    print func, result
    content = handler.execute(func, result)
    handler.feedback(content)

    # handler.feedback('你是谁啊你是谁')
    # handler.audio_handler.play('test_tts.wav')
    # audio_handler = AudioHandler()
    # audio_handler.record(3, f)

    # with open('test_record.wav', 'wb') as ff:
    #     print f.read()
    #     ff.write(f.read())

    # with open('test_tts.wav', 'rb') as f:
    #     audio = BytesIO(f.read())
    # handler.audio_handler.play(audio)

    # p = vlc.MediaPlayer("file:///path/to/track.mp3")


if __name__ == '__main__':
    main()
