from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class DefaultMainWindowParams:
    title = "Paint Application"
    left_indent = 600
    top_indent = 200
    width = 1000
    height = 700


class DefaultSideBarParams:
    bg_color = QColor('lightgray')
    width = 200
    height = None


class DefaultColorButtonParams:
    width = 200
    height = None


class DefaultDrawParams:
    pen_color = Qt.black
    inner_color = Qt.white
    thickness = 3
