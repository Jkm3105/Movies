# 🎬 Movie Booking API

A RESTful API for a movie ticket booking system. This project allows users to browse movies, view showtimes, select seats, and make reservations.

---

## 🚀 Features

* User Authentication (Signup/Login)
* Movie Management
* Theatre & Screen Management
* Showtime Scheduling
* Seat Management
* Ticket Reservation System

---

## 🔄 Project Flow

After authentication, the system follows this flow:

```
User → Movie → Theatre → Screen → Showtime → Seats → Reservation
```

---

## 🔐 Authentication

### 📌 Signup

`POST /auth/register`

```json
{
  "email": "string",
  "password": "string"
}
```

### 📌 Login

`POST /auth/login`

```json
{
  "email": "string",
  "password": "string"
}
```

---

## 🎥 Movies

### Get Movies

`GET /movies`

```json
[
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "poster_url": "string"
  }
]
```

### Create Movie

`POST /movies`

```json
{
  "title": "string",
  "description": "string",
  "poster_url": "string"
}
```

---

## 🏢 Theatre

### Get Theatres

`GET /theatre`

```json
[
  {
    "id": "string",
    "name": "string",
    "location": "string"
  }
]
```

### Create Theatre

`POST /theatre`

```json
{
  "name": "string",
  "location": "string"
}
```

---

## 🎭 Screen

### Get Screens

`GET /screen`

```json
[
  {
    "id": "string",
    "name": "string",
    "theatre_id": "string"
  }
]
```

### Create Screen

`POST /screen`

```json
{
  "name": "string",
  "theatre_id": "string"
}
```

---

## ⏰ Showtime

### Get Showtimes

`GET /showtime`

```json
[
  {
    "id": "string",
    "movie_id": "string",
    "screen_id": "string",
    "start_time": "datetime",
    "end_time": "datetime",
    "total_seats": 0,
    "price": 0
  }
]
```

### Create Showtime

`POST /showtime`

```json
{
  "movie_id": "string",
  "screen_id": "string",
  "start_time": "datetime",
  "end_time": "datetime",
  "total_seats": 1,
  "price": 0
}
```

---

## 💺 Seats

### Get All Seats

`GET /seat`

```json
[
  {
    "id": "string",
    "seat_number": "string",
    "row": "string",
    "price": 0,
    "screen_id": "string"
  }
]
```

### Create Seat

`POST /seat`

```json
{
  "seat_number": "string",
  "row": "string",
  "price": 0,
  "screen_id": "string"
}
```

### Get Seats by Screen

`GET /seat/screen/{screen_id}`

---

## 🎟️ Reservation

### Create Reservation

`POST /reservation`

```json
{
  "user_id": "string",
  "showtime_id": "string",
  "seat_ids": ["string"]
}
```

---

## 🛒 Cart & Orders (Optional if used)

### Add to Cart

`POST /cart/add`

### Get Cart

`GET /cart`

### Checkout

`POST /order/checkout`

### Payment Success

`GET /order/success`

---

## 🧠 How It Works

1. User signs up or logs in
2. User browses available movies
3. Selects a theatre
4. Chooses a screen
5. Picks a showtime
6. Selects available seats
7. Creates a reservation

---

## 🛠️ Tech Stack

*   Backend: FastAPI (Python-based high-performance web framework)
    Database: PostgreSQL (Relational database for structured data)
    API Documentation: Swagger UI / OpenAPI (auto-generated interactive docs via FastAPI)

---
