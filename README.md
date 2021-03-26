Scrummage
=========

Utils to extract and analyse scrum data.

[Trello API Docs](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)

---

Running the Backend Locally
---------------------------

1. Clone the repo
    ``` 
    $ git clone 
    ```

2. Install the requirements
    ```
    (venv) $ pip install backend/scrummage/requirements.txt
    ```

3. Run migrations
    ```
    # cd scrummage/backend
    (venv) $ ./manage.py migrate
    ```

4. Create superuser
    ```
    # cd scrummage/backend
    (venv) $ ./manage.py createsuperuser
    ```

5. Run development server
    ```
    # cd scrummage/backend
    (venv) $ ./manage.py runserver
    ```
