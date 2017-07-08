# Setup

## python

use virtualenv.

```
# install virtualenv
sudo easy_install virtualenv

# init virtualenv
cd [PROJECT DIR]
virtualenv --no-site-packages fbad

# activate virtualenv
source fbad/bin/activate

# install pip
easy_install pip

# install modules
pip install -r packages.txt
```


## Auth

```
python init.py
```

## SQLite

```
sqlite3 fbad.db < sql/init.sql
```
