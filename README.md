# TokenSharing
Program that gives tokens to users and save it in database

# Team
Asanuly Alikhan - main 'login' and 'protected' functions 

Malikov Alan - Database and coonection it to the python, little part of 'login' functions

Kurmangali Sanzhar - part of database connection and test.py folder, little part of 'protected' functions

# Installation
Firstly, you need to download 'Flask' 
using
```bash
pip install Flask
```
Secondly, you need to download 'Flask-SQLAlchemy' 
```bash
pip install Flask-SQLAlchemy
```
Thirdly, you need to download 'pyjwt'
```bash
pip install pyjwt
```
# Usage
Run test.py from test folder, use a direcory to the folder test and run it with this command in cmd or other termianls (src and test folders should be lockated in one package)
``` bash
python test.py
```
Alternative is taking python files from src and use it by your own or copy code and use it. 
# Examples
You need to login and give a password, it will give a token, after that you need to write in URL place '\protected?token='given token'' and program will save it in Postresql table.

``` bash
WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\sqlac\env\lib\site-packages\flask_sqlalchemy\__init__.py:872: 
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  
Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
 * Debugger is active!
 * Debugger PIN: 841-538-525
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
You need to go by link: 
``` bash
//127.0.0.1:5000/
```
After that register:
![Снимок экрана (1042)](https://user-images.githubusercontent.com/77801087/139111440-fb8c4fd8-82e5-472c-8199-53c6c4701f23.png)
Result(in http):
![photo_2021-10-27_21-55-55](https://user-images.githubusercontent.com/77801087/139102967-ff638160-6371-4917-9571-d362d69ac5a5.jpg)
Enter token in protected and program will give message:
![photo_2021-10-27_22-56-25](https://user-images.githubusercontent.com/77801087/139112145-4ec1fa2c-4ecb-45f5-b460-682603ff7018.jpg)
Result in postgresSql:
![photo_2021-10-27_22-10-47](https://user-images.githubusercontent.com/77801087/139105073-5ded2bef-e028-4c88-9318-6674f3ee8dbe.jpg)

# License
[MIT](https://choosealicense.com/licenses/mit/)
