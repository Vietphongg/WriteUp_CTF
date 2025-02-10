
Bước 1: Sử dụng thuật toán CRT   
Dữ liệu ban đầu bao gồm các giá trị c, n, và các tham số liên quan đến RSA.  
Áp dụng Chinese Remainder Theorem (CRT) để tính giá trị y_cubed từ các giá trị c[i] và n[i].  
Bước 2: Tìm căn bậc ba  
Sau khi tính được y_cubed, thực hiện tính căn bậc ba (cube root) để lấy giá trị y.  
Bước 3: Chuyển đổi từ số nguyên sang byte  
Chuyển y (giá trị nguyên) thành một chuỗi byte bằng cách sử dụng long_to_bytes.  
Sau đó, giải mã chuỗi byte này để lấy chuỗi flag.  
  
