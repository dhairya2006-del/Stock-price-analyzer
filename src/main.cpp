#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>

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

    // open input dataset
    ifstream infile("data/raw_prices.csv");

    if(!infile.is_open())
    {
        cout << "Error opening raw_prices.csv" << endl;
        return 1;
    }

    // open output feature dataset
    ofstream outfile("data/features.csv");

    // write header
    outfile << "date,price,span,max_price,min_price,profit\n";

    string line;

    // skip CSV header
    getline(infile, line);

    while(getline(infile, line))
    {
        stringstream ss(line);

        string date;
        string price_str;

        getline(ss, date, ',');
        getline(ss, price_str, ',');

        int price = stoi(price_str);

        cout << "\nNew Price: " << price << endl;

        // STACK
        int span = stackAnalysis.processSpan(price);
        int nge = stackAnalysis.nextGreater(price);

        // HEAP
        heapAnalysis.processPrice(price);

        int maxPrice = heapAnalysis.getMaxPrice();
        int minPrice = heapAnalysis.getMinPrice();

        vector<int> topK = heapAnalysis.getTopKPrices();

        // PROFIT
        profitAnalysis.processPrice(price);
        int maxProfit = profitAnalysis.getMaxProfit();


        // PRINT ANALYTICS
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


        // WRITE FEATURE ROW
        outfile << date << ","
                << price << ","
                << span << ","
                << maxPrice << ","
                << minPrice << ","
                << maxProfit << "\n";
    }

    infile.close();
    outfile.close();

    cout << "\nFeature dataset generated: data/features.csv\n";

    return 0;
}