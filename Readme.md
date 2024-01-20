Ghost question bot

# Installation

## Install python env and libraries

- In Windows:
    ```shell
    $ pip install virtualenv
    $ python -m venv venv
    $ venv/Scripts/activate
    $ pip install -r requirements.txt
    ```

- In Linux (like Ubuntu, Debian):
    ```shell
    $ sudo apt install python3.11 python3-pip python3.11-venv
    $ python3 -m pip install virtualenv
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```

## Configurate `.env` values
Copy from `.env.example` file and create `.env` file.
```shell
$ cp .env.example .env
```

Edit `.env` file values
```shell
$ nano .env
```
Values:
 - `BOT_TOKEN` - Bot token from [@botfather](https://t.me/botfather)
 - `DEBUG` - boolean True or False for debugging
 - `ADMINS` - list[int] bot admins's telegram id number
 - `DB_URL` - Database connection URL like postgresql or mysql (sqlite3 has asynchronous queries problem)
 - `USE_REDIS` - boolean: True or False if True use `redis` for caching
 - `REDIS_DB` - `redis` database number (if USE_REDIS is True)
 - `REDIS_PASSWORD` - `redis` database password (if USE_REDIS is True)

## Configure Database
Install and configure Postgresql or MySQL. Create schemas using these commands:
```shell
$ aerich init -t settings.TORTOISE_ORM
$ aerich init-db
```
Migrations:
```shell
$ aerich migrate
$ aerich upgrade
```

## Configure i18n
### Step1: Extract messages
Extract messages:
```shel
$ pybabel extract  --input-dirs=. --ignore-dirs=venv -o locales/messages.pot --project=GhostQuestionBot --version=1.0
```
Here is `--input-dirs=.` - path to code and the `locales/messages.pot` is template where _messages_ will be extracted and messages is translation domain.

> [!NOTE]  
> Some useful options:
> 
> Extract texts with pluralization support -k __:1,2
> 
> Add comments for translators, you can use another tag if you want (TR) --add-comments=NOTE
> 
> Disable comments with string location in code --no-location
> 
> Set project name --project=MySuperBot
> 
> Set version --version=2.2


### Step2: Init languages
```shell
$ pybabel init -i locales/messages.pot -d locales -D messages -l en
```
 - -i locales/messages.pot - pre-generated template
 - -d locales - translations directory
 - -D messages - translations domain
 - -l en - language. Can be changed to any other valid language code (For example -l ru for russian language)

### Step3: Translate texts
To open .po file you can use basic text editor or any PO editor, e.g. [Poedit](https://poedit.net/)

Just open the file named `locales/{language}/LC_MESSAGES/messages.po` and write translations

### Step4: Compile translations
```shell
$ pybabel compile -d locales -D messages
```

### Step5: Updating messages
When you change the code of your bot you need to update po & mo files
- Step 5.1: regenerate pot file: command from step 1
- Step 5.2: update po files
    ```shell
    $ pybabel update -d locales -D messages -i locales/messages.pot
    ```
- Step 5.3: update your translations: location and tools you know from step 3
- Step 5.4: compile mo files: command from step 4

# Running bot
Running bot using this command:
```shell
$ python main.py
```
____________

&copy; Murodillo 2024   