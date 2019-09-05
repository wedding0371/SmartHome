# 安装 Domoticz



## 安装Domoticz主体

```
    sudo apt-get install curl -y
    sudo curl -L install.domoticz.cn | sudo bash
    # sudo curl -L -k install.domoticz.cn | sudo bash
    wget http://ftp.nl.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u8_armhf.deb
    sudo dpkg -i libssl1.0.0_1.0.1t-1+deb8u8_armhf.deb
    # sudo iptables -I INPUT -i eth0 -p tcp --dport 23334 -j ACCEPT          # 可能不用
    # sudo iptables  -I OUTPUT -o eth0 -p tcp --sport 23334 -j ACCEPT        # 可能不用
    cd domoticz/
    sudo  ./domoticz
    sudo service domoticz.sh start     # 开机自启
    sudo reboot
```
## 安装homebridge\-edomoticz

```
    sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
    sudo apt-get install -y nodejs
    sudo apt-get install npm -y
    sudo apt-get install libavahi-compat-libdnssd-dev -y
    sudo npm install -g --unsafe-perm homebridge hap-nodejs node-gyp
    cd /usr/local/lib/node_modules/homebridge/
    sudo npm install --unsafe-perm bignum

    cd /usr/lib/node_modules/hap-nodejs/node_modules/mdns
    sudo node-gyp BUILDTYPE=Release rebuild

    cd ~
    sudo npm install -g homebridge-homeassistant
    sudo nano /home/pi/.homebridge/config.json
        {
            "bridge": {
                "name": "Homebridge",
                "username": "B8:27:EB:77:2E:7D",        # ip mac
                "port": 51826,
                "pin": "031-45-154"
            },

            "description": "Configuration file for (e)xtended Domoticz platform.",
            "platforms": [
                {
                    "platform": "eDomoticz",
                    "name": "eDomoticz",
                    "server": "127.0.0.1",
                    "port": "1234",                        # port: 23334
                    "ssl": 0,
                    "roomid": 2,
                    "mqtt": 1
                }
            ],
            "accessories": []
        }
    sudo npm install -g homebridge-edomoticz
```

