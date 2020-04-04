from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import *
from helpers.constants import COMMON_ERROR_MSG, PAINT_ERROR_MSG
from helpers.mappings import FigureLabels


class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setToolTip('This is a Draw Area!')
        self.reset()
        self.show()

    def reset(self):
        self.points = []
        self.figures = []
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        self.draw_figures(qp)
        qp.end()

    def draw_points(self, qp):
        pen = QPen(Qt.red)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(5)
        qp.setPen(pen)

        for point in self.points:
            qp.drawPoint(point)

    def draw_figures(self, qp):
        for fig in self.figures:
            fig.render(qp)

    def __is_enough_points(self, trigger_value):
        return len(self.points) == trigger_value

    def _section_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(2):
            figure = Section(
                border_color=kwargs.get('border_color'),
                start_point=self.points[0],
                end_point=self.points[1]
            )
        return figure

    def _ray_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(2):
            figure = Ray(
                border_color=kwargs.get('border_color'),
                start_point=self.points[0],
                end_point=self.points[1],
                border=self.geometry(),
            )
        return figure

    def _line_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(2):
            figure = Line(
                border_color=kwargs.get('border_color'),
                start_point=self.points[0],
                end_point=self.points[1],
                border=self.geometry(),
            )
        return figure

    def _circle_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(2):
            figure = Circle(
                border_color=kwargs.get('border_color'),
                inner_color=kwargs.get('inner_color'),
                center_point=self.points[0],
                border_points=[self.points[1]]
            )
        return figure

    def _ellipse_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(3):
            figure = Ellipse(
                border_color=kwargs.get('border_color'),
                inner_color=kwargs.get('inner_color'),
                center_point=self.points[0],
                border_points=[self.points[1], self.points[2]]
            )
        return figure

    def _polyline_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(self.parent.num):
            figure = Polyline(
                border_color=kwargs.get('border_color'),
                inner_points=self.points,
            )
        return figure

    def _irregular_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(self.parent.num):
            figure = Irregular(
                border_color=kwargs.get('border_color'),
                inner_color=kwargs.get('inner_color'),
                border_points=self.points,
            )
        return figure

    def _regular_processor(self, **kwargs):
        figure = None
        if self.__is_enough_points(2):
            figure = Regular(
                border_color=kwargs.get('border_color'),
                inner_color=kwargs.get('inner_color'),
                center_point=self.points[0],
                border_points=[self.points[1]],
                num=self.parent.num
            )
        return figure

    def _new_figure_event_processor(self):
        # remove all auxiliary points from the screen
        self.points = []
        # perform screen update
        self.update()

    @property
    def border_color(self):
        return self.parent.sidebar.border_color_btn.color()

    @property
    def inner_color(self):
        return self.parent.sidebar.bg_color_btn.color()

    def _mouse_press_event(self, event):
        figure_processor_mappings = {
            FigureLabels.section_label: self._section_processor,
            FigureLabels.line_label: self._line_processor,
            FigureLabels.ray_label: self._ray_processor,
            FigureLabels.polyline_label: self._polyline_processor,
            FigureLabels.regular_shape_label: self._regular_processor,
            FigureLabels.irregular_shape_label: self._irregular_processor,
            FigureLabels.circle_label: self._circle_processor,
            FigureLabels.ellipse_label: self._ellipse_processor,
        }

        # save new point
        self.points.append(event.pos())
        # display new point on the screen
        self.update()

        figure_processor = figure_processor_mappings.get(self.parent.active)

        if figure_processor is None:
            raise KeyError(PAINT_ERROR_MSG)

        try:
            figure = figure_processor(
                border_color=self.border_color,
                inner_color=self.inner_color,
            )
            if figure:
                self.figures.append(figure)
                # drawing is happening here
                self._new_figure_event_processor()
        except:
            raise Exception(COMMON_ERROR_MSG)

    def mousePressEvent(self, event):
        # entry point for all paint event
        try:
            self._mouse_press_event(event)
        except Exception as exc:
            self.points = []
            self._show_error_msg(exc)

    @staticmethod
    def _show_error_msg(exc):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Ooops!!!')
        msg.setInformativeText(f'{exc}')
        msg.exec_()
