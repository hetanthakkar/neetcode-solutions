def lengthOfLongestSubstring(s):
    windowSize = 0
    window = {}
    for i in range(len(s)):
        if s[i] not in window:
            window.update({s[i]: i})
        else:
            for key in list(window.keys()):
                if key == s[i]:
                    break
                del window[key]
            del window[s[i]]
            window.update({s[i]: i})
        windowSize = max(len(window), windowSize)
    return windowSize
