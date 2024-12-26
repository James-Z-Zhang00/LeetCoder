/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = (chars) => {
    let res = 0
    let i = 0
    let letter = ""
    let count = 0

    while (i < chars.length) {
        
        letter = chars[i]
        count = 0
        
        while (i < chars.length && chars[i] === letter) {
            count += 1
            i += 1
        }

        chars[res] = letter
        res += 1

        if (count > 1) {
            for (const c of count.toString()) {
                chars[res] = c
                res += 1
            }
        }
    }
    return res
}