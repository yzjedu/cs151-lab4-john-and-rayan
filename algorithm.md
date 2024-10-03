# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Start program
2. Ask user for input of package
3. While input not Package Green, Package Blue, Package Purple:
   1. Output ('Invalid package. Please put a valid answer')
   2. Ask for reinput
4. If input is Package Green:
   1. price = 49.99
   2. gb = 2
   3. Ask user for input of how much extra GB they've used (extra_gb)
      1. If extra_gb > gb:
         1. (extra_gb - gb) * 15 = gb
         2. price = price + gb
   4. Ask user if they have a coupon or not
      1. If coupon = yes and package = package_green and price >= 75:
         2. price =  price - 25
   5. Output price and GB
5. Else if input is Package Blue:
   1. price = 70
   2. gb = 4
   3. Ask user for input of how much extra GB they've used (extra_gb)
      1. If extra_gb > gb:
         1. (extragb - gb) * 10 = gb
         2. price = price + gb
   4. Output price and GB
6. Else if input is Package Purple:
   1. price =  99.95
   2. gb = unlimited
   3. Output price and GB
7. End program