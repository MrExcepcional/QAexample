# Document Signing Test
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg?style=for-the-badge&logo=appveyor)](https://www.python.org/downloads/release/python-392/)

This library is a solved code challenge to implement a multi-browser signature validation test. Following instructions have Ubuntu linux in mind.

## 📦 Installation

Use of python3.9 recommended. You can find it [here.](https://www.python.org/downloads/release/python-392/)
Is a good practice to use a virtualenv. [Here is a guide.](https://pythonbasics.org/virtualenv/)
For Internet Explorer we use BrowserStack. Create your free account [here.](https://www.browserstack.com/automate)

Download and unzip file. Edit run_on_three_browsers.sh.template replacing USER and KEY placeholders with your BrowserStack crendentials. Save it as run_on_three_browsers.sh

Install requirements
```bash
pip install -r requirements.txt
```

## 🚀 How to use

Navigate inside the unzipped folder.
In command line run with the desired browser (Chrome, Firefox, IE).
```bash
BROWSER=Chrome python3.9 -m unittest discover
```
Remember to pass your browserStack credentials if you test IE11
```bash
BROWSER=IE USER=yourUserHere KEY=yourKeyHere python3.9 -m unittest discover
```

If you prefer, you can use the included bash script to run all three browsers in parallel.
```bash
bash run_on_three_browsers.sh
```

Also works with...
```bash
chmod +x run_on_three_browsers.sh
./run_on_three_browsers.sh
```