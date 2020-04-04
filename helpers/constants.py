from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


PAINT_ERROR_MSG = "Ooops, something is wrong with our paint app. We are fixing this error now ;)"
COMMON_ERROR_MSG = "Unexpected error. Even we don't know what has happened. Try again)"


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
    pen_style = Qt.SolidLine
    pen_cap_style = Qt.RoundCap
    pen_join_style = Qt.RoundJoin
    pen_thickness = 3
    inner_color = Qt.white
