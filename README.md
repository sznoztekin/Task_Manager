Attığınız dosyadaki projede türkçe dil desteği sunulmamıştır.

# Task Manager Uygulaması

Bu proje, kullanıcıların görevlerini yönetebildiği (CRUD), Flask tabanlı bir görev takip sistemidir.

## Özellikler

- Kayıt ol / Giriş yap / Oturumu kapat
- Her kullanıcının kendi görevlerini görmesi
- Görev ekle / güncelle / sil
- SQLite veritabanı kullanımı
- JSON API desteği (`/api/tasks`)
- Bootstrap 5 ile responsive arayüz

### Kurulum

```bash
git clone https://github.com/kullanici/task-tracker.git
cd task-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py




Örnek Kullanıcı Bilgileri


{
    "id": 1,
    "ad": "Ahmet Yılmaz",
    "email": "ahmet@example.com",
    "password": "sifre123_hashed",  // Gerçekte hash'lenmiş olarak saklanır
    "created_at": "2023-11-20T10:00:00"
}



JSON Çıktısı

[
    {
        "id": 1,
        "user_id": 1,
        "title": "Proje raporunu tamamla",
        "description": "Flask API dokümantasyonunu yaz",
        "due_date": "2023-12-10T23:59:00",
        "status": "Devam Ediyor",
        "created_at": "2023-11-25T09:30:00"
    },
    {
        "id": 2,
        "user_id": 1,
        "title": "Market alışverişi",
        "description": "Süt, ekmek, yumurta",
        "due_date": "2023-12-05T18:00:00",
        "status": "Beklemede",
        "created_at": "2023-11-28T14:15:00"
    },
    {
        "id": 3,
        "user_id": 1,
        "title": "Spor salonu",
        "description": null,  // Açıklama boş bırakılmış
        "due_date": null,     // Tarih atanmamış
        "status": "Tamamlandı",
        "created_at": "2023-11-30T20:00:00"
    }
]


