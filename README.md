## 📝NumberOfDays

```
Find the number of days in the given month and year 

    Leap year (where February has 29 days) is the year that is either
        - a divisible by 400 OR
        - b divisible by 4 but not divisible by 100
        Examples of leap year: 2000, 2020, 2024, 4, 40
        Examples of non-leap year (February has 28 days): 2025, 2019, 2100, 100

    Return 'Error' if inputs are out of range 
```
```
    พี่อยากให้น้อง ๆ ช่วยคิดโปรแกรมในการช่วยหาจำนวนวันในเดือนและปีตามที่กำหนดให้ 

    โดยมีการคำนวณดังนี้
    หากเป็นปีอธิกสุรทิน (ปีที่เดือนกุมภาพันธ์มี 29 วัน) สามารถคำนวณได้โดยการ
        1. เป็นปีที่หารด้วย 400 ลงตัว
        หรือ 2. เป็นปีที่หารด้วย 4 ลงตัว แต่หารด้วย 100 ไม่ลงตัว
    เช่น ปีอธิกสุรทิน: 2000, 2020, 2024, 4, 40
    ปีที่ไม่ใช่ปีอธิกสุรทิน (เดือนกุมภาพันธ์มี 28 วัน): 2025, 2019, 2100, 100
```
## 📥Input(s)
```
    month, year
```

## 📤Output(s)
```
    Number of Days (จำนวนวันของเดือนนั้น ๆ)
```

## ⚙️Function

The function is defined in the file `NumberOfDays.py` as the following:
>This is your default function for this Quiz

```python
def NumberOfDays(month,year):

    return 0
```

## 💡 Example  

**Input**  
```python
1. NumberOfDays(2,2100)
2. NumberOfDays(11,2020)
3. NumberOfDays(2,2020)
```

**Output**
```python
1. 28
2. 30
3. 29
```

## ▶️ To Run a Test Case  

### 🪟 Windows 
    run a file name "run_window.ps1"
### 🍎 macOS
    run a file name "run_macos.sh"

## 🚨 Importance  

⚠️ **Always commit and push your code to origin before calling the TA to submit your quiz!**  
🚀 This ensures your latest work is saved and reviewed correctly.
