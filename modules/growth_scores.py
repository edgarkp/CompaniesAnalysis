def growth_score(netSales, EPS):
    "'This function evaluates a growth score using as inputs the net sales and earning per share on 6 years'" 
    "'The current year being n, data are taken from n-3 to n+2 so that previous, current and future info are already integrated in the score'"
    "'The data are supposed to be on format : data = [data(n-3) data(n-2) data(n-1) data(n) data(n+1) data(n+2)'"

    # 1st step : Compute the rate for each quantity
    rateNetSales = netSales.pct_change(axis = 'columns').dropna(axis = 'columns')
    rateEPS = EPS.pct_change(axis = 'columns').dropna(axis = 'columns')

    # 2nd step: Compute the gross and mean rates
    grossRateNetSales = (netSales.iloc[:, 5] - netSales.iloc[:, 1])/ netSales.iloc[:, 1]
    grossRateNetSales = grossRateNetSales.values[0]
    meanRateNetSales = rateNetSales.values[0].mean()
    grossRateEPS = (EPS.iloc[:, 5] - EPS.iloc[:, 1])/ EPS.iloc[:, 1]
    grossRateEPS = grossRateEPS.values[0]
    meanRateEPS = rateEPS.values[0].mean()

    # 3rd step: Calculate different scores
    Score1NetSales = sum([rate>0 for rate in rateNetSales.values[0]])
    Score1EPS = sum([rate>0 for rate in rateEPS.values[0]])

    if grossRateNetSales < 0 :
        Score2NetSales = 0
    elif grossRateNetSales < 0.05 :
        Score2NetSales = 50*grossRateNetSales
    else:
        Score2NetSales = 2.5

    if grossRateEPS < 0 :
        Score2EPS = 0
    elif grossRateEPS < 0.05 :
        Score2EPS = 50*grossRateEPS
    else:
        Score2EPS = 2.5

    if meanRateNetSales < 0 :
        Score3NetSales = 0
    elif meanRateNetSales < 0.25 :
        Score3NetSales = 10*meanRateNetSales
    else:
        Score3NetSales = 2.5

    if meanRateEPS < 0 :
        Score3EPS = 0
    elif meanRateEPS < 0.25 :
        Score3EPS = 10*meanRateEPS
    else:
        Score3EPS = 2.5
    
    # 4th step: Calculate the total score
    ScoreNetSales = Score3NetSales + Score2NetSales + Score1NetSales
    ScoreEPS = Score3EPS + Score2EPS + Score1EPS

    return 0.6*ScoreNetSales + 0.4*ScoreEPS

def profitability_score(ROE, netMargin) :
     "'This function evaluates a profitability score using as ROE and Net margin on 6 years'" 
     "'The current year being n, data are taken from n-3 to n+2 so that previous, current and future info are already integrated in the score'"
     "'The data are supposed to be on format : data = [data(n-3) data(n-2) data(n-1) data(n) data(n+1) data(n+2)'"

     # 1st step: Calculate the different rates
     rateROE = ROE.pct_change(axis = 'columns').dropna(axis = 'columns')
     rateNetMargin = netMargin.pct_change(axis = 'columns').dropna(axis = 'columns')

     # 2nd step: Calculate the main score for each quantity
     advantage1ROE = sum([1 for roe in ROE.values[0] if roe >= 0.1 ])
     advantage1NetMargin = sum([1 for nm in netMargin.values[0] if nm >= 0.1 ])

     adjustRatioROE = 6/len(ROE.dropna(axis = 'columns').values[0])
     adjustRatioNetMargin = 6/len(netMargin.dropna(axis = 'columns').values[0])

     Score_main_ROE = 8-1.2*(6-adjustRatioROE*advantage1ROE)
     Score_main_netMargin = 8-1.2*(6-adjustRatioNetMargin*advantage1NetMargin)

     # 3rd step: Calculate the bonus score for each quantity
     advantage2ROE = sum([1 for rate_roe in rateROE.values[0] if rate_roe >= 0 ])
     advantage2NetMargin = sum([1 for rate_nm in rateNetMargin.values[0] if rate_nm >= 0 ])

     adjustRatioRateROE = 5/len(rateROE.dropna(axis = 'columns').values[0])
     adjustRatioRateNetMargin = 5/len(rateNetMargin.dropna(axis = 'columns').values[0])

     Score_bonus_ROE = 2-0.2*(5-adjustRatioRateROE*advantage2ROE)
     Score_bonus_netMargin = 2-0.2*(5-adjustRatioRateNetMargin*advantage2NetMargin)

     # 4th step: Calculate the final score
     Score_ROE = Score_main_ROE + Score_bonus_ROE
     Score_netMargin = Score_main_netMargin + Score_bonus_netMargin
    
     print(Score_main_ROE)
     print(Score_bonus_ROE)
     print(Score_main_netMargin)
     print(Score_bonus_netMargin)
     return (Score_ROE + Score_netMargin)/2


