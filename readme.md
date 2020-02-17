# Konrad Karimi zaliczenie z Przetwarzania Obrazów

Repozytorium zawierające rozwiązanie zadań z przedmiotu __Przetwarzanie Obrazów__

> **Zestaw zadań __9__**


### Prerequisites / Wymagania wstępne

What things you need to install the software and how to install them

Install **Python** >= 3.4

Check `Python` installation
```
python3 --version
pip3 --version
virtualenv --version
```

### Installing / Instalacja

Create `Virtualenv`
```
python3 -m venv /path/to/new/virtual/environment

# for windows
python -m venv c:\path\to\myenv
```

Activate `Virtualenv`
```
source ./venv/bin/activate  # sh, bash, ksh, or zsh

# on windows
myenv\Scripts\activate.bat
```
Install reqiurements
```
pip install --upgrage pip
pip install -r requirements.txt
pip list # shows installed packages
```
This should install all needed in this project python packages.

To exit `Virtualenv`
```
deactivate
```

**Now it's ready to start!**

## Running the scripts / Uruchamianie skryptów

1. Make sure you have active `Virtualenv`
2. Run the script using python:
```
python KonradKarimi_Inf4_NStac_ZadA.py --path_to_mat_file="./Signal9.mat"
```

```
python KonradKarimi_Inf4_NStac_ZadB.py --path_to_image="./son1.GIF" --brightness=2
```
> ***Both scripts got adjustable parameters***
```
#Only on script A
--path_to_mat_file="HERE GOES FILENAME" 

#Only on script B
--path_to_image="HERE GOES FILENAME"
--brightness=2 #integer value
```


## Authors

* **Konrad Karimi** - [KonradKarimi](https://github.com/KonradKarimi)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.