from collections import namedtuple

from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QRadioButton, QVBoxLayout, QLabel, QWidget, QColorDialog, QFileDialog, \
    QButtonGroup, QInputDialog

from helpers.constants import (
    DefaultSideBarParams as SideBarParams,
    DefaultColorButtonParams,
)
from helpers.mappings import FIGURE_LABEL_MAPPINGS, SEVERAL_POINTS_FIGURES_LABEL, FigureLabels

DialogParams = namedtuple(
    'DialogParams',
    [
        'min_points_num',
        'dialog_point_step'
    ]
)


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent        # MainWindow instance
        self.parent.active = None   # active figure
        self.set_bg_color()

        self.figures_radio_buttons = []
        self.num_btn = QPushButton('Set num', self)
        self.reset_btn = QPushButton('Reset', self)
        self.border_color_btn = QColorButton('Choose border color')
        self.bg_color_btn = QColorButton('Choose background color')
        self.save_btn = QPushButton("Save", self)
        self.button_group = QButtonGroup()

        self.render_buttons()

    @pyqtSlot()
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(
            parent=self,
            caption="Save Image",
            filter="PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) "
        )

        if file_path == "":
            return
        self.image.save(file_path)

    def render_buttons(self):
        layout = QVBoxLayout()
        layout.addStretch(0)

        layout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save)

        layout.addWidget(self.reset_btn)
        self.reset_btn.clicked.connect(lambda: self.parent.draw_area.reset())

        layout.addWidget(self.num_btn)
        self.num_btn.clicked.connect(lambda: self.show_dialog(self.parent.active))

        layout.addWidget(QLabel('Border color:', self))
        layout.addWidget(self.border_color_btn)

        layout.addWidget(QLabel('Bg color:', self))
        layout.addWidget(self.bg_color_btn)

        layout.addWidget(QLabel('Figure:', self))

        # render buttons to choose a figure
        self.figures_radio_buttons = [
            QRadioButton(figure_label)
            for figure_label in FIGURE_LABEL_MAPPINGS.keys()
        ]

        for button in self.figures_radio_buttons:
            layout.addWidget(button)

        for button in self.figures_radio_buttons:
            self.button_group.addButton(button)

        # set processing function
        self.button_group.buttonClicked[int].connect(self.on_button_clicked)

        # set first active figure as default
        self.figures_radio_buttons[0].setChecked(True)
        self.parent.active = self.figures_radio_buttons[0].text()
        self.parent.num = 3

        self.setLayout(layout)

    def on_button_clicked(self, button_id):
        for button in self.button_group.buttons():
            if button is self.button_group.button(button_id):
                self.show_dialog(button.text())
                self.parent.active = button.text()

    def set_bg_color(self):
        color = SideBarParams.bg_color
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.setAutoFillBackground(True)

    def show_dialog(self, active_name):
        dialog_params = DialogParams(3, 1)

        if active_name in SEVERAL_POINTS_FIGURES_LABEL:
            num, _ = QInputDialog.getInt(
                self,
                'points dialog',
                'enter a number of points',
                min=dialog_params.min_points_num,
                step=dialog_params.dialog_point_step,
                value=dialog_params.min_points_num,
            )
            self.parent.num = num


class QColorButton(QPushButton):
    '''
    Custom Qt Widget to show a chosen color.
    Left-clicking the button shows the color-chooser, while
    right-clicking resets the color to None (no-color).
    '''

    colorChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        self._color = None
        self.setMaximumWidth(DefaultColorButtonParams.width)
        self.pressed.connect(self.on_color_picker)

    def set_color(self, color):
        if color != self._color:
            self._color = color
            self.colorChanged.emit()

        if self._color:
            self.setStyleSheet("background-color: %s;"%self._color)
        else:
            self.setStyleSheet("")

    def color(self):
        return QColor(self._color)

    def on_color_picker(self):
        '''
        Show color-picker dialog to select color.
        Qt will use the native dialog by default.
        '''
        dlg = QColorDialog(self)
        if self._color:
            dlg.setCurrentColor(QColor(self._color))

        if dlg.exec_():
            self.set_color(dlg.currentColor().name())

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.set_color(None)

        return super(QColorButton, self).mousePressEvent(e)