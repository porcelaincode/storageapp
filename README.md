<br />
<p align="center">
  <a href="https://github.com/porcelaincode/storageapp">
    <img src="https://www.flaticon.com/svg/vstatic/svg/715/715563.svg?token=exp=1610966478~hmac=4ca47f5eb0a4a3f483f1728ca82f302a" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Storage App</h3>

  <p align="center">
    Local Storage With Web Interface | Cloud Storage when deployed
  </p>
</p>

## About The Project

This project acts as a file manager with a web interface, wired to REST API Framework, powered by Django. It can act as a cloud file storage when deployed on a development server.

### Built With

These are the major frameworks that I built this project using.

- [Django](https://www.djangoproject.com)
- [Django REST Framework](https://django-rest-framework.com)
- [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html)
- [Bootstrap](https://getbootstrap.com)
- [JQuery](https://jquery.com)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running, follow these simple example steps.

### Prerequisites

- django

  ```sh
  pip install django
  ```

- django REST framework
  ```sh
  pip install djangorestframework
  ```
- django CORS header
  ```sh
  pip install django-cors-headers
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/porcelaincode/storageapp.git
   ```
2. Create your own superuser
   ```sh
   python manage.py createsuperuser
   ```
3. Migrate all the changes
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run `manage.py` file
   ```sh
   python manage.py runserver
   ```

## Usage

This project can be pushed on your trusted hosting server or any production server and used as your own cloud storage facility. On your local machine it acts as any normal file manager with a web interface.

_To add any REST API functionalities, please refer to the [Django REST Framework](https://www.django-rest-framework.org)_

## Contact

Your Name - [@\_vatsalpandya](https://twitter.com/_vatsalpandya)

Project Link: [https://github.com/porcelaincode/storageapp](https://github.com/porcelaincode/storageap)
