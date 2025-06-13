# Freight API (Simple Test Project)

Simple Django + Django Rest Framework project untuk simulasi perhitungan ongkos kirim.

---

## 📦 API Endpoint

### 1. Search Country

**GET** `/api/countries?search={query}`

- Return list country berdasarkan keyword search.

### 2. Search Category (By Country)

**GET** `/api/categories?country_id={id}&search={query}`

- Return list kategori berdasarkan country.

### 3. Calculate Freight

**POST** `/api/calculate`

**Request Body:**

```json
{
  "country_id": 1,
  "category_id": 2,
  "destination_id": 3,
  "weight": 5
}
```

**Response:**
```json
{
  "origin": "Indonesia",
  "destination": "Bandung",
  "category_name": "Fresh Fruit",
  "international_price": 75000,
  "domestic_price": 50000,
  "total_price": 125000
}
```

### 🚀 Setup
Clone repo & install package

```bash
pip install -r requirements.txt
```

Apply migration

```bash
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

⚠️ Catatan
Domestic price masih dummy: weight * 10000

Dummy destination masih hardcode

