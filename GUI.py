import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QFileDialog, QWidget, 
                             QTabWidget, QMenuBar, QAction, QMenu, QScrollArea,
                             QSplitter, QFrame)
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtCore import Qt
import cv2
import numpy as np

class ImageProcessingGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.student_id = "1229641"  # Öğrenci numarası 
        self.student_name = "Öğrenci Adı"  # Öğrenci adı buraya yazılacak
        self.course_name = "Dijital Görüntü İşleme"
        
        self.init_ui()
        
    def init_ui(self):
        # Ana pencere ayarları
        self.setWindowTitle(f"{self.course_name} - {self.student_name} ({self.student_id})")
        self.setGeometry(100, 100, 1000, 800)
        
        # Ana widget oluşturma
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Ana layout
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Başlık
        self.create_header()
        
        # Menü çubuğu oluşturma
        self.create_menu_bar()
        
        # Tab widget oluşturma (Ödevler için)
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        
        # Ödev tablarını oluştur
        self.create_assignment_tabs()
        
        self.show()
    
    def create_header(self):
        # Başlık bölümü
        header_frame = QFrame()
        header_frame.setFrameShape(QFrame.StyledPanel)
        header_layout = QVBoxLayout(header_frame)
        
        # Ders adı etiketi
        course_label = QLabel(self.course_name)
        course_label.setFont(QFont("Arial", 16, QFont.Bold))
        course_label.setAlignment(Qt.AlignCenter)
        
        # Öğrenci bilgileri etiketi
        student_label = QLabel(f"Öğrenci: {self.student_name} - {self.student_id}")
        student_label.setFont(QFont("Arial", 12))
        student_label.setAlignment(Qt.AlignCenter)
        
        header_layout.addWidget(course_label)
        header_layout.addWidget(student_label)
        
        self.main_layout.addWidget(header_frame)
    
    def create_menu_bar(self):
        # Menü çubuğu
        menu_bar = self.menuBar()
        
        # Dosya menüsü
        file_menu = menu_bar.addMenu("Dosya")
        
        # Görüntü Yükle aksiyonu
        load_image_action = QAction("Görüntü Yükle", self)
        load_image_action.triggered.connect(self.load_image)
        file_menu.addAction(load_image_action)
        
        # Çıkış aksiyonu
        exit_action = QAction("Çıkış", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Ödevler menüsü
        assignments_menu = menu_bar.addMenu("Ödevler")
        
        # Ödev aksiyonları
        for i in range(1, 6):  # Örnek olarak 5 ödev
            assignment_action = QAction(f"Ödev {i}", self)
            assignment_action.triggered.connect(lambda checked, index=i-1: self.tab_widget.setCurrentIndex(index))
            assignments_menu.addAction(assignment_action)
    
    def create_assignment_tabs(self):
        # Ödev 1 tab'ı
        self.assignment1_tab = QWidget()
        self.tab_widget.addTab(self.assignment1_tab, "Ödev 1: GUI Tasarımı")
        
        # Ödev 1 layout
        assignment1_layout = QVBoxLayout(self.assignment1_tab)
        
        # Açıklama
        description_label = QLabel("Ödev 1: GUI Tasarımı ve Temel İşlevselliğin Oluşturulması")
        description_label.setFont(QFont("Arial", 12, QFont.Bold))
        assignment1_layout.addWidget(description_label)
        
        # Ödev detayları
        details_label = QLabel("Bu ödevde temel bir görüntü işleme arayüzü oluşturulmuştur. "
                              "Görüntü yükleyebilir ve basit işlemler uygulayabilirsiniz.")
        details_label.setWordWrap(True)
        assignment1_layout.addWidget(details_label)
        
        # Görüntü yükleme butonu
        load_button = QPushButton("Görüntü Yükle")
        load_button.clicked.connect(self.load_image)
        assignment1_layout.addWidget(load_button)
        
        # İşlem butonları için yatay layout
        operations_layout = QHBoxLayout()
        
        # Gri tonlama butonu
        grayscale_button = QPushButton("Gri Tonlama")
        grayscale_button.clicked.connect(self.convert_to_grayscale)
        operations_layout.addWidget(grayscale_button)
        
        # Yatay çevirme butonu
        flip_h_button = QPushButton("Yatay Çevir")
        flip_h_button.clicked.connect(self.flip_horizontal)
        operations_layout.addWidget(flip_h_button)
        
        # Dikey çevirme butonu
        flip_v_button = QPushButton("Dikey Çevir")
        flip_v_button.clicked.connect(self.flip_vertical)
        operations_layout.addWidget(flip_v_button)
        
        # Orijinal görüntüye dönme butonu
        reset_button = QPushButton("Orijinale Dön")
        reset_button.clicked.connect(self.reset_image)
        operations_layout.addWidget(reset_button)
        
        assignment1_layout.addLayout(operations_layout)
        
        # Görüntü gösterme alanı
        image_layout = QHBoxLayout()
        
        # Orijinal görüntü alanı
        self.original_image_frame = QFrame()
        self.original_image_frame.setFrameShape(QFrame.StyledPanel)
        original_image_layout = QVBoxLayout(self.original_image_frame)
        
        original_title = QLabel("Orijinal Görüntü")
        original_title.setAlignment(Qt.AlignCenter)
        original_image_layout.addWidget(original_title)
        
        self.original_image_label = QLabel()
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setText("Görüntü yüklenmedi")
        original_image_layout.addWidget(self.original_image_label)
        
        # İşlenmiş görüntü alanı
        self.processed_image_frame = QFrame()
        self.processed_image_frame.setFrameShape(QFrame.StyledPanel)
        processed_image_layout = QVBoxLayout(self.processed_image_frame)
        
        processed_title = QLabel("İşlenmiş Görüntü")
        processed_title.setAlignment(Qt.AlignCenter)
        processed_image_layout.addWidget(processed_title)
        
        self.processed_image_label = QLabel()
        self.processed_image_label.setAlignment(Qt.AlignCenter)
        self.processed_image_label.setText("İşlenmiş görüntü yok")
        processed_image_layout.addWidget(self.processed_image_label)
        
        image_layout.addWidget(self.original_image_frame)
        image_layout.addWidget(self.processed_image_frame)
        
        assignment1_layout.addLayout(image_layout)
        
        # Diğer ödev tabları için örnek (boş)
        for i in range(2, 6):  # Örnek olarak 5 ödev
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)
            tab_label = QLabel(f"Ödev {i} içeriği burada gösterilecek")
            tab_label.setAlignment(Qt.AlignCenter)
            tab_layout.addWidget(tab_label)
            self.tab_widget.addTab(tab, f"Ödev {i}")
    
    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Görüntü Dosyası Seç", "", 
                                                 "Görüntü Dosyaları (*.png *.jpg *.bmp *.jpeg)")
        
        if file_name:
            # OpenCV ile görüntüyü oku
            self.cv_image = cv2.imread(file_name)
            
            if self.cv_image is not None:
                # Orijinal görüntüyü sakla
                self.original_cv_image = self.cv_image.copy()
                
                # Görüntüyü görüntüle
                self.display_image(self.cv_image, self.original_image_label)
                self.processed_image_label.setText("İşlenmiş görüntü yok")
            else:
                self.original_image_label.setText("Görüntü yüklenemedi!")
    
    def display_image(self, cv_img, label, max_size=400):
        if cv_img is None:
            return
        
        # BGR'dan RGB'ye dönüştür (OpenCV BGR, Qt RGB kullanır)
        if len(cv_img.shape) == 3:  # Renkli görüntü
            cv_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        else:  # Gri tonlamalı görüntü
            cv_rgb = cv2.cvtColor(cv_img, cv2.COLOR_GRAY2RGB)
        
        # Görüntüyü QImage'e dönüştür
        h, w, ch = cv_rgb.shape
        bytes_per_line = ch * w
        q_img = QImage(cv_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # Görüntüyü ölçeklendir (boyutu çok büyükse)
        pixmap = QPixmap.fromImage(q_img)
        if pixmap.width() > max_size or pixmap.height() > max_size:
            pixmap = pixmap.scaled(max_size, max_size, Qt.KeepAspectRatio)
        
        # QLabel'a görüntüyü ayarla
        label.setPixmap(pixmap)
    
    def convert_to_grayscale(self):
        if hasattr(self, 'cv_image') and self.cv_image is not None:
            gray_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2GRAY)
            self.display_image(gray_image, self.processed_image_label)
    
    def flip_horizontal(self):
        if hasattr(self, 'cv_image') and self.cv_image is not None:
            flipped_image = cv2.flip(self.cv_image, 1)  # 1 = yatay çevirme
            self.display_image(flipped_image, self.processed_image_label)
    
    def flip_vertical(self):
        if hasattr(self, 'cv_image') and self.cv_image is not None:
            flipped_image = cv2.flip(self.cv_image, 0)  # 0 = dikey çevirme
            self.display_image(flipped_image, self.processed_image_label)
    
    def reset_image(self):
        if hasattr(self, 'original_cv_image') and self.original_cv_image is not None:
            self.cv_image = self.original_cv_image.copy()
            self.display_image(self.cv_image, self.original_image_label)
            self.processed_image_label.setText("İşlenmiş görüntü yok")

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessingGUI()
    sys.exit(app.exec_())

 