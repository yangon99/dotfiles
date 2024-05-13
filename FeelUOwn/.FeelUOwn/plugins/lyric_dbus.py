import logging
from dbus import SessionBus
from feeluown.consts import SONG_DIR as DEFAULT_DOWNLOAD_DIR
from feeluown.fuoexec.signal_manager import signal_mgr

"""
监听 app.live_lyric.sentence_changed 事件，并使用 app 的 dbus 服务发送dbus信息
"""


__alias__ = "歌词Dbus"
__desc__ = __doc__
__version__ = "0.1"


logger = logging.getLogger(__name__)
diy_bar = None


def send_dbus_msg(curr_sentence):
    global diy_bar
    logger.info('send dbus message: {}'.format(curr_sentence))
    if not diy_bar:
        logger.warning('try to get diy_bar object.')
        diy_bar = SessionBus().get_object('org.kde.plasma.doityourselfbar', '/id_1').get_dbus_method('pass')
        return
    if curr_sentence is not None and curr_sentence != "":
        diy_bar('|A|%s|||' % (curr_sentence))
    else:
        diy_bar('| A | …… |||')


def enable(app):
    app.live_lyric.sentence_changed.connect(send_dbus_msg)


def disable(app):
    signal_mgr.remove('app.live_lyric.sentence_changed', send_dbus_msg, False)