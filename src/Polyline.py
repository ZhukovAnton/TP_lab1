#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.Section import Section


class Polyline(Section):
    def __init__(self, border_color, inner_points):
        super().__init__(
            border_color=border_color,
            start_point=inner_points[0],
            end_point=inner_points[-1]
        )
        self._inner_points = inner_points

    inner_points = property()

    @inner_points.getter
    def inner_points(self):
        return self._inner_points

    @inner_points.setter
    def inner_points(self, value):
        # NOTE: update start and end point
        self.start_point = value[0],
        self.end_point = value[-1]
        self._inner_points = value

    def render(self, qp):
        qp.setPen(self.pen)
        qp.drawPolyline(*self.inner_points)

