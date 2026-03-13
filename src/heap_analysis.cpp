#include "../include/heap_analysis.h"

#include <queue>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;


// internal data
static int K;
static int maxPrice = INT_MIN;
static int minPrice = INT_MAX;

static priority_queue<int, vector<int>, greater<int>> minHeap;


// constructor
HeapAnalyzer::HeapAnalyzer(int k)
{
    K = k;
}


// process new price
void HeapAnalyzer::processPrice(int price)
{
    // update max price
    if(price > maxPrice)
        maxPrice = price;

    // update min price
    if(price < minPrice)
        minPrice = price;


    // maintain top K prices using min heap
    minHeap.push(price);

    if(minHeap.size() > K)
        minHeap.pop();
}


// return maximum price
int HeapAnalyzer::getMaxPrice()
{
    return maxPrice;
}


// return minimum price
int HeapAnalyzer::getMinPrice()
{
    return minPrice;
}


// return top K prices
vector<int> HeapAnalyzer::getTopKPrices()
{
    vector<int> result;

    priority_queue<int, vector<int>, greater<int>> temp = minHeap;

    while(!temp.empty())
    {
        result.push_back(temp.top());
        temp.pop();
    }

    // sort descending for better display
    sort(result.begin(), result.end(), greater<int>());

    return result;
}