var maxArea = (height: number[]): number => {
    let right: number = height.length - 1
    let left: number = 0
    let area: number = 0

    while (left < right) {
        let curr_area: number = Math.min(height[left], height[right]) * (right - left)
        area = Math.max(area, curr_area)

        if (height[left] < height[right]) left += 1
        else right -= 1
    }
    return area
}