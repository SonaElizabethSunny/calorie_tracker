# Calorie Tracker
A web application built with Django that allows users to track their calorie intake by logging food items. It provides real-time calorie calculation, along with health tips based on the user's total calorie intake.
## Features
- User login and registration.
- Add and manage food items with their calorie details.
- Track daily calorie intake.
- Get tips based on the total calories consumed.
- Search functionality for food items.
- Responsive and modern user interface using Bootstrap.
## Installation

1. Clone the repository:
2. Navigate to the project directory:

3. Set up a virtual environment:
- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
- For Mac/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install the required dependencies:

5. Apply migrations to set up the database:

6. Create a superuser to access the admin panel:
 
7. Run the development server:

## Usage
- Register or login to the app.
- Add food items with their calorie details.
- Track your calorie intake for each day.
- Use the search bar to find food items.
- View your daily total calorie count and get tips based on it.

## Technologies Used
- Django (Python Web Framework)
- HTML, CSS, Bootstrap (for the frontend)
- JavaScript (for food search functionality)
- SQLite (default database for Django)

## Contributing
1. Fork the project.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.
--------------------------------------------------

8. Usage
   
After setting up the project:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to use the calorie tracker app.

9. Future Improvements
    
Add daily goal reminders.

Dark mode support.

Generate weekly and monthly calorie reports (PDF export).

Visual calorie trends with charts/graphs using Chart.js or Recharts.

Integrate barcode scanner (for packaged food items).

Create a mobile-friendly PWA version (Progressive Web App).

Add calorie burn tracking via exercise logs.


Author

Sona Sunny
GitHub Profile: https://github.com/SonaElizabethSunny
