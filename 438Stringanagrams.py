def findAnagrams(s: str, p: str) -> list[int]:
    phash = [0] * 27
    shash = [0] * 27
    size = len(p)
    location = []
    for i in range(size):
        phash[ord(p[i]) - ord('a')] += 1
        shash[ord(s[i]) - ord('a')] += 1

    i = 0
    for i in range(len(s) - size):
        if phash == shash:
            location.append(i)
        shash[ord(s[i + size]) - ord('a')] += 1
        shash[ord(s[i]) - ord('a')] -= 1

    if phash == shash:
        location.append(i)
    return location

def isAnagram(s: str, t: str) -> bool:
    # if len(s) > len(t) or len(t) > len(s):
    #     return False

    for i in s:
        if s.count(i) != t.count(i):
            return False
    return True

def groupAnagram(strs):
    group = []
    count = 0
    while strs:
        inner = []
        for i in strs:
            for j in strs:
                if sorted(i) == sorted(j):
                    inner.append(j)
            for deletes in inner:
                strs.remove(deletes)
            break
        group.append(inner)
    return group
if __name__ == '__main__':
    print(findAnagrams("ab","ba"))
    print(isAnagram("aacc","ccac"))
    print(groupAnagram(["nozzle","punjabi","waterlogged","imprison","crux","numismatists","sultans","rambles","deprecating","aware","outfield","marlborough","guardrooms","roast","wattage","shortcuts","confidential","reprint","foxtrot","dispossession","floodgate","unfriendliest","semimonthlies","dwellers","walkways","wastrels","dippers","engrossing","undertakings","unforeseen","oscilloscopes","pioneers","geller","neglects","cultivates","mantegna","elicit","couriered","shielded","shrew","heartening","lucks","teammates","jewishness","documentaries","subliming","sultan","redo","recopy","flippancy","rothko","conductor","e","carolingian","outmanoeuvres","gewgaw","saki","sarah","snooping","hakka","highness","mewling","spender","blockhead","detonated","cognac","congaing","prissy","loathes","bluebell","involuntary","aping","sadly","jiving","buffalo","chided","instalment","boon","ashikaga","enigmas","recommenced","snell","parsley","buns","abracadabra","forewomen","persecuted","carsick","janitorial","neonate","expediti"]))