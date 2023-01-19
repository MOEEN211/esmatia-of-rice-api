Steps to run this project on local(For Windows):

1. Create virtual environment:
    py -m venv venv

2. Activate environment:
   .\venv\Scripts\activate

3. Install req.txt:
    pip insall -r requirement.txt

4. Then:
    py manage.py makemigrations
    py manage.py migrate

5. For runing server:
    py manage.py runserver