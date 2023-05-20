def yield_score(dividendYield):
    "'This function evaluates a yield score using as inputs the yield on 6 years'" 
    "'The current year being n, data are taken from n-3 to n+2 so that previous, current and future info are already integrated in the score'"
    "'The data are supposed to be on format : data = [data(n-3) data(n-2) data(n-1) data(n) data(n+1) data(n+2)'"

    # 1st step : Compute the rate and its mean
    rateYield = dividendYield.pct_change(axis = 'columns').dropna(axis = 'columns')
    meanRateYield = rateYield.values[0].mean()

    # 2nd step: Calculate the bonus score
    if meanRateYield < 0:
        Score_bonus = 0
    elif meanRateYield < 0.02 :
        Score_bonus = 1
    else :
        Score_bonus = 2
    
    # 3rd step: Calculate the main score
    penalty1 = sum([1 for dividend in dividendYield.values[0] if dividend >= 0.04 if dividend <= 0.06 ])
    penalty2 = sum([1 for dividend in dividendYield.values[0] if dividend < 0.04 ])
    adjustRatio = 6/len(dividendYield.dropna(axis = 'columns').values[0])
    Score_main = 8 - adjustRatio*(0.25*penalty1 + 0.75*penalty2)
    
    # 4th step: Calculate the total score
    return Score_main + Score_bonus


def payout_ratio_score(payoutRatio):
    "'This function evaluates a payout ratio score using as inputs the payout ratio on 6 years'" 
    "'The current year being n, data are taken from n-3 to n+2 so that previous, current and future info are already integrated in the score'"
    "'The data are supposed to be on format : data = [data(n-3) data(n-2) data(n-1) data(n) data(n+1) data(n+2)'"

    penalty1 = sum([1 for pr in payoutRatio.values[0] if pr >= 0.5 if pr <= 0.75 ])
    penalty2 = sum([1 for pr in payoutRatio.values[0] if pr > 0.75])
    adjustRatio = 6/len(payoutRatio.dropna(axis = 'columns').values[0])
    Score_main = 10 - adjustRatio*(penalty1 + 1.5*penalty2)
    
    return Score_main 