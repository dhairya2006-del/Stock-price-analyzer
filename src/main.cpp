#include <iostream>
#include <vector>

#include "../include/stack_analysis.h"
#include "../include/heap_analysis.h"
#include "../include/profit_analysis.h"

using namespace std;


// STACK ANALYZER
class StackAnalyzer {
public:
    int processSpan(int price);
    int nextGreater(int price);
};


// HEAP ANALYZER
class HeapAnalyzer {
public:
    HeapAnalyzer(int k);

    void processPrice(int price);

    int getMaxPrice();
    int getMinPrice();

    vector<int> getTopKPrices();
};


// PROFIT ANALYZER
class ProfitAnalyzer {
public:
    void processPrice(int price);
    int getMaxProfit();
};



int main()
{
    int k;

    cout << "Enter value of K: ";
    cin >> k;

    StackAnalyzer stackAnalyzer;
    HeapAnalyzer heapAnalyzer(k);
    ProfitAnalyzer profitAnalyzer;

    int price;

    cout << "\nEnter stock prices (-1 to stop):\n";

    while(true)
    {
        cin >> price;

        if(price == -1)
            break;

        cout << "\nNew Price: " << price << endl;

        // STACK OPERATIONS
        int span = stackAnalyzer.processSpan(price);
        int nge  = stackAnalyzer.nextGreater(price);

        // HEAP OPERATIONS
        heapAnalyzer.processPrice(price);

        int maxPrice = heapAnalyzer.getMaxPrice();
        int minPrice = heapAnalyzer.getMinPrice();

        vector<int> topK = heapAnalyzer.getTopKPrices();

        // PROFIT CALCULATION
        profitAnalyzer.processPrice(price);
        int maxProfit = profitAnalyzer.getMaxProfit();


        cout << "Max Price: " << maxPrice << endl;
        cout << "Min Price: " << minPrice << endl;

        cout << "Span: " << span << endl;

        cout << "Next Greater Element: ";
        if(nge == -1)
            cout << "None" << endl;
        else
            cout << nge << endl;

        cout << "Top " << k << " Prices so far: ";

        for(int x : topK)
            cout << x << " ";

        cout << endl;

        cout << "Maximum Profit So Far: " << maxProfit << endl;

        cout << "-----------------------------------\n";
    }

    return 0;
}