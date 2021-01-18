<br />
<p align="center">
  <a href="https://github.com/porcelaincode/storageapp">
  <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" fill="currentColor" class="bi bi-folder" viewBox="0 0 16 16">
    <path d="M.54 3.87L.5 3a2 2 0 0 1 2-2h3.672a2 2 0 0 1 1.414.586l.828.828A2 2 0 0 0 9.828 3h3.982a2 2 0 0 1 1.992 2.181l-.637 7A2 2 0 0 1 13.174 14H2.826a2 2 0 0 1-1.991-1.819l-.637-7a1.99 1.99 0 0 1 .342-1.31zM2.19 4a1 1 0 0 0-.996 1.09l.637 7a1 1 0 0 0 .995.91h10.348a1 1 0 0 0 .995-.91l.637-7A1 1 0 0 0 13.81 4H2.19zm4.69-1.707A1 1 0 0 0 6.172 2H2.5a1 1 0 0 0-1 .981l.006.139C1.72 3.042 1.95 3 2.19 3h5.396l-.707-.707z"/>
</svg>
  </a>

  <h3 align="center">Storage App</h3>

  <p align="center">
    Local Storage | Cloud Storage when deployed
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
