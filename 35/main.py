n = int(input("تعداد تيله رو وارد کن:"))
if n % 3 == 0:
    print("من نفر دومم ")
else:
    print("من نفر اول هستم")
    m = n % 3
    print(f" من {m} تعداد تيله برميدارم")
    n = n - m
    
# wehile n > 0:
#     print(f" اکنون {n} تيله روي ميز است ")
#     m = int(input("چند تيله برميداري ؟ "))
#     n = n - m