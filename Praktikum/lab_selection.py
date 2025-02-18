from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QRadioButton


class LabSelection(QGroupBox):
    def __init__(self):
        super().__init__("Lab")
        layout = QHBoxLayout()

        self.lab_a = QRadioButton("A")
        self.lab_b = QRadioButton("B")
        self.lab_c = QRadioButton("C")

        layout.addWidget(self.lab_a)
        layout.addWidget(self.lab_b)
        layout.addWidget(self.lab_c)

        self.setLayout(layout)

    def get_selected_lab(self):
        if self.lab_a.isChecked():
            return "A"
        elif self.lab_b.isChecked():
            return "B"
        elif self.lab_c.isChecked():
            return "C"
        return "None"

    def reset(self):
        self.lab_a.setChecked(False)
        self.lab_b.setChecked(False)
        self.lab_c.setChecked(False)
