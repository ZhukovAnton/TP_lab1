#!/usr/bin/python
#-*- coding: utf-8 -*-
from helpers.geometry import get_distance
from src.Circle import Circle


class Ellipse(Circle):

    def render(self, qp):
        qp.setPen(self.pen)
        qp.setBrush(self.inner_color)
        radius_x = get_distance(self.center_point, self.border_points[0])
        radius_y = get_distance(self.center_point, self.border_points[1])
        qp.drawEllipse(self.center_point, radius_x, radius_y)
