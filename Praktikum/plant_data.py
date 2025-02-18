from PySide6.QtWidgets import QFormLayout, QSpinBox, QDoubleSpinBox, QWidget


class PlantData(QWidget):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        self.plants_input = QSpinBox()
        self.plants_input.setRange(0, 20)
        self.plants_input.setFixedSize(100, 30)
        layout.addRow("Plants", self.plants_input)

        self.blossoms_input = QSpinBox()
        self.blossoms_input.setRange(0, 1000)
        self.blossoms_input.setFixedSize(100, 30)
        layout.addRow("Blossoms", self.blossoms_input)

        self.min_height_input = QDoubleSpinBox()
        self.min_height_input.setRange(0.00, 1000.00)
        self.min_height_input.setFixedSize(100, 30)
        layout.addRow("Min Height (cm)", self.min_height_input)

        self.max_height_input = QDoubleSpinBox()
        self.max_height_input.setRange(0.00, 1000.00)
        self.max_height_input.setFixedSize(100, 30)
        layout.addRow("Max Height (cm)", self.max_height_input)

        self.med_height_input = QDoubleSpinBox()
        self.med_height_input.setRange(0.00, 1000.00)
        self.med_height_input.setFixedSize(200, 30)
        layout.addRow("Median Height (cm)", self.med_height_input)

        self.setLayout(layout)
