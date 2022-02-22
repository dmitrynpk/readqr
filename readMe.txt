1. Установим утилиту с помощью которой будем конвертировать PDF в JPG
sudo apt install imagemagick
2. Команда "convert -density 300 qr.pdf qr.jpg" сконвертирует PDF в JPG
Если конвертация работать не будет выполним команду "sudo 2sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml"
3. Установим библиотеки для Python3
sudo apt install python3-opencv
sudo apt-get install zbar-tools
pip3 install qrcode pyzbar numpy
4. Поместим в одну папку PDF файлы и скрипты "python convertPdfToJpg.py" и "python readqr.py"
5. Для конвертации PDF в JPG выполним команду "python convertPdfToJpg.py"
6. Для чтения кодов DataMatrix выполним команду "python readqr.py"
