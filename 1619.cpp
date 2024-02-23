class Solution {
public:
    bool isPathCrossing(string path) {
        int x = 0, y = 0;
        set<pair<int, int>> seen;
        seen.insert({0, 0});
        
        for(char c:path){
            if(c=='N')
                y += 1;
            else if(c=='S')
                y -= 1;
            else if(c == 'E')
                x += 1;
            else
                x -= 1;
            
            if(seen.find({x, y}) != seen.end())
                return true;
            seen.insert({x,y});
        }
        return false;
    }
};