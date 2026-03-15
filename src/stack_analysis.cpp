#include "../include/stack_analysis.h"

#include <stack>
#include <utility>

using namespace std;


// stack for stock span (price, span)
static stack<pair<int,int>> spanStack;

// stack for next greater element
static stack<int> ngeStack;


// STOCK SPAN
int StackAnalysis::processSpan(int price)
{
    int span = 1;

    while(!spanStack.empty() && spanStack.top().first <= price)
    {
        span += spanStack.top().second;
        spanStack.pop();
    }

    spanStack.push({price, span});

    return span;
}


// NEXT GREATER ELEMENT
int StackAnalysis::nextGreater(int price)
{
    int result = -1;

    while(!ngeStack.empty() && ngeStack.top() <= price)
    {
        result = ngeStack.top();
        ngeStack.pop();
    }

    ngeStack.push(price);

    return result;
}