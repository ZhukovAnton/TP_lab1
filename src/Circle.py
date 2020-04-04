#!/usr/bin/python
#-*- coding: utf-8 -*-
from helpers.geometry import get_distance
from src.ClosedFigure import ClosedFigure


class Circle(ClosedFigure):
    def __init__(self, border_color, inner_color, center_point, border_points):
        super().__init__(
            center_point=center_point,
            border_color=border_color,
            inner_color=inner_color,
            border_points=border_points,
        )

    def render(self, qp):
        qp.setPen(self.pen)
        qp.setBrush(self.inner_color)
        radius = get_distance(self.center_point, self.border_points[0])
        qp.drawEllipse(self.center_point, radius, radius)
