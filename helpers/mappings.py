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


class FigureLabels:
    circle_label = 'circle'
    ellipse_label = 'ellipse'
    line_label = 'line'
    polyline_label = 'polyline line'
    ray_label = 'ray'
    section_label = 'section'
    regular_shape_label = 'regular shape'
    irregular_shape_label = 'irregular shape'


FIGURE_LABEL_MAPPINGS = {
    FigureLabels.circle_label: Circle,
    FigureLabels.ellipse_label: Ellipse,
    FigureLabels.line_label: Line,
    FigureLabels.polyline_label: Polyline,
    FigureLabels.ray_label: Ray,
    FigureLabels.section_label: Section,
    FigureLabels.regular_shape_label: Regular,
    FigureLabels.irregular_shape_label: Irregular,
}


SEVERAL_POINTS_FIGURES_LABEL = [
    FigureLabels.irregular_shape_label,
    FigureLabels.polyline_label,
    FigureLabels.regular_shape_label,
]