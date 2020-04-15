from helpers.constants import ButtonsLabels, PaintMode, FigureLabels
from src import (
    Circle,
    Ellipse,
    Line,
    Polyline,
    Ray,
    Section,
    Regular,
    Irregular
)

PAINT_MODE_MAPPING = {
    ButtonsLabels.draw: PaintMode.draw,
    ButtonsLabels.move: PaintMode.move,
}


FIGURE_LABEL_MAPPINGS = {
    FigureLabels.circle_label: Circle,
    FigureLabels.ellipse_label: Ellipse,
    FigureLabels.line_label: Line,
    FigureLabels.polyline_label: Polyline,
    FigureLabels.ray_label: Ray,
    FigureLabels.section_label: Section,
    FigureLabels.regular_shape_label: Regular,
    FigureLabels.irregular_shape_label: Irregular,
    FigureLabels.triangle_label: Irregular,
    FigureLabels.rhombus_label: Irregular,
    FigureLabels.rectangle_label: Irregular,
}


SEVERAL_POINTS_FIGURES_LABEL = [
    FigureLabels.irregular_shape_label,
    FigureLabels.polyline_label,
    FigureLabels.regular_shape_label,
]
