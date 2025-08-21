import sys
import os
import re
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PySide6.QtCore import Qt

print("Launching Regex Explorer…")


def regex_search(folder, pattern):
    try:
        regex = re.compile(pattern)
    except re.error as e:
        return [], f"Invalid regex: {e}"

    matches = []
    for root, _, files in os.walk(folder):
        for f in files:
            if regex.search(f):
                matches.append((f, os.path.join(root, f)))
    return matches, None


class RegexSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RegexExplorer - File Finder")
        self.setGeometry(200, 200, 700, 500)

        layout = QVBoxLayout()

        folder_layout = QHBoxLayout()
        self.folder_input = QLineEdit()
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_folder)
        folder_layout.addWidget(QLabel("Folder:"))
        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(browse_btn)

        regex_layout = QHBoxLayout()
        self.regex_input = QLineEdit()
        regex_layout.addWidget(QLabel("Regex:"))
        regex_layout.addWidget(self.regex_input)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.run_search)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(["Filename", "Path"])
        self.results_table.horizontalHeader().setStretchLastSection(True)

        self.results_table.cellDoubleClicked.connect(self.open_file_from_table)

        layout.addLayout(folder_layout)
        layout.addLayout(regex_layout)
        layout.addWidget(search_btn)
        layout.addWidget(self.results_table)

        self.setLayout(layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_input.setText(folder)

    def run_search(self):
        folder = self.folder_input.text().strip()
        pattern = self.regex_input.text().strip()

        if not folder or not os.path.isdir(folder):
            QMessageBox.warning(self, "Error", "Please select a valid folder.")
            return
        if not pattern:
            QMessageBox.warning(self, "Error", "Please enter a regex pattern.")
            return

        results, error = regex_search(folder, pattern)
        if error:
            QMessageBox.critical(self, "Regex Error", error)
            return

        self.results_table.setRowCount(len(results))
        for row, (fname, path) in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(fname))
            self.results_table.setItem(row, 1, QTableWidgetItem(path))

    def open_file_from_table(self, row, col):
        path_item = self.results_table.item(row, 1)
        if path_item:
            filepath = path_item.text()
            if os.path.exists(filepath):
                try:
                    os.startfile(filepath)
                except Exception as e:
                    QMessageBox.critical(
                        self, "Open Error", f"Could not open file:\n{e}"
                    )
            else:
                QMessageBox.warning(self, "Not Found", f"File not found:\n{filepath}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegexSearchApp()
    window.show()
    sys.exit(app.exec())
