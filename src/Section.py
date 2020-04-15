#!/usr/bin/python
#-*- coding: utf-8 -*-

from src.OpenFigure import OpenFigure


class Section(OpenFigure):

    def render(self, qp):
        qp.setPen(self.pen)
        qp.drawLine(self.start_point, self.end_point)

    def move(self, shift):
        self.start_point += shift
        self.end_point += shift
