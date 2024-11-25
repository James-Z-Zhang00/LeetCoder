function removeElement(nums: number[], val: number): number {
    let counter = 0
    for (let n of nums) if (n !== val) nums[counter++] = n
    return counter
};