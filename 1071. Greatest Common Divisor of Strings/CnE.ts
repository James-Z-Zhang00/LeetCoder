// const gcd = (a: number, b: number): number => b === 0 ? a : gcd(b, a % b)

// const gcdOfStrings = (str1: string, str2: string) :string => (str1 + str2 !== str2 + str1) ? "" : str1.substring(0,gcd(str1.length,str2.length))

const gcdOfStrings = (str1: string, str2: string, gcd = (a: number,b: number): number => b === 0 ? a : gcd(b, a % b)) => (str1 + str2 !== str2 + str1) ? "" : str1.substring(0,gcd(str1.length,str2.length))