
<h1>
  <img src="https://raw.githubusercontent.com/meetvivek/FoodieHub-Django/main/food/static/food/LOGO.png" alt="FoodieHub Logo" width="30" />
  FoodieHub-Django
</h1>

FoodieHub is a Django-based web application where users can register, log in, and manage food items. Each user can add, edit, or delete their own food listings, which are displayed with the name of the user who posted them. The app also includes a profile page for each user.

This project developed as part of my learning journey with Django. The project helped me to practically apply various Django concepts like views, models, templates, and authentication. It serves as a hands-on exercise to solidify my understanding of Django and web development in general.
## Features

- **User Authentication**: 
  - Register, Login, and Logout functionality.
  - Profile pages for each user.
  - Route restrictions to ensure only authenticated users can access certain features.
  
- **Food Listings**: 
  - Users can add new food items with details.
  - Only the user who added a food item can edit or delete it.
  
- **Django Concepts Used**:
  - **Views**: Both function-based and class-based views were implemented.
  - **URL Patterns**: Configured to handle different app routes.
  - **Models**: Used to define the structure of the food items and user profiles.
  - **Admin Panel**: Integrated to manage the application’s data.
  - **Templates**: Utilized for rendering the frontend.
  - **Static Files**: Managed for styling and scripts.
  - **Django Forms**: Used for handling user inputs.
  - **Django Signals**: Implemented for automating tasks like updating profiles.
    
- **Bootstrap**: Used for responsive design and styling.


## Requirements

- Python 3.x
- Django 3.x or higher
- Other dependencies are listed in `requirements.txt`.
  
## Installation

### Clone the repository:
```bash
git clone https://github.com/meetvivek/FoodieHub-Django.git
cd FoodieHub-Django
```

### Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### Install the required packages:
```bash
pip install -r requirements.txt
```

### Apply migrations:
```bash
python manage.py migrate
```

### Run the development server:
```bash
python manage.py runserver
```

### Access the application in your browser at 'http://127.0.0.1:8000/food'

## Deployment
The project is hosted on PythonAnywhere. You can view it live at '[FoodieHub on PythonAnywhere](https://meetvivek.pythonanywhere.com/food/)'.

## Contributing
Contributions are welcome! Please feel free to submit a pull request.
