#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC

from src.Figure import Figure
from ui.constants import DefaultDrawParams


class ClosedFigure(ABC, Figure):
    def __init__(
            self,
            inner_color=DefaultDrawParams.inner_color,
            border_points=None
    ):
        self._inner_color = inner_color
        if border_points is None:
            self._border_points = []

    inner_color = property()
    border_points = property()

    @inner_color.getter
    def inner_color(self):
        return self._inner_color

    @inner_color.setter
    def inner_color(self, value):
        self._inner_color = value

    @border_points.getter
    def border_points(self):
        return self._border_points

    @border_points.setter
    def border_points(self, value):
        self._border_points = value
