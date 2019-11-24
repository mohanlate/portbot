from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from .models import Portfolio,Stock
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

# Create your views here.


def index(request):
    portfolioInvestmentValue = 0
    data = pd.DataFrame()
    today = date.today()
    print(today.strftime("%Y/%m/%d"))

    portfolios = Portfolio.objects.all()
    portfolio_id = request.GET["portfolio_id"]
    stocks = Stock.objects.filter(portfolio_id =portfolio_id)

    for stock in stocks:
        stock.investmentAmount = round((stock.quantity*stock.buyRate),2)
        portfolioInvestmentValue += stock.investmentAmount
        data = wb.DataReader(stock.ticker, data_source='yahoo', start=today.strftime("%Y/%m/%d"))['Adj Close']
        stock.cmp = round((data[0]),2)


    for stock in stocks:
        stock.weight = round((stock.investmentAmount/portfolioInvestmentValue * 100),2)
        stock.expRet = round((((stock.target-stock.buyRate)/stock.buyRate) * 100),2)


    my_context = {
        'portfolios': portfolios,
        'stocks': stocks,
        'portfolioInvestmentValue' : round(portfolioInvestmentValue, 2)
    }

    return render(request, 'index.html', my_context)


def addStock(request):
    return HttpResponse('Add new stock here')


