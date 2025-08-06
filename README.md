# 🏋️‍♂️ Gym Slot AutoBooker

At my friends’ dormitory gym, booking workout slots is managed through a shared Google Calendar system. The residents of the dorm need to book the slot using their Membership ID. However, the booking window opens precisely at midnight for slots available for two days later (i.e., the day after tomorrow). This leads to a rush as many users try to secure popular time slots immediately at midnight.

To simplify this process, reduce the stress of manual booking at an exact time and also I just wanted to play around with automating this workflow and try something new.
So, to test my theory I developed my own Appointment booking Demo application and finished my first draft of this automation.

# What is currently does - 

This first draft focuses on automating the booking process for a single slot, with plans to enhance it later by managing multiple bookings and possibly cancellations efficiently.
A Python-based automation script using Selenium to book gym slots via a Google Calendar appointment schedule. This is helpful for users who want to ensure they reserve their preferred gym slots in advance, respecting the booking rules (e.g., book at least 23 hours prior).

---

## 📌 Features

- Automatically selects slots 2 days ahead (Since my Mock Application had this constraint, but you can modify it according to your own need)
- Selects specific time ranges (e.g., 3:30pm).
- Fills in contact details in the form -first name, last name, email (For more professional use case Specific ID's to be used in order to verify against duplicate bookings)
- Submits the booking.

---
## 🚀 Getting Started
```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
pip install --necessary dependencies

# Step 4: Execute the script
python autoBook.py

```
---

## Potential Ideas to be implemented
> - Automating the script execution locally and log the bookings in order to track the booking so as to not book mutiple slot for the same day
> - ⚠️ If multiple slots are booked on the same day manually, they may be deleted without prior notice (enforcement feature to be added later) or only one booking per day for a single email ID in this projects context.
> - 📌 Incorporate special identifier such as Membership ID in the form for identification

---



