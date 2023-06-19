# Installation Guide
- Install latest node version
https://nodejs.org/dist/v16.20.0/node-v16.20.0-x64.msi
- Install latest python version
https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe

- Install pip to manage python packages
* `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
* `python get-pip.py`

- install node packages
run `npm install`
- install python libraries
run `pip install discord`
    `pip install selenium`
    `pip install dotenv`
    `pip install numpy`
    `pip install json`
- Setup environment
`C:\Program Files\Google\Chrome\Application` Run command prompt here.
Run `chrome.exe --remote-debugging-port=9014 --user-data-dir=C:\Selenium\Chrome_Test_Profile` in console
Setup wallet extension on your browser and login with the wallet(subscription wallet) on dextools

# Run
- Run `npm start`
- To reset database, use `/reset` slash command