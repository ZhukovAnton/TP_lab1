#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from PyQt5.QtGui import QPen

from helpers.constants import DefaultDrawParams


class Figure(ABC):
    """Base abstract figure class"""
    def __init__(
            self,
            center_point=None,
            border_color=DefaultDrawParams.pen_color
    ):
        self._center_point = center_point
        self._border_color = border_color

    center_point = property()
    border_color = property()

    @center_point.getter
    def center_point(self):
        return self._center_point

    @center_point.setter
    def center_point(self, value):
        self._center_point = value

    @border_color.getter
    def border_color(self):
        return self._border_color

    @border_color.setter
    def border_color(self, value):
        self._border_color = value

    @property
    def pen(self):
        """create and return default pen"""
        pen = QPen()
        pen.setStyle(DefaultDrawParams.pen_style)
        pen.setWidth(DefaultDrawParams.pen_thickness)
        pen.setBrush(self.border_color)
        pen.setCapStyle(DefaultDrawParams.pen_cap_style)
        pen.setJoinStyle(DefaultDrawParams.pen_join_style)
        return pen

    @abstractmethod
    def move(self, shift):
        pass
