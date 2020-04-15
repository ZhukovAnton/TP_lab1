#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC

from src.Figure import Figure
from helpers.constants import DefaultDrawParams


class ClosedFigure(Figure, ABC):
    """
    Base abstract class for all closed figures.
    Closed figures has inner space and inner color
    """
    def __init__(
            self, center_point, border_color,
            inner_color=DefaultDrawParams.inner_color,
            border_points=None,
    ):
        super().__init__(center_point, border_color)
        self._inner_color = inner_color
        self._border_points = border_points if border_points else []

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

    def move(self, shift):
        self.center_point += shift
        for point in self.border_points:
            point += shift
