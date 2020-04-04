#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from src.ClosedFigure import ClosedFigure


class Shape(ClosedFigure, ABC):
    def __init__(
            self,
            center_point=None,
            border_color=None,
            inner_color=None,
            border_points=None,
    ):
        super().__init__(
            center_point=center_point,
            border_points=border_points,
            border_color=border_color,
            inner_color=inner_color
        )
        self._amount_of_points = len(border_points) if border_points else 0

    amount_of_points = property()

    @amount_of_points.getter
    def amount_of_points(self):
        return self._amount_of_points

    @amount_of_points.setter
    def amount_of_points(self):
        return self._amount_of_points
