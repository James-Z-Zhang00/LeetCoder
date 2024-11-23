// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0, right = nums.length
    // left should be the min possible value and right should ne the max possible value
    while (left < right) {
        let middle = left + Math.floor((right-left)/2)
        target > nums[middle] ? left = middle + 1 : right = middle
    }
    return left
};