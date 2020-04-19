#!/usr/bin/python
#-*- coding: utf-8 -*-
from helpers.geometry import get_line_point
from src.Ray import Ray


class Line(Ray):
    def __init__(self, start_point, end_point, border_color, border):
        super().__init__(
            start_point=get_line_point(start_point, end_point, x=0.001),
            end_point=end_point,
            border_color=border_color,
            border=border
        )

