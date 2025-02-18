from PySide6.QtWidgets import QFormLayout, QDoubleSpinBox, QWidget, QCheckBox


class EnvironmentData(QWidget):
    def __init__(self):
        super().__init__()

        layout = QFormLayout()

        self.temperature_input = QDoubleSpinBox()
        self.temperature_input.setRange(4.00, 40.00)
        self.temperature_input.setFixedSize(100, 30)
        layout.addRow("Temperature (°C)", self.temperature_input)

        self.equipment_fault_checkbox = QCheckBox("Equipment Fault")
        layout.addRow(self.equipment_fault_checkbox)

        self.setLayout(layout)
