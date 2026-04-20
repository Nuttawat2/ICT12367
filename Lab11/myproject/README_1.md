# ICT12367 — ระบบจัดการข้อมูลประชากร

โปรเจกต์ Django สำหรับวิชา ICT12367 SPU  
พัฒนาระบบ CRUD + ค้นหาข้อมูลประชากร ครอบคลุม Assignment 11, 12, 13

---

## 📋 สิ่งที่ทำในแต่ละ Assignment

### Assignment 11 — รับส่งข้อมูลจากแบบฟอร์ม
- สร้างแบบฟอร์มกรอกชื่อ-นามสกุลและอายุ (`form.html`)
- บันทึกข้อมูลลงฐานข้อมูลผ่าน `views.py`
- แสดงตารางข้อมูลประชากรในหน้าแรก (`index.html`)
- เพิ่มฟิลด์วันที่เพิ่มข้อมูลในตาราง (`auto_now_add=True`)

### Assignment 12 — แบบฟอร์มแก้ไขข้อมูล
- สร้างหน้าแก้ไขข้อมูล (`edit.html`)
- เพิ่มฟังก์ชัน `edit()` และ `delete()` ใน `views.py`
- เพิ่ม URL pattern `/edit/<id>/` และ `/delete/<id>/` ใน `urls.py`
- ครบ CRUD (Create, Read, Update, Delete)

### Assignment 13 — การค้นหาข้อมูล
- เพิ่มช่องค้นหาใน `index.html` (method GET)
- ใช้ `Q object` จาก Django ORM กรองข้อมูลได้ทั้งชื่อและอายุ
- แสดงข้อความ "ไม่พบข้อมูล" เมื่อค้นหาไม่เจอ

---

## 🗂️ โครงสร้างโปรเจกต์

```
myproject/
├── myapp/
│   ├── templates/
│   │   ├── base.html       # Layout หลัก (Navbar, Footer)
│   │   ├── index.html      # หน้าแรก + ตารางประชากร + ค้นหา
│   │   ├── form.html       # แบบฟอร์มเพิ่มข้อมูล
│   │   ├── edit.html       # แบบฟอร์มแก้ไขข้อมูล
│   │   └── about.html      # หน้าแกลเลอรี่
│   ├── models.py           # Model: Person (name, age, date)
│   ├── views.py            # Logic: index, form, edit, delete
│   └── urls.py             # URL routing
└── myproject/
    └── settings.py
```

---

## 🚀 วิธีรันโปรเจกต์

```bash
python manage.py runserver
```

เปิดเบราว์เซอร์ไปที่ `http://127.0.0.1:8000/`

---

## 🛠️ Tech Stack

- Python 3
- Django
- SQLite
- Bootstrap 5
