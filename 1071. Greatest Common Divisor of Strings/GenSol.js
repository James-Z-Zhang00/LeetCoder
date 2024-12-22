/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */

const gcd = (a, b) => {
    a = BigInt(a);
    b = BigInt(b);
    while (b !== 0n) {
        [a, b] = [b, a % b];
    }
    return Number(a);
};

var gcdOfStrings = (str1, str2) => {
    return (str1 + str2 !== str2 + str1) ? "" : str1.substring(0,gcd(str1.length,str2.length))
};