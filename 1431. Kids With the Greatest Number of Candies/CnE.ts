const kidsWithCandies = (candies: number[], extraCandies: number): boolean[] => {
    return candies.map(c => c + extraCandies >= Math.max(...candies));
}