#######102. Binary Tree Level Order Traversal###############################################################################################################
// Time Complexity : n
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no problem

// Your code here along with comments explaining your approach in three sentences only
I have used here BFS approach where we use a queue to store element on same level and process them on level basis


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        lvl=0
        q=collections.deque()
        q.append(root)
        res=[]
        while len(q)>0:
            l1=[]
            lvl+=1
            #len1=len(q)
            for i in range(len(q)):
                #print(i,lvl,q)
                curr=q.popleft()
                l1.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)               
            res.append(l1)
        return res
            
        
        
        
        

######207. Course Schedule#############################################################################################################


// Time Complexity : n
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : NA

// Your code here along with comments explaining your approach in three sentences only
Here we have also taken BFS approach where we stored all the courses in queue with the prerequisites also we have hash map to map the course to its dependent. So when ever any courses reaches requirement of zero it is released for queue and we keep doing it till our count matches courses



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''if numCourses<2:
            return True
        if len(prerequisites)==0:
            return True'''
        dict1={}
        indegree=[0]*numCourses
        #create dict and indegree list
        for i in prerequisites:
            dep,ind=i[0],i[1]
            if ind not in dict1:
                dict1[ind]=[dep]
            else:
                dict1[ind].append(dep)
            indegree[dep]+=1
        #print(dict1,indegree)
        #update dict with independent course
        '''for i in range(numCourses):
            if i not in dict1:
                dict1[i]=[]  '''  
        
        q1=collections.deque()
        cnt=0
        #populate queue and count
        for i,val in enumerate(indegree):
            if val==0:
                #dict1[i]=[]
                q1.append(i)
                cnt+=1
        print(dict1,indegree)
        print(q1,cnt)
        if cnt==numCourses:
                return True
        while len(q1)>0:
            curr=q1.popleft()
            
            if curr in dict1:
                dep1=dict1[curr]
                for i in dep1:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q1.append(i)
                        cnt+=1
            if cnt==numCourses:
                return True
        return False