#include <iostream>
#include <vector>

#include "../include/stack_analysis.h"
#include "../include/heap_analysis.h"
#include "../include/profit_analysis.h"

using namespace std;

int main()
{
    int k;

    cout << "Enter value of K: ";
    cin >> k;

    StackAnalysis stackAnalysis;
    HeapAnalysis heapAnalysis(k);
    ProfitAnalysis profitAnalysis;

    int price;

    cout << "\nEnter stock prices (-1 to stop):\n";

    while(true)
    {
        cin >> price;

        if(price == -1)
            break;

        cout << "\nNew Price: " << price << endl;

        // STACK OPERATIONS
        int span = stackAnalysis.processSpan(price);
        int nge  = stackAnalysis.nextGreater(price);

        // HEAP OPERATIONS
        heapAnalysis.processPrice(price);

        int maxPrice = heapAnalysis.getMaxPrice();
        int minPrice = heapAnalysis.getMinPrice();

        vector<int> topK = heapAnalysis.getTopKPrices();

        // PROFIT CALCULATION
        profitAnalysis.processPrice(price);
        int maxProfit = profitAnalysis.getMaxProfit();


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