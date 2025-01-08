class Solution
{
public:
    int maxArea(vector<int> &height)
    {

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
                right--;
        }
        return area;
    }
};