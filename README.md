# 🔍 Booking.com URL Status Checker (Streamlit App)

This is a Streamlit web app that takes an Excel file containing Booking.com hotel URLs and checks the availability status of each property.

---

## 🚀 Features

- ✅ Check if a hotel is currently available for booking
- 🔁 Detect if the URL redirects to a listing page or another hotel
- ❌ Identify properties that are not taking reservations
- 📥 Upload `.xlsx` files with hotel URLs
- 📤 Download a processed Excel file with status results
- 📊 Summary of results directly in the app

---

## 📁 Excel Format (Input)

Upload a file like this:

| URL |
|-----|
| https://www.booking.com/hotel/... |
| https://www.booking.com/hotel/... |

- **Column name must be exactly `URL`**
- Must be in `.xlsx` format (Excel)

---

## 🧠 Booking Status Legend

| Status                              | Meaning                                                |
|-------------------------------------|--------------------------------------------------------|
| ✅ Available                        | Hotel is bookable                                      |
| ❌ Not Taking Reservations          | Hotel not taking bookings (shown on page)              |
| 🔁 Redirected to Listing Page       | Redirected to unknown page                             |
| 🔁 Redirected to Listing Page       | Redirected to a list of hotels                         |
| ➡️ Redirected to Another Hotel Page | Redirected to a different hotel page                   |
| ❌ Error / Invalid URL              | URL was empty, invalid, or caused a request failure    |

---

## 📦 Installation (Local Use)

```bash
# Clone this repository
git [clone https://github.com/your-username/booking-status-checker.git](https://github.com/Donotmakenoise/check_booking_status)
cd booking-status-checker

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
