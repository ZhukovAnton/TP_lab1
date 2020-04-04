#!/usr/bin/python
#-*- coding: utf-8 -*-
from math import cos, sin, pi, atan

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon

from helpers.geometry import get_distance
from src.Shape import Shape


class Regular(Shape):
    def __init__(
            self, border_points, num,
            center_point=None, border_color=None, inner_color=None
    ):
        super().__init__(
            center_point=center_point,
            border_color=border_color,
            inner_color=inner_color,
            border_points=border_points,
        )
        self._prepare_points(num)

    def _prepare_points(self, num):
        a = self.center_point
        r = get_distance(self.border_points[0], self.center_point)
        alpha = atan(
            (self.border_points[0].y() - self.center_point.y())/(self.border_points[0].x() - self.center_point.x())
        )
        for i in range(1, num):
            x = r*cos(2.0*pi*i/num + alpha) + self.center_point.x()
            y = r*sin(2.0*pi*i/num + alpha) + self.center_point.y()
            self.border_points.append(QPoint(x, y))

    def render(self, qp):
        qp.setPen(self.pen)
        qp.setBrush(self.inner_color)
        qp.drawPolygon(QPolygon(self.border_points))
