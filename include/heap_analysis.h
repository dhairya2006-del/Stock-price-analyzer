#ifndef HEAP_ANALYSIS_H
#define HEAP_ANALYSIS_H

#include <vector>

class HeapAnalysis
{
public:
    // constructor
    HeapAnalysis(int k);

    // process incoming stock price
    void processPrice(int price);

    // return maximum price so far
    int getMaxPrice();

    // return minimum price so far
    int getMinPrice();

    // return top K prices
    std::vector<int> getTopKPrices();
};

#endif