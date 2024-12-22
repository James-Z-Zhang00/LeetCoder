/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = (candies, extraCandies) => {
    return candies.map(c => c + extraCandies >= Math.max(...candies));
}