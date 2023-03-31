import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class CameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.camera = None
        self.photo = None
        self.initUI()

    def initUI(self):
        # Create a label widget to display the camera frame
        self.camera_label = QLabel()
        self.camera_label.setAlignment(Qt.AlignCenter)

        # Create a label widget to display the captured photo
        self.photo_label = QLabel()
        self.photo_label.setAlignment(Qt.AlignCenter)

        # Create a button to capture the photo and a layout for the UI
        capture_button = QPushButton('Capture')
        capture_button.setGeometry(100,100,50,50)
        hbox = QHBoxLayout()
        hbox.addWidget(self.camera_label)
        hbox.addWidget(self.photo_label)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(capture_button)

        # Set the layout
        self.setLayout(vbox)
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Camera App')

        # When the capture button is clicked, capture the photo
        capture_button.clicked.connect(self.capture_photo)
        capture_button.clicked.connect(self.capture_photo)

        # Start the camera
        self.start_camera()

    def start_camera(self):
        # Open the webcam
        self.camera = cv2.VideoCapture(0)

        # Create a timer to read frames from the webcam and update the label widget
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)

    def update_frame(self):
        # Capture a frame from the webcam
        ret, frame = self.camera.read()

        # Convert the frame from BGR to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a QImage from the RGB frame
        image = QImage(rgb_frame, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)

        # Create a QPixmap from the QImage and set it to the camera label widget
        self.camera_label.setPixmap(QPixmap.fromImage(image))

    def capture_photo(self):
        # Stop the timer
        self.timer.stop()

        # Set the captured photo to the photo label widget
        if self.photo is not None:
            image = QImage(self.photo, self.photo.shape[1], self.photo.shape[0], QImage.Format_RGB888)
            self.photo_label.setPixmap(QPixmap.fromImage(image))

        # Capture a new photo from the webcam
        ret, frame = self.camera.read()

        # Convert the photo from BGR to RGB format
        rgb_photo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Store the photo for later use
        self.photo = rgb_photo

        # Create a QImage from the RGB photo
        image = QImage(rgb_photo, rgb_photo.shape[1], rgb_photo.shape[0], QImage.Format_RGB888)
        image.save()
        # Create a QPixmap from the QImage and set it to the camera label widget
        self.camera_label.setPixmap(QPixmap.fromImage(image))

        # Resume the timer
        self.timer.start(50)


clicked = False

def click_save():
    global clicked

    clicked = True

def open_camera():
    global clicked
    while True:
        app = QApplication([])
        camera_app = CameraApp()
        camera_app.show()
        app.exec_()
        if clicked == True:
            camera_app.close()
            break
        else:
            pass
open_camera()