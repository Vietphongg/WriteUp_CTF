giá trị moneyAccount là int (giới hạn từ -2147483648 đến 2147483647)  

thử nhập một số lớn để gây tràn số (integer overflow) trong phép nhân:  

How many codes do you want to buy? > 1431655765  

Vì totalCost = buyQuantities * VIDEO_PRICE, nếu buyQuantities đủ lớn, phép nhân có thể gây overflow, dẫn đến totalCost trở thành một số âm hoặc một số nhỏ hơn moneyAccount.
