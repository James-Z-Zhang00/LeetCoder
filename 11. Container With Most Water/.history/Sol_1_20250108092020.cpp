class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxArea = 0;

        while (left < right) {
            int currentArea = min(height[left], height[right]) * (right - left);
            maxArea = max(maxArea, currentArea);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
};

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
#include <algorithm>

        int left = 0;
        int right = height.size() - 1;
        int area = 0;

        while (left < right)
        {
            int curr_area = min(height[left], height[right]) * (right - left);
            area = max(area, curr_area);

            if (height[left] < height[right])
                left++;
            else
                right++;
        }
        return area;
    }
};