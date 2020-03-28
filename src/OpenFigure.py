#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC

from src.Figure import Figure


class OpenFigure(ABC, Figure):
    def __init__(self, start_point=0, end_point=0):
        self._start_point = start_point
        self._end_point = end_point

    start_point = property()
    end_point = property()

    @end_point.getter
    def end_point(self):
        return self._end_point

    @end_point.setter
    def inner_color(self, value):
        self._end_point = value

    @start_point.getter
    def start_point(self):
        return self._start_point

    @start_point.setter
    def border_points(self, value):
        self._start_point = value
