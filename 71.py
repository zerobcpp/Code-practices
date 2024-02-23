class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        path = path.replace('//', '/').split('/')
        print(path)
        
        for dirs in path:
            if not dirs or dirs == '.':
                continue
            if dirs == '..':
                if st:
                    st.pop()
            else:
                st.append(dirs)
        
        
        return '/' + '/'.join(st)
            