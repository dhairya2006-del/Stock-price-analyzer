#ifndef HEAP_ANALYZER_H
#define HEAP_ANALYZER_H

#include <vector>

class HeapAnalyzer
{
public:
    // constructor
    HeapAnalyzer(int k);

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