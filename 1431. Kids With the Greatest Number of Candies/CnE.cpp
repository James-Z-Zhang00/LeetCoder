class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        using namespace std;
        int maxCandies = *max_element(candies.begin(), candies.end());
        // max_element returns an iterator, use * for deferencing to get the element (max value)
        vector<bool> res;
        res.reserve(candies.size()); 
        // Reserve space to avoid multiple allocations, improve performance
        for (int c : candies) res.push_back(c + extraCandies >= maxCandies);
        return res;
    }
};