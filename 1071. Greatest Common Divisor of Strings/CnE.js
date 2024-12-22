/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */

// const gcd = (a, b) => b === 0n ? Number(a) : gcd(b, a % b)

// const gcdOfStrings = (str1, str2) => (str1 + str2 !== str2 + str1) ? "" : str1.substring(0, gcd(BigInt(str1.length), BigInt(str2.length)))

const gcdOfStrings = (str1, str2, gcd = (a, b) => b === 0n ? Number(a) : gcd(b, a % b)) => (str1 + str2 !== str2 + str1) ? "" : str1.substring(0, gcd(BigInt(str1.length), BigInt(str2.length)))