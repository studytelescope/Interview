//
// Created by jonny on 20.08.2021.
//

// Find max substring containing strictly growing consequence of numbers

#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

struct interval
{
    int first;
    int second;
};

struct interval max_subinterval(string & arr)
{
    struct interval result = {0, 0};
    int counter = 1;
    int curr_begin = 0;
    int curr_end= 0;

    for(int i = 0; i < arr.size() - 1; i++)
    {
        if(arr[i + 1] > arr[i])
        {
            if(counter == 1)
                curr_begin = i;

            curr_end = i + 1;
            counter++;

            if(counter > result.first - result.second + 1)
                result = {curr_begin, curr_end};
        }
        else
            counter = 1;
    }
    return result;
}

int main()
{
    string base_string = "he4llo, 34344 world!123123123";
    cout << max_subinterval(base_string).first << " " << max_subinterval(base_string).second << endl;
    return 0;
}
