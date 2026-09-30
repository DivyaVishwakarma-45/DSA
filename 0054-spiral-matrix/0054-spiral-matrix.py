class Solution:
    def spiralOrder(self, arr: list[list[int]]) -> list[int]:
        srow=0;scol=0;ans=[]
        erow=len(arr)-1;ecol=len(arr[0])-1
        while(srow<=erow and scol<=ecol):
            for i in range(srow,ecol+1):
                ans.append(arr[srow][i])
            for j in range(srow+1,erow+1):
                ans.append(arr[j][ecol])
            for k in range(ecol-1,scol-1,-1):
                if(srow>=erow):
                    break
                else:
                    ans.append(arr[erow][k])
            for l in range(erow-1,srow,-1):
                if(scol>=ecol):
                    break
                else:
                    ans.append(arr[l][scol])
            srow+=1;scol+=1
            ecol-=1;erow-=1
        return ans
            