import logging
from dbus import SessionBus
from feeluown.consts import SONG_DIR as DEFAULT_DOWNLOAD_DIR
from feeluown.fuoexec.signal_manager import signal_mgr

"""
监听 app.live_lyric.lyrics_changed 事件，发送dbus信息
"""


__alias__ = "歌词Dbus"
__desc__ = __doc__
__version__ = "0.1"


logger = logging.getLogger(__name__)
diy_bar = None

def send_dbus_msg(new_line):
    logger.debug('get origin new_line: {}'.format(new_line.origin))
    global diy_bar
    if not diy_bar:
        logger.warning('try to get diy_bar object.')
        diy_bar = SessionBus().get_object('org.kde.plasma.doityourselfbar', '/id_1').get_dbus_method('pass')
    msg_str = ''

    if new_line.origin is not None and new_line.origin != "":
        msg_str = '|A|<font-size="%ipx">%s</font>|||' % (16 if new_line.has_trans else 18, new_line.origin)
    else:
        msg_str = '| A | …… |||'
    
    if new_line.has_trans:
        msg_str += '|B|<font-size="14px">%s</font>|||' % (new_line.trans)

    logger.debug('send dbus message: {}'.format(msg_str))
    diy_bar(msg_str)


def enable(app):
    app.live_lyric.line_changed.connect(send_dbus_msg)


def disable(app):
    app.live_lyric.line_changed.disconnect(send_dbus_msg)
