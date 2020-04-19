#!/usr/bin/python
#-*- coding: utf-8 -*-
from helpers.geometry import get_line_point
from src.Section import Section


class Ray(Section):

    def __init__(self,  border_color, start_point, end_point, border):
        super().__init__(
            start_point=start_point,
            end_point=get_line_point(start_point, end_point, x=border.bottomRight().x()),
            border_color=border_color,
        )

