## Install

### Python paquet manager

```bash
apt install python3-pip
```

### Install dependencies

```bash
pip3 install python-telegram-bot RPi.GPIO
```

### Copy Service & Register

```bash
cp disruptdoor.service /etc/systemd/system/
systemctl daemon-reload
```

### Copy Service

```bash
cp disruptdoor.service /etc/systemd/system/
```

### Copy app

```bash
mkdir /usr/local/lib/disruptdoor/ && cp main.py /usr/local/lib/disruptdoor/
```
