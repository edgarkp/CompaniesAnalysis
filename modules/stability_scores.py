def debt_score(debt, Equities, EBITDA):
    "'This function evaluates a debt score using as inputs the debt, on the actual year'" 
    "'The current year being n, data are taken from n-3 to n+2 so that previous, current and future info are already integrated in the score'"

    # 1st step : Calculate the different leverages
    op_leverage = debt/EBITDA
    eq_leverage = Equities/debt

    # 2nd step: Calculate the scores
    if debt == 0 :
        score_op = 10
    else :
        score_op = max(10 - 1.8*op_leverage, 0)

    if debt == 0 :
        score_eq = 10
    else :
        score_eq = min(1 + 1.8*eq_leverage, 10)

    # 3rd step: Calculate the final score
    return 0.4*score_op + 0.6*score_eq


def valuation_score(PER, historicalPER, PBR, PCF, PEG):
    "'This function evaluates a valuation ratio score using as inputs :'"
    "' PER: Price to Earning Ratio and its historical PER'" 
    "' PBR: Price to Book Ratio'"
    "' PCF: Price Cash Flow"
    "' PEG: Price Earnings Growth"
    "'The current year being n, data are taken from n-3 to n+2 (except for the historical PER) so that previous, current and future info are already integrated in the score'"
    "'The data are supposed to be on format : data = [data(n-3) data(n-2) data(n-1) data(n) data(n+1) data(n+2)'"

    # 1st step : Calculate additional inputs : the Graham Ratio & the mean PER & input values at current year
    GR = PER.values[0]*PBR.values[0]
    currentGR = GR[3]
    
    meanPER = PER.values[0].mean()
    currentPER = PER.iloc[:, 3].values[0]
    currentPBR = PBR.iloc[:, 3].values[0]
    currentPCF = PCF.iloc[:, 3].values[0]
    PEG5years = PEG.iloc[:,1:]

    # 2nd step: Calculate the different scores
    ## 1 - score on the mean PER wrt historical PER
    if meanPER > 2*historicalPER :
        score1 = 0
    elif (meanPER >= historicalPER) & (meanPER <= 2*historicalPER) :
        score1 = 2 - (meanPER/historicalPER)
    else :
        score1 = 1

    ## 2- score on current PER wrt historical PER
    if currentPER < 0 :
        score2 = 0
    elif currentPER > 2*historicalPER :
        score2 = 0
    elif (currentPER >= historicalPER) & (currentPER <= 2*historicalPER) :
        score2 = 2 - (currentPER/historicalPER)
    else :
        score2 = 1

    ## 3- score on current PER in general
    if currentPER <= 3 or currentPER >=20 :
        score3 = 0
    else: 
        score3 = 1

    ## 4- score on PBR
    if currentPBR >= 4 :
        score4 = 0
    else: 
        score4 = 1

    ## 5- score on PCF
    if currentPCF == 3 or currentPCF >=8 :
        score5 = 0
    else: 
        score5 = 1

    ## 6- score on Graham ratio
    if (currentGR <= 0) or (currentGR >= 40):
        score6 = 0
    elif currentGR <= 22.5 :
        score6 = 2.5
    else :
        score6 = ((2.5 - 0)/(22.5 - 40))*(currentGR-40)
    
    ## 7- score on PEG
    adjustRatio = 5/len(PEG5years.values[0])
    penalty1PEG = sum([0 if (0 < peg <= 4) else 1 for peg in PEG5years.values[0] ])
    penalty2PEG = sum([1 if (2 <= peg < 4) else 0 for peg in PEG5years.values[0] ])
    score7 = 2.5 - adjustRatio*(0.5*penalty1PEG + 0.2*penalty2PEG)

    # 3rd step: Calculate the different scores
    return score1 + score2 + score3 + score4 + score5 + score6 + score7

def additional_assessment(PER, sectorialPER, PBR):
    currentPER = PER.iloc[:, 3].values[0]
    currentPBR = PBR.iloc[:, 3].values[0]

    if currentPER > sectorialPER :
        sectorPositionKPI = 'OK'
    else :
        sectorPositionKPI = 'NOK'

    if currentPBR > 1 :
        intrisicPriceKPI = 'NOK'
    else :
        intrisicPriceKPI = 'OK'

    return [sectorPositionKPI, intrisicPriceKPI]
    