import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load mô hình
model = load_model('face_anti_spoofing_model.h5')

# Định nghĩa lớp
classes = ['real', 'spoof']

# Đọc ảnh
image = cv2.imread('testing_data/real_00001.jpg')

# Resize ảnh
image = cv2.resize(image, (32, 32))

# Chuyển đổi ảnh thành numpy array và chuẩn hóa
image = np.array(image) / 255.0

# Thêm chiều batch
image = np.expand_dims(image, axis=0)

# Dự đoán lớp của ảnh
predictions = model.predict(image)

# Lấy chỉ số của lớp có xác suất cao nhất
class_idx = np.argmax(predictions)

# Lấy tên lớp tương ứng với chỉ số
class_name = classes[class_idx]

# In kết quả
print('Class:', class_name)
