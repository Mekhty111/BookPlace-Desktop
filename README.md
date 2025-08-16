# 🛫 MyBookingProject-Clone-Aviasales

---

## ✨ Key Features

- **Aviasales-style desktop UI:** Clean and modern design with custom icons and backgrounds using Tkinter and CustomTkinter
- **Multi-service portal:** Search flights, hotels, apartments, and car rentals in one app
- **Calendar date selection:** Date picker powered by `tkcalendar` for easy date input
- **Database integration:** Uses MySQL for managing and querying travel data (flights, hotels, cars)
- **Interactive UI elements:** Dynamic frames and buttons update content interactively without restarting the app
- **Random price display:** Mocked price generation to simulate realistic pricing
- **Custom fonts and images:** Uses Pillow (PIL) to handle icons and custom fonts for enhanced UI
- **Cart system:** Basic "basket" feature to collect selected bookings

---

## 🛠️ Technologies & Libraries

- **Python 3.x**
- **Tkinter** & **CustomTkinter** — for GUI components and styling
- **MySQL Connector/Python** — for database connectivity
- **Pillow (PIL)** — image and font handling
- **tkcalendar** — calendar date picker widget
- **Datetime** and **random** — for date parsing and randomization of prices

---
## 📂 Project Structure
```
├── MainApp.py            # Main application source code
├── apartments.csv        # Apartment rental data source
├── aviatickets.csv       # Flights data source
├── carsharing.csv        # Car rental data source
├── hotels.csv            # Hotels data source
├── Calendar_icons/       # Calendar-related icons/images
├── Cars/                 # Car images/assets
├── Fonts/                # Custom fonts used in the app
├── Hotels_pics/          # Hotel images
├── bakground_img/        # Background images
├── data/                 # Data folder (added/updated)
├── icons/                # General app icons
├── requirements          # Added requirements (новый файл/папка)
├── .gitignore            # Updated .gitignore
├── README.md             # Updated README

```
---
## 🚀 Installation & Setup

1. **Clone the repository:**

git clone https://github.com/Mekhty111/MyBookingProject-Clone-Aviasales-.git
cd MyBookingProject-Clone-Aviasales-

text

2. **Install required Python packages:**

pip install mysql-connector-python pillow tkcalendar customtkinter

text

3. **Set up MySQL database:**

- Create a new database named `travelDB` (or modify the connection settings in `MainApp.py` accordingly)
- Import the provided `Untitled.sql` file to initialize tables and sample data
- Update your MySQL user and password in the `MainApp.py` (`mysql.connector.connect`) connection section if different

4. **Run the application:**

python MainApp.py

text

---

## 🎯 Usage

- Use the top navigation buttons to switch between **flights**, **hotels**, **apartments**, and **car rental** search interfaces.
- Enter the required search input fields, for example, destination city or hotel name, select dates using the calendar widget.
- Click the search button to query available options from the database.
- Results are displayed with images, prices (randomly generated for simulation), and additional info.
- Selections can be added to the cart (basket) for easy review.

---

## 👨‍💻 Author

**Mekhty Mekhtyev**  
[LinkedIn](https://www.linkedin.com/in/mekhty-mekhtyev/) | [GitHub](https://github.com/Mekhty111)

---

💡 *This project is an educational desktop application clone showcasing Python GUI development combined with MySQL database integration and custom UI design to replicate a popular flight booking platform.*
