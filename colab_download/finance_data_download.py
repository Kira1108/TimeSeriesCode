# -*- coding: utf-8 -*-
"""Finance Data Download.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mbji8ydFSP1ifyIK0g3TacgeVBeCFQ9j
"""

!pip install yfinance

!git clone https://github.com/lazyprogrammer/financial_engineering.git

!python ./financial_engineering/get_data.py

!python /content/financial_engineering/append.py

!python /content/financial_engineering/append_small.py

!cp -R ./data /content/drive/MyDrive/finance_data/stocks

!cp sp500full.csv /content/drive/MyDrive/finance_data/stocks/sp500full.csv

!cp sp500sub.csv /content/drive/MyDrive/finance_data/stocks/sp500sub.csv