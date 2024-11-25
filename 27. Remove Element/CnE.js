/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = (nums, val) => {
    var counter = 0
    nums.forEach(n => n !== val ? nums[counter++] = n : null)
    // counter++ means to use the value of counter and then apply an increment after the use
    return counter
    // Where counter is the first <counter> numbers of elements 
    // in the list that must not equal to val
};
