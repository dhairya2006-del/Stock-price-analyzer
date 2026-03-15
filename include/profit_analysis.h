#ifndef PROFIT_ANALYSIS_H
#define PROFIT_ANALYSIS_H

class ProfitAnalysis
{
public:
    // process new stock price
    void processPrice(int price);

    // return maximum profit so far
    int getMaxProfit();
};

#endif