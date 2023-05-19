from modules.growth_score import growth_score
from modules.dividend_score import yield_score, payout_ratio_score
import pandas as pd


netSales = pd.DataFrame([[83049,	83044,	86849,	57139, 57546, 60559]], 
                         index = ['netSales'], 
                         columns=['2017','2018','2019','2020','2021','2022'])

EPS = pd.DataFrame([[7.29, 7.01, 6.32, 4.93, 5.61, 6.84]],
                    index = ['EPS'], 
                    columns=['2017','2018','2019','2020','2021','2022'])
scoreGrowth = growth_score(netSales, EPS)

dividendYield = pd.DataFrame([[0.031,	0.0344,	0.0397,	0.0324,	0.0274,	0.0288]],
                    index = ['Yield'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

payoutRatio = pd.DataFrame([[0.51,	0.54,	0.62,	0.71,	0.64,	0.55]],
                    index = ['Payout ratio'], 
                    columns=['2017','2018','2019','2020','2021','2022'])

scoreYield = yield_score(dividendYield)
scorePayoutRatio = payout_ratio_score(payoutRatio)

print('Growth score:', scoreGrowth)
print('Dividend Yield score:', scoreYield)
print('Dividend payout ratio score:', scorePayoutRatio)