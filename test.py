from modules.growth_scores import growth_score, profitability_score
from modules.dividend_scores import yield_score, payout_ratio_score
from modules.stability_scores import debt_score, valuation_score, additional_assessment
import pandas as pd

# growth Score
netSales = pd.DataFrame([[83049,	83044,	86849,	57139, 57546, 60559]], 
                         index = ['netSales'], 
                         columns=['2017','2018','2019','2020','2021','2022'])

EPS = pd.DataFrame([[7.29, 7.01, 6.32, 4.93, 5.61, 6.84]],
                    index = ['EPS'], 
                    columns=['2017','2018','2019','2020','2021','2022'])
scoreGrowth = growth_score(netSales, EPS)

# dividend scores
dividendYield = pd.DataFrame([[0.031,	0.0344,	0.0397,	0.0324,	0.0274,	0.0288]],
                    index = ['Yield'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

payoutRatio = pd.DataFrame([[0.51,	0.54,	0.62,	0.71,	0.64,	0.55]],
                    index = ['Payout ratio'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

scoreYield = yield_score(dividendYield)
scorePayoutRatio = payout_ratio_score(payoutRatio)

# Profitability score
ROE = pd.DataFrame([[0.1560,	0.1310,	0.1110,	0.0954,	0.1170,	0.1320]],
                    index = ['ROE'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

NetMargin = pd.DataFrame([[0.0728,	0.0699,	0.0596,	0.0705,	0.0798,	0.0909]],
                    index = ['Net Margin'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

scoreProfitability = profitability_score(ROE, NetMargin)

# Debt score
debt = 30526
Equities = 42257
EBITDA = 7601

scoreDebt = debt_score(debt, Equities, EBITDA)

# Valuation score
PER = pd.DataFrame([[16.4,	15.7,	15.5,	21.9,	23.3,	19.1]],
                    index = ['PER'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

historicalPER = 14.8
sectorialPER = 14.8*(48 / 45)

PBR = pd.DataFrame([[2.25,	1.98,	1.65,	2.39,	2.64,	2.48]],
                    index = ['PBR'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

PCF = pd.DataFrame([[13.82,	10.69,	9.51,	10.00,	14.43,	13.14]],
                    index = ['PCF'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

PEG = pd.DataFrame([[-4.09, -4.09,	-1.57, -1.43,	1.52,	1.00]], #the 1st value was artificial , generated, it's not real
                    index = ['PEG'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

scoreValuation = valuation_score(PER, historicalPER, PBR, PCF, PEG)
otherAss = additional_assessment(PER, sectorialPER, PBR)

print('Growth score:', scoreGrowth)
print('Dividend Yield score:', scoreYield)
print('Dividend payout ratio score:', scorePayoutRatio)
print('Profitability score:', scoreProfitability)
print('Debt score:', scoreDebt)
print('Valuation score:', scoreValuation)
print('PER position wrt to its sector:', otherAss[0])
print('Intrisic stock value:', otherAss[1])