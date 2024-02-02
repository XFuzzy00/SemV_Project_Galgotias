from django.shortcuts import render
from .data import price_ticker, generate_candlestick_chart, prediction_chart


# Create your views here.
def main_render(request):
    
    stock_price1, change1, p_change1 = price_ticker('BTC-USD')
    stock_price2, change2, p_change2 = price_ticker('ETH-USD')
    stock_price3, change3, p_change3 = price_ticker('BNB-USD')
    stock_price4, change4, p_change4 = price_ticker('NVDA')
    stock_price5, change5, p_change5 = price_ticker('HPQ')
    stock_price6, change6, p_change6 = price_ticker('ADSK')
    stock_price7, change7, p_change7 = price_ticker('SHOT')
    stock_price8, change8, p_change8 = price_ticker('JWN')

    data = {}

    crypto = {
        'name1' : "Bitcoin", 'Symbol1' : 'BTC-USD', 'price1' : stock_price1, 'change1' : change1, 'percent1' : p_change1,
        'name2' : "Ethereum", 'Symbol2' : 'ETH-USD', 'price2' : stock_price2, 'change2' : change2, 'percent2' : p_change2,
        'name3' : "BNB USD", 'Symbol3' : 'BNB-USD', 'price3' : stock_price3, 'change3' : change3, 'percent3' : p_change3
    }

    trending_data = {
        'name4' : "NVIDIA Corporation", 'Symbol4' : 'NVDA', 'price4' : stock_price4, 'change4' : change4, 'percent4' : p_change4,
        'name5' : "HP Inc.", 'Symbol5' : 'HPQ', 'price5' : stock_price5, 'change5' : change5, 'percent5' : p_change5,
        'name6' : "Autodesk, Inc.", 'Symbol6' : 'ADSK', 'price6' : stock_price6, 'change6' : change6, 'percent6' : p_change6,
        'name7' : "Safety Shot, Inc.", 'Symbol7' : 'SHOT', 'price7' : stock_price7, 'change7' : change7, 'percent7' : p_change7,
        'name8' : "Nordstrom, Inc.", 'Symbol8' : 'JWN', 'price8' : stock_price8, 'change8' : change8, 'percent8' : p_change8,
    }
    data.update(crypto)
    data.update(trending_data)

    return render(request, "index.html", data)

def stocks_render(request):

    stock_price1, change1, p_change1 = price_ticker('BTC-USD')
    stock_price2, change2, p_change2 = price_ticker('ETH-USD')
    stock_price3, change3, p_change3 = price_ticker('BNB-USD')
    stock_price4, change4, p_change4 = price_ticker('STNE')
    stock_price5, change5, p_change5 = price_ticker('LOW')
    stock_price6, change6, p_change6 = price_ticker('SOL-USD')
    stock_price7, change7, p_change7 = price_ticker('AVAX-USD')
    stock_price8, change8, p_change8 = price_ticker('SYM')
    stock_price9, change9, p_change9 = price_ticker('XOM')
    stock_price10, change10, p_change10 = price_ticker('CRSP')

    crypto = {
        'name1' : "Bitcoin", 'Symbol1' : 'BTC-USD', 'price1' : stock_price1, 'change1' : change1, 'percent1' : p_change1,
        'name2' : "Ethereum", 'Symbol2' : 'ETH-USD', 'price2' : stock_price2, 'change2' : change2, 'percent2' : p_change2,
        'name3' : "BNB USD", 'Symbol3' : 'BNB-USD', 'price3' : stock_price3, 'change3' : change3, 'percent3' : p_change3,
        'name4' : "StoneCo. Ltd.", 'Symbol4' : 'STNE', 'price4' : stock_price4, 'change4' : change3, 'percent4' : p_change3,
        'name5' : "Lowe's Companies, Inc.", 'Symbol5' : 'LOW', 'price5' : stock_price5, 'change5' : change3, 'percent5' : p_change3,
        'name6' : "Solana USD", 'Symbol6' : 'SOL-USD', 'price6' : stock_price6, 'change6' : change3, 'percent6' : p_change3,
        'name7' : "Avalanche USD", 'Symbol7' : 'AVAX-USD', 'price7' : stock_price7, 'change7' : change3, 'percent7' : p_change3,
        'name8' : "Symbotic Inc.", 'Symbol8' : 'SYM', 'price8' : stock_price8, 'change8' : change3, 'percent8' : p_change3,
        'name9' : "Exxon Mobil Corporation", 'Symbol9' : 'XOM', 'price9' : stock_price9, 'change9' : change3, 'percent9' : p_change3,
        'name10' : "CRISPR Therapeutics AG", 'Symbol10' : 'CRSP', 'price10' : stock_price10, 'change10' : change3, 'percent10' : p_change3,
    }

    return render(request, "stocks.html", crypto)

def bitcoin_render(request):

    candlestick_chart, df_html = generate_candlestick_chart('BTC-USD')
    chart_json = candlestick_chart.to_json()
    
    pred_chart = prediction_chart('BTC-USD')
    prediction_chart_json = pred_chart.to_json()

    return render(request, "bitcoin.html", {'chart_json': chart_json, 'df_html': df_html, 'prediction_chart_json': prediction_chart_json})

def Ethereum_render(request):

    candlestick_chart, df_html = generate_candlestick_chart('ETH-USD')
    chart_json = candlestick_chart.to_json()
    
    pred_chart = prediction_chart('ETH-USD')
    prediction_chart_json = pred_chart.to_json()

    return render(request, "ethereum.html", {'chart_json': chart_json, 'df_html': df_html, 'prediction_chart_json': prediction_chart_json})

def bnb_render(request):

    candlestick_chart, df_html = generate_candlestick_chart('BNB-USD')
    chart_json = candlestick_chart.to_json()
    
    pred_chart = prediction_chart('BNB-USD')
    prediction_chart_json = pred_chart.to_json()

    return render(request, "bnb.html", {'chart_json': chart_json, 'df_html': df_html, 'prediction_chart_json': prediction_chart_json})

def about_us_render(request):
    return render(request, "about-us.html")

def hire_a_broker(request):
    return render(request, "hire-a-broker.html")

