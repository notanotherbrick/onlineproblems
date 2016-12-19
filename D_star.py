# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:55:57 2016

@author: Hobbiton
"""


import heapq
## Initializaiton
sensor_range=1.5
c=8
r=7
state=[['NEW']*c for _ in xrange(r)]
o_pen=[]
h=[[0]*c for _ in xrange(r)]
k=[[0]*c for _ in xrange(r)]
back_pointer=[[[-1,-1] for _ in xrange(c)] for _ in xrange(r)]


#obstacles=[[2,3],[4,1],[5,2]]
obstacles=set([(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(5,3),(6,3),(2,4)])
new_obs=set([(3,4)])
goal=[6,7]
start=[1,2]


def sensor_cost(curr,nex):
    n_x,n_y=nex
    nex=(n_x,n_y)
    curr_x,curr_y=curr
    curr=(curr_x,curr_y)
    if nex in new_obs or curr in new_obs:
        return 10000
    
    return get_cost(curr,nex)
    # fix this later
    if nex in obstacles or curr in obstacles:
        return 10000
    elif abs(curr[0]-nex[0])+abs(curr[1]-nex[1])==2:
        return 1.414
    else:
        return 1
    

def repair_replan(X):
    X_r,X_c=X
    k_min=1000 #check in future
    while k_min != -1 and k_min < h[X_r][X_c]:#) and i<70:
        k_min,X=process_state()
        X_r,X_c=X
#        print 'k end of this iteration is', k_min
#        print 'open list here is',o_pen
#        print [X_r,X_c]
        #raw_input("Press Enter to continue...")        
#        print
   
    path=[]     
    if k_min!=-1:
        #print back_pointer
        path=get_backpointer_path(X,goal)
    return path        
        




def get_cost(curr,nex):
    n_x,n_y=nex
    nex=(n_x,n_y)
    curr_x,curr_y=curr
    curr=(curr_x,curr_y)
    if nex in obstacles or curr in obstacles:
        return 10000
    # move along the diagonal
    elif abs(curr[0]-nex[0])+abs(curr[1]-nex[1])==2:
        return 1.414
    
    else:
        return 1
        

def generate_valid_neighbours(X_r,X_c):
    '''
    rtype : list[list]
    '''
    moves=[(1,1),(-1,1),
           (1,-1),(-1,-1),
           (1,0),(0,1),
           (-1,0),(0,-1)]
    valid_moves=[]
    for m_r,m_c in moves:
        if m_r+X_r>=0 and m_r+X_r<r and m_c+X_c>=0 and m_c+X_c<c:
            valid_moves.append([m_r+X_r,m_c+X_c])
    return valid_moves

def insert (X,h_new):
    X_r,X_c=X[0],X[1]
    if state[X_r][X_c]=='NEW':
        k[X_r][X_c]=h_new
    elif state[X_r][X_c]=='OPEN':
        k[X_r][X_c]=min(h_new,k[X_r][X_c])
    elif state[X_r][X_c]=='CLOSED':
        k[X_r][X_c]=min(h_new,h[X_r][X_c])
    h[X_r][X_c]=h_new
    state[X_r][X_c]='OPEN'
    heapq.heappush(o_pen,(k[X_r][X_c],X))
    
    



def process_state():
    if not o_pen: # X=NULL    
        return -1,[-1,-1]
    
    k_old,[X_r,X_c]=heapq.heappop(o_pen)
    #print 'Got k =',k_old
    state[X_r][X_c]='CLOSED'
    #print 'Processing state', [X_r,X_c],'with h =',h[X_r][X_c],'with b=', back_pointer[X_r][X_c] 
    if k_old<h[X_r][X_c]:
        for Y_r,Y_c in generate_valid_neighbours(X_r,X_c):
            if h[Y_r][Y_c]<=k_old and \
            h[X_r][X_c]>h[Y_r][Y_c]+get_cost([X_r,X_c],[Y_r,Y_c]):# and state[Y_r][Y_c]!='NEW':
                back_pointer[X_r][X_c] = [Y_r,Y_c]
                h[X_r][X_c]=h[Y_r][Y_c]+get_cost([X_r,X_c],[Y_r,Y_c])
                
    if k_old==h[X_r][X_c]:            
        for Y_r,Y_c in generate_valid_neighbours(X_r,X_c):
            if state[Y_r][Y_c]=='NEW'or (
            back_pointer[Y_r][Y_c] == [X_r,X_c] and 
                h[Y_r][Y_c]!=h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c])) or (
            back_pointer[Y_r][Y_c] != [X_r,X_c] and 
                h[Y_r][Y_c]>h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c])):
                back_pointer[Y_r][Y_c]=[X_r,X_c]
                insert([Y_r,Y_c],h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c]))

    else:
        for Y_r,Y_c in generate_valid_neighbours(X_r,X_c):
            if state[Y_r][Y_c]=='NEW'or (
            back_pointer[Y_r][Y_c] == [X_r,X_c] and 
                h[Y_r][Y_c]!=h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c])):
                back_pointer[Y_r][Y_c]=[X_r,X_c]
                insert([Y_r,Y_c],
                h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c]))
            else:
                if back_pointer[Y_r][Y_c]!=[X_r,X_c] and \
                h[Y_r][Y_c]>h[X_r][X_c]+get_cost([X_r,X_c],[Y_r,Y_c]):
                    insert([X_r,X_c],h[X_r][X_c])
                else:
                    if back_pointer[Y_r][Y_c]!=[X_r,X_c] and \
                    h[X_r][X_c]>h[Y_r][Y_c]+get_cost([X_r,X_c],[Y_r,Y_c]) and \
                        state[Y_r][Y_c]=='CLOSED' and \
                        h[Y_r][Y_c]>k_old:
                            insert([Y_r,Y_c],h[Y_r][Y_c])
                             
    return k_old,[X_r,X_c] # doubt

def states_sensor_range(curr):
    X_r,X_c=curr
    '''
    rtype : list[list]
    '''
    moves=[]
    l=range(-1*(1+int(sensor_range)),(1+int(sensor_range))+1)
    for i in l:
        for j in l:
            if (i)**2 + (j)**2 <= sensor_range**2 and \
            i+X_r>=0 and \
            i+X_r<r and \
            j+X_c>=0 and \
            j+X_c<c:
                moves.append([i+X_r,j+X_c])
    return moves
    


def prepare_repair(curr):
    for X in states_sensor_range(curr):
        X_r,X_c=X
        for Y in generate_valid_neighbours(X_r,X_c):
            if get_cost(X,Y)!=sensor_cost(X,Y):
                modify_cost(X,Y,sensor_cost(Y,X))
            if get_cost(Y,X)!=sensor_cost(Y,X):
                modify_cost(Y,X,sensor_cost(X,Y))
                

def modify_cost(X,Y,cval):
    # new_obstacle
    print X,Y,cval,get_cost(X,Y),'dsdsds'
    print o_pen
    X_r,X_c=X
    Y_r,Y_c=Y    
    Y=(Y_r,Y_c)
    if cval==10000: # saw new obstacle
        obstacles.add(Y)
        new_obs.remove(Y)
    
    # new open_node    
    else:
        obstacles.remove(Y)
    print state[Y_r][Y_c]
    print 
    if state[X_r][X_c]=='CLOSED':
        insert(X,h[X_r][X_c])
        print 'open list is', o_pen
    

def init_plan(start,goal):
    X_r,X_c=goal
    X=goal
    print 'goal for inital plan is', goal
    k_min=1000 #check in future
    while k_min != -1 and \
        state[X_r][X_c]!='CLOSED' and \
        X!=start:#) and i<70:
        k_min,X=process_state()
        X_r,X_c=X
#        print 'k end of this iteration is', k_min
#        print 'open list here is',o_pen
#        print [X_r,X_c]
#        #raw_input("Press Enter to continue...")        
#        print
   
    path=[]     
    if k_min!=-1:
        #print back_pointer
        path=get_backpointer_path(X,goal)
    
    return path
    
#

def get_backpointer_path(X,goal):
    ''' return path from X to goal
    rtype : list[[x_r,x_c]]
    '''
    path=[]
    #print back_pointer
    

    while X!=goal:
        path.append(X)
        X=back_pointer[X[0]][X[1]]
    
    path.append(X) # add goal state in the end
        
    return path
    





## Outer block of code

    
def d_star_body():
    h[goal[0]][goal[1]]=0
    insert(goal,h[goal[0]][goal[1]])
    
    curr=start
    
    path=init_plan(curr,goal)
    print path
    return -1
    
    if not path:
        return -1
    
    print path
    # Intialization complete
    
    while curr!=goal:
        print 'here', curr
        prepare_repair(curr)
        path=repair_replan(curr)
        
        if not path:
            return -1
        print path
        curr=path[1]
    
    return curr
if __name__ == "__main__":
    d_star_body()