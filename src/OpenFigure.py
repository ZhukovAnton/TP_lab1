#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC

from helpers.geometry import midpoint
from src.Figure import Figure


class OpenFigure(Figure, ABC):
    """
    Base abstract class for the open figures.
    There are no inner area or inner color.
    We have only two points to determine figure position.
    """
    def __init__(self, border_color=None, start_point=0, end_point=0):
        # NOTE: we should also recalculate center_point
        # every time we update start point or end point
        center_point = midpoint(start_point, end_point)
        super().__init__(center_point, border_color)

        self._start_point = start_point
        self._end_point = end_point

    start_point = property()
    end_point = property()

    @end_point.getter
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        self._end_point = value
        self.center_point = midpoint(
            self._start_point, self._end_point
        )

    @start_point.getter
    def start_point(self):
        return self._start_point

    @start_point.setter
    def start_point(self, value):
        self._start_point = value
        self.center_point = midpoint(
            self._start_point, self._end_point
        )

