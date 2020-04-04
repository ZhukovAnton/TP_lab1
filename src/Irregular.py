#!/usr/bin/python
#-*- coding: utf-8 -*-
from PyQt5.QtGui import QPolygon

from src.Shape import Shape


class Irregular(Shape):

    def render(self, qp):
        qp.setPen(self.pen)
        qp.setBrush(self.inner_color)
        qp.drawPolygon(QPolygon(self.border_points))

