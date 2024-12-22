/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = (word1, word2) => {
    let res = ""
    let i = 0
    while (i < word1.length || i < word2.length) {
        if (i < word1.length) {res += word1[i]}
        if (i < word2.length) {res += word2[i]}
        i += 1
    }

    return res
};