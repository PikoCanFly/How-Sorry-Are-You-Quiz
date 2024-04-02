

# Django-How-Sorry-Are-You-Quiz


## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Support](#support)
6. [Contributing](#contributing)



## Introduction


This repository contains the source code for a Quiz Application Created With Django.

 [YouTube tutorial]((https://www.youtube.com/watch?v=s0aCEXg3ct4)). 


[![Django Authentication Tutorial Thumbnail](https://img.youtube.com/vi/s0aCEXg3ct4/0.jpg)](https://www.youtube.com/watch?v=s0aCEXg3ct4)

In this tutorial we build a Quiz App using Django to quantify how sorry the people who upset us are.




## Installation


To get started with the project, follow these steps:

1. **Clone the Repository**: Use Git to clone the project repository to your local machine: 
```
git clone <repository-url>
```

- Replace `<repository-url>` with the URL of the GitHub repository:


2. **Navigate to the Project Directory**: Move into the project directory: 
```
cd <project-directory>
```

- Replace `<project-directory>` with the name of the directory created during cloning.

3. **Set Up Virtual Environment**: Create a virtual environment for the project: 
```
python -m venv env
```

- Activate the virtual environment:

- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS and Linux:

  ```
  source env/bin/activate
  ```

4. **Install Dependencies**: Install project dependencies using pip:
```
pip install -r requirements.txt
```


## Configuration


Before running the project, make sure to configure the necessary settings:

1. **Environment Variables**: Update the `.env` file with your configuration settings, such as email address and password.

2. **Database Migrations**: Apply database migrations using the following command:

```
python manage.py migrate
```

## Usage

Once the project is set up and configured, you can run it using the following command:

```
python manage.py runserver
```

Access the development server at `http://localhost:8000/` in your web browser.


## Support

If you found this project helpful, consider becoming a patron on my Patreon:

[![Support me on Patreon](https://img.shields.io/badge/Support%20me%20on-Patreon-orange.svg)](https://www.patreon.com/PikoCanFly)

Your contributions will help me continue creating helpful content. Thank you for your support!

## Contributing

This project was made to help spread knowledge. If you'd like to contribute, feel free to fork the repository, make your changes, and submit a pull request.

