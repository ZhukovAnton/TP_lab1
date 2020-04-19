#!/usr/bin/python
#-*- coding: utf-8 -*-
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPolygon

from src.Shape import Shape


class Irregular(Shape):

    def __init__(self, border_color, inner_color, border_points):
        super().__init__(
            center_point=self.__calculate_center(border_points),
            border_color=border_color,
            inner_color=inner_color,
            border_points=border_points,
        )

    @staticmethod
    def __calculate_center(border_points):
        result_point = QPoint(0, 0)
        for point in border_points:
            result_point += point
        return result_point/len(border_points)

    def render(self, qp):
        qp.setPen(self.pen)
        qp.setBrush(self.inner_color)
        qp.drawPolygon(QPolygon(self.border_points))

