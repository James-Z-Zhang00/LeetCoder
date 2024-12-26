class Solution
{
public:
    int compress(vector<char> &chars)
    {
        int res = 0;
        int i = 0;
        char letter = ' ';
        int count = 0;

        while (i < chars.size())
        {
            count = 0;
            letter = chars[i];

            while (i < chars.size() && chars[i] == letter)
            {
                i++;
                count++;
            }

            chars[res] = letter;
            res++;

            if (count > 1)
            {
                for (char c : std::to_string(count))
                {
                    chars[res] = c;
                    res++;
                }
            }
        }
        return res;
    }
};