import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import transcription_logic as tl
import os

class Worker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            self.progress.emit(0)
            audio_mp4 = tl.baixar_audio(self.url)
            self.progress.emit(33)
            audio_wav = tl.converter_audio(audio_mp4)
            self.progress.emit(66)
            transcription = tl.transcrever_audio(audio_wav)
            self.progress.emit(100)

            print(f"Tipo de Transcrição: {type(transcription)}")
            print(f"Valor de Transcrição: {transcription}")

            if isinstance(transcription, str):
                self.finished.emit(transcription)
            else:
                raise ValueError("Transcrição não é uma string")

            os.remove(audio_mp4)
            os.remove(audio_wav)
        except Exception as e:
            self.error.emit(str(e))

class TranscriptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Transcrição de vídeos do YouTube')

        self.layout = QVBoxLayout()

        self.label = QLabel('Insira aqui a URL do Youtube')
        self.layout.addWidget(self.label)

        self.url_entry = QLineEdit()
        self.layout.addWidget(self.url_entry)

        self.process_button = QPushButton('Processar Agora!', self)
        self.process_button.clicked.connect(self.process_url)
        self.layout.addWidget(self.process_button)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.progress_bar)

        self.result_label = QLabel('Transcrição do áudio: ')
        self.layout.addWidget(self.result_label)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        self.setLayout(self.layout)

    def process_url(self):
        url = self.url_entry.text()
        self.worker = Worker(url)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.show_result)
        self.worker.error.connect(self.show_error)
        self.worker.start()

    def update_progress(self, value):
        print(f'Progresso atual: {value}')
        self.progress_bar.setValue(value)

    def show_result(self, transcription):
        print(f"Resultado final: {transcription}")
        self.result_text.setPlainText(transcription)
        self.progress_bar.setValue(0)

    def show_error(self, error_message):
        print(f"Erro: {error_message}")
        self.result_text.setPlainText(f'Erro ao processar URL: {error_message}')
        self.progress_bar.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranscriptionApp()
    ex.show()
    sys.exit(app.exec_())
