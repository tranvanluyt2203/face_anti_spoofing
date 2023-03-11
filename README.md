<h1>Cách chạy</h1> 
<br><b>1) Quay video bỏ vào MaiAL_Anti_Fake/Videos với tên real.mp4</b>
<br><b>2) Lấy video chạy bằng điện thoại và quay lưu vào MaiAL_Anti_Fake/V17:19 Thứ ideos với tên fake.mp4</b><br>
<h3>Tiền xử lí</h3>
Ở bước trước chúng ta đã có 2 file real.mp4 và fake.mp4 rồi. Sang bước này chúng ta sẽ tiền xử lý để làm 2 việc:

Tách các video nói trên thành các frame
Cắt khuôn mặt trong các frame và lưu vào 2 thư mục fake và real riêng để phục vụ công tác train.
Chúng ta tiến hành tiền xử lý file real.mp4 trước bằng lệnh sau:
<br><b>python face_extract.py --input MaiAL_Anti_Fake/videos/real.mp4 --output dataset/real </b>
<br>Input là file video, output là thư mục sẽ lưu các khuôn mặt được cắt ra để train, ở đây là dataset/real (kiểm tra thư mục xem có file chưa).

Tiếp đến file fake.mp4, chúng ta cũng chạy lệnh tương tự:
<br><b>python face_extract.py --input MaiAL_Anti_Fake/videos/fake.mp4 --output dataset/fake </b>
________________________________
<h3>Chạy chương trình</h3>

train cho model của chúng ta hiểu đâu là fake, đâu là real : 
<br><b>chạy python train_liveness.py</b>
 Kiểm thử model Chống giả mạo 
<br><b>chạy python liveness_demo.py </b>

