#include "../include/profit_analysis.h"

#include <climits>

using namespace std;


// track minimum price seen so far
static int minPrice = INT_MAX;

// track maximum profit
static int maxProfit = 0;


// process incoming price
void ProfitAnalysis::processPrice(int price)
{
    // update minimum price
    if(price < minPrice)
        minPrice = price;

    // calculate profit if sold today
    int profit = price - minPrice;

    // update maximum profit
    if(profit > maxProfit)
        maxProfit = profit;
}


// return maximum profit
int ProfitAnalysis::getMaxProfit()
{
    return maxProfit;
}