#ifndef STACK_ANALYSIS_H
#define STACK_ANALYSIS_H

#include <stack>
#include <utility>

class StackAnalysis
{
public:
    // compute stock span
    int processSpan(int price);

    // compute next greater element
    int nextGreater(int price);
};

#endif