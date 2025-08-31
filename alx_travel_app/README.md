# 🏖️ ALX Travel App 0x00

This project is a backend service for managing travel listings, bookings, and reviews.  
It was created as part of the ALX backend learning tasks.  
Key additions include:
- Defined database models (`Listing`, `Booking`, `Review`)
- Implemented serializers for API data representation
- Management command to seed the database with sample data

---

## ✨ Features

✅ **Listings Management**
- Create and store travel property listings with details like location, price, and description.

✅ **Bookings**
- Guests can create bookings for listings with check-in/check-out dates and status tracking.

✅ **Reviews**
- Guests can review completed bookings and leave ratings.

✅ **Seed Command**
- A management command to populate the database with sample data for quick testing.

---

## 📂 **Project Structure**


---

## ⚙️ **Models**

- **Listing**
  - `host` (FK to User)
  - `title`, `description`, `location`
  - `price_per_night`
  - Timestamps

- **Booking**
  - `listing` (FK to Listing)
  - `guest` (FK to User)
  - `check_in`, `check_out`, `status`

- **Review**
  - `booking` (OneToOne FK to Booking)
  - `reviewer` (FK to User)
  - `rating`, `comment`

---

## 📦 **Serializers**

- `ListingSerializer`: exposes listing fields
- `BookingSerializer`: exposes booking fields

---
