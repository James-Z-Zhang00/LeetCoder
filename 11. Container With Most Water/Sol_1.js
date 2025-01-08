/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = (height) => {
    var area = 0
    var right = height.length - 1
    var left = 0

    while (left < right) {
        var curr_area = Math.min(height[left], height[right]) * (right - left)
        area = Math.max(area, curr_area)

        if (height[left] < height[right]) {left += 1}
        else {right -= 1}
    }
    return area
};