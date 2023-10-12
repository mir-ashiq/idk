# Instructions for preparing to start auto-output
For the scripts to work, you need to download and install Python 3.10.10
Download python 3.10.10 https://www.python.org/downloads/
https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe
Download studio https://visualstudio.microsoft.com/ru/downloads/
https://aka.ms/vs/17/release/vs_BuildTools.exe

For the scripts to work, you need to download and install Python
To install components:
1. You need to open CMD
2. Go to the directory where you unpacked the archive with scripts, using the command: cd path
3. Run of the commands:
pip install --upgrade pip
pip install -r requirements.txt

If there is an error when installing hd-wallet, download Microsoft C++ Build Tools

In the wallets folder, you need to put your files ".txt" with seed phrases or privatekey. 
The anti-public concept works in the script, 
therefore, after the first launch and complete addition of addresses and private keys to the Database, 
delete the files from the wallets folder.

Database base.db is created automatically in the directory with all scripts in its absence,
if it has already been created, it will be checked with new files in the wallets folder,
by obtaining addresses and private keys from seed phrases.

The settings are set in the script config.py
To run the scripts, you need to run the script main.py

# Инструкция для подготовки к запуску авто-вывода  от https://t.me/OpenToo1s

Для работы скриптов, необходимо скачать и установить Python 3.10.10
Во время установки поставить галочку Add Python.exe to PATH.
Download python 3.10.10 https://www.python.org/downloads/
https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe
Download studio https://visualstudio.microsoft.com/ru/downloads/
https://aka.ms/vs/17/release/vs_BuildTools.exe

Для установки компонентов:
1. Необходимо открыть CMD
2. Перейти в директорию куда распаковали архив со скриптами, при помощи команды: cd путь (в пути не должно быть кириллицы)
3. Выполнить команды:
pip install --upgrade pip
pip install -r requirements.txt

Если при установке hd-wallet ошибка, скачайте Microsoft C++ Build Tools

В папку wallets, необходимо поместить ваши файлы ".txt" с seed фразами или privatekey. 
В скрипте работает принцип анти-паблика, 
поэтому после первого запуска и полного добавления в Базу данных адресов и приватных ключей, 
удалите файлы из папки wallets.

База данных base.db создается автоматически в директории со всеми скриптами при ее отсутсвии, 
если она уже создана, то будет идти сверка с новыми файлами в папке wallets, 
путем получения из seed фраз адресов и приватных ключей.

Настройки задаются в скрипте config.py
Для запуска работы cофта, необходимо запустить скрипт main.py

