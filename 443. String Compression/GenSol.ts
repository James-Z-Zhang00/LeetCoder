const compress = (chars: string[]): number => {
    var res:number = 0
    var i:number = 0
    var letter:string = ""
    var count:number = 0

    while (i < chars.length) {
        letter = chars[i]
        count = 0
        
        while (i < chars.length && chars[i] === letter) {
            i += 1 // Check the next char
            count += 1 // Increment the same letter count
        }

        chars[res] = letter // Set the leading letter
        res += 1 // Move the res to the next position

        if (count > 1) {
        // If there's a need to display numbers
            for (let c of count.toString()) {
                chars[res] = c // Assign the digit as char/string
                res += 1 // Increment the res to move to the next position
            }
        }
    }
    return res
}