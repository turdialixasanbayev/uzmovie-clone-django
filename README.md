# uzmovie-clone-django

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Umumiy ma’lumot

**uzmovie-clone-django** — bu Django asosida yozilgan web ilova bo‘lib, UZMovie saytidagi ba’zi funksiyalarni klon qiladi. Masalan, filmlar ro‘yxatini ko‘rish, autentifikatsiya (foydalanuvchi tizimiga kirish), profil sozlamalari va hokazo.

---

## Xususiyatlari

- Django framework — Python 3+ asosida  
- Foydalanuvchi autentifikatsiyasi (kirish, ro‘yxatdan o‘tish)  
- Film va kontent ro‘yxatini ko‘rish  
- Template’lar orqali frontend interfeys  
- Loyihaning muhitini sozlash uchun `.env` fayl namunasi  
- `requirements/` papkasida zarur kutubxonalar ro‘yxati

---

## Strukturasi

```
uzmovie-clone-django/
├── apps/              # Django ilovalari (app’lar)
├── config/            # Loyihaning asosiy konfiguratsiyalari
├── templates/         # HTML shablonlar
│   └── base/          # Bosh shablonlar
├── images/            # Rasm va tasvirlar
├── requirements/      # Python kutubxonalar ro‘yxati
├── scripts/           # Ishga tushirish va yordamchi skriptlar
├── .env.example       # Muhit o‘zgaruvchilari namunasi
├── manage.py          # Django jarayonini boshqarish ssenariysi
└── README.md          # Loyihaning ushbu hujjati
```

---

## O‘rnatish (Installation)

Quyidagilarni bajarish orqali loyiha nusxasini o‘rnatishingiz mumkin:

1. Repo’ni klonlash:
   ```bash
   git clone https://github.com/turdialixasanbayev/uzmovie-clone-django.git
   cd uzmovie-clone-django
   ```

2. Virtual muhit yaratish (masalan, `venv`):
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Linux/macOS
   # yoki
   venv\Scripts\activate           # Windows
   ```

3. Kerakli kutubxonalarni o‘rnatish:
   ```bash
   pip install -r requirements/base.txt
   # Agar `requirements/` ning boshqa fayllari bo‘lsa, ularni ham ko‘rib oling
   ```

4. `.env` faylini sozlash:
   `.env.example` fayldan nusxa ko‘chiring va kerakli o‘zgaruvchilarni to‘ldiring (masalan, SECRET_KEY, DB sozlamalari, DEBUG va h.k.)

5. Ma’lumotlar bazasini migratsiya qilish:
   ```bash
   python manage.py migrate
   ```

6. Ishga tushirish:
   ```bash
   python manage.py runserver
   ```

7. Brauzerda oching:
   ```
   http://127.0.0.1:8000/
   ```

---

## Foydalanish

- Foydalanuvchi ro‘yxatdan o‘tishi va tizimga kirishi mumkin  
- Sahifalardan film ro‘yxatini ko‘rish  
- Bosh sahifa, ma’lumotlar sahifalari va boshqa mumkin bo‘lgan sahifalarlar bilan ishlash  

---

## Loyiha rejalari (Roadmap)

- Film tavsiyalari (recommendation) tizimi  
- Admin panelini kengaytirish, film qo‘shish va tahrirlash imkoniyati  
- Mobilga moslashuvchan dizayn (responsive design) yaxshilash  
- API qo‘llab-quvvatlash (masalan, REST APIs)  
- Test yozish (unit va integration testlar)

---

## Hissa qo‘shish (Contributing)

Agar biror g‘oya yoki xatolik topsangiz, quyidagilarni amalga oshiring:

1. Fork qiling  
2. Yangi branch yarating (`git checkout -b feature/yangifunksiya`)  
3. O‘zgartirishlaringizni commit qiling (`git commit -m "Qo‘shildi: yangi funksiya"`)  
4. Push qiling (`git push origin feature/yangifunksiya`)  
5. Pull request yuboring

---

## Litsenziya

Ushbu loyiha **MIT Litsenziyasi** ostida tarqatiladi.  
Batafsil ma’lumot `LICENSE` faylida.

---

## Muallif

Turdiali Xasanbayev — backend developer  
Repo: [turdialixasanbayev/uzmovie-clone-django](https://github.com/turdialixasanbayev/uzmovie-clone-django)
