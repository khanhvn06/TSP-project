
from docplex.mp.model import Model
from math import *

def is_float(n):
    try:
        float(n)
        return True
    except:
        return False

def readdata(data): 
    T = []
    with open(data, "r") as file1:
        for line in file1.readlines():  
            lst = [float(n) for n in line.split('  ') if is_float(n)]
            T.append(lst)       
    return T
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def readdatafromcoor(data): 
    T = []
    with open(data, "r") as file1:
        for line in file1.readlines():  
            lst = [float(n) for n in line.split() if is_float(n)]
            T.append(lst) 
    print("T=",T)
    print(len(T))
    CTable=[]
    for i in range(0,len(T),1):
        print(len(T[i]))
        if (len(T[i])==3):
            CTable.append(T[i])
          
    DTable=[[0 for j in range(0,N,1) ]for i in range(0,N,1)]
    
    for i in range(0,N,1):
       
        for j in range(0,N,1):
            
            DTable[i][j]=(distance(CTable[i][1],CTable[i][2],CTable[j][1],CTable[j][2]))
            
    
    return DTable

N=16

A=1
#M=readdata("five_d.txt")
M=readdatafromcoor("ulysses16.tsp")
# Check=readdata("att48_d.txt")

print("M=",M)

# for i in range(0,N,1):
#     print()
#     for j in range(0,N,1):
#         print(int(M[i][j])-Check[i][j], end=' ')

# def readsolution(solution):
#     T = []
#     with open(solution, "r") as file1:
#         for line in file1.readlines():  
#             if is_float(line):
#                 T.append(float(line))       
#     return T

# def carrying_normalroute(C):
#     G=[]             #products carrying array
#     G.append(total_products)
#     for i in range (1,N,1):
#         G.append(G[i-1]-C[i])
#     print("G=",G)
#     return G


# def workforce(G,M,S):
    
#     D=[]
#     F=[]
#     for i in range(0,N,1):
#         a=S[i]
#         if (i==N-1):
#             b=S[0]
#         else:
#                 b=S[i+1]
#         d=M[a-1][b-1]
#         D.append(d)
#         f=G[i]*d
#         F.append(f)
#     return D,F

# def sumforce(F):
#     sum_force=0
#     for i in range(N-1):
#         sum_force=sum_force+F[i]
#     return sum_force


    



# S=readsolution("five_s.txt")

# for i in range(N):
#     S[i]=int(S[i])
#     S.append(S[i])
    
# print("S=",S)   #S element must be -1 for index
# def calculcapcity(S):
#     C=[0 for i in range(N*2)] #consumption each node
#     C[0]=0
#     C[N]=0
#     for i in range(1,N,1):
#         for j in range (i, i+N,1):
#             a=S[j]
#             if (j==2*N-1):
#                 b=S[0]
#             else:
#                 b=S[j+1]
#             d=M[a-1][b-1]
#             C[i]=C[i]+d
#     for i in range(N,N*2,1):
#         C[i]=C[i-N]
#     return C

# C=  calculcapcity(S)
# print("C=",C) 

# total_products=0

# for i in range(N):
#     total_products=total_products+C[i]
# print("Total products=",total_products)

# G=carrying_normalroute(C)
# D,F=workforce(G,M,S)
# print("D=",D)
# print("F=",F)

# print("Total workforce of normal route(2 rounds)=",2*sumforce(F))
# #------------------algo-------------------------------------------------
# S_algo=[0 for i in range(2*N)]
# S_algo_1=[0 for i in range(N)]
# S_algo_2=[0 for i in range(N)]
# for i in range(N):
#     S_algo[i]=S[i]
#     S_algo_1[i]=S[i]
# S_algo[N]=S[0]
# count=1
# while count<N:
#     S_algo[N+count]=S[N-count]
#     count=count+1
    
# for i in range(N):
#     S_algo_2[i]=S_algo[i+N]
# print("S_algo=",S_algo)


# def calculcapacity_algo(S_algo):
#     C_algo=[0 for i in range(N*2)] #consumption each node
#     C_algo[0]=0
#     C_algo[N]=0
#     for i in range(1,2*N,1):
#         if (i!=N):
#             j=i
#             while True:
#                 a=S_algo[j]
#                 if (j==2*N-1):
#                     b=S_algo[0]
#                 else:
#                     b=S_algo[j+1]
#                 d=M[a-1][b-1]
#                 C_algo[i]=C_algo[i]+d
#                 if (j==2*N-1):
#                     j=0
#                 else:
#                     j=j+1
#                 if (S_algo[j]==S_algo[i]):
#                     break
               
       
            
#     return C_algo

# C_algo=calculcapacity_algo(S_algo)
# print("C_algo=",C_algo)

# total_products_algo_1=0
# total_products_algo_2=0

# for i in range(N):
#     total_products_algo_1=total_products_algo_1+C_algo[i]
# print("Total products algo 1=",total_products_algo_1)

# for i in range(N,2*N,1):
#     total_products_algo_2=total_products_algo_2+C_algo[i]
# print("Total products algo 2=",total_products_algo_2)

# G_algo_1=[]
# G_algo_1.append(total_products_algo_1)
# for i in range (1,N,1):
#      G_algo_1.append(G_algo_1[i-1]-C_algo[i])
# print("G_algo_1=",G_algo_1)

# G_algo_2=[]
# G_algo_2.append(total_products_algo_2)
# for i in range (1,N,1):
#     G_algo_2.append(G_algo_2[i-1]-C_algo[i+N])


# D_algo_1,F_algo_1=workforce(G_algo_1,M,S_algo_1)
# print("S_algo_1=",S_algo_1)

# print("D_algo_1=",D_algo_1)
# print("F_algo_1=",F_algo_1)
# print("Total workforce of algo route 1=",sumforce(F_algo_1))

# print("G_algo_2=",G_algo_2)
# D_algo_2,F_algo_2=workforce(G_algo_2,M,S_algo_2)
# print("S_algo_2=",S_algo_2)
# print("D_algo_2=",D_algo_2)
# print("F_algo_2=",F_algo_2)
# print("Total workforce of algo route 2=",sumforce(F_algo_2))
# print("Total workforce of algo =",sumforce(F_algo_1)+sumforce(F_algo_2))

#MIP------------------------------------------------------------
maxd=0;
for i in range(0,N,1):
    for j in range(0,N,1):
        M[i][j]=float(int(M[i][j]*10))
        if M[i][j]>maxd:
            maxd=M[i][j]
         
Limit=maxd*N*4
H=Limit
print("H=",H)
for i in range(N):
    for j in range(N):
        if M[i][j]==0:
            M[i][j]=Limit
print(M)
def solveTSP():
    idxM = [(i, j) for i in range(1,N+1,1) for j in range(1,N+1,1) ]
    idxd = [i for i in range (1,N+1,1)  ]
    



    mdl = Model(name='TSP')
    x=mdl.binary_var_dict(idxM,0,1, "x")

    u=mdl.integer_var_dict(idxd,1,N,'u')

 


    for i in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for j in range(1,N+1,1)) == 1)
         
    for j in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for i in range(1,N+1,1)) == 1)
         
    for i in range(1,N+1,1):
        for j in range(1,N+1,1):
            if (i!=j) and (j!=A):
                mdl.add_constraint(u[i]-u[j]+N*x[i,j]<=N-1)
                
    for i in range(1,N+1,1):
        if i==A:
            mdl.add_constraint(u[i]==1)
           
    
    mdl.set_objective("min", mdl.sum(M[i-1][j-1]*x[i, j] for i in range(1,N+1,1) for j in range(1,N+1,1)))
    mdl.print_information()
      
    mdl.solve()

    mdl.print_solution()

    print(mdl.solve_details)
    
def solveMIP():
   
    idxM = [(i, j) for i in range(1,N+1,1) for j in range(1,N+1,1) ]
    idxd = [i for i in range (1,N+1,1)  ]
    idxf = [(i, j) for i in range(1,N+1,1) for j in range(1,N+1,1) ]
    



    mdl = Model(name='repeat')
    x=mdl.binary_var_dict(idxM,0,1, "x")

    u=mdl.integer_var_dict(idxd,1,N,'u')

    f=mdl.continuous_var_dict(idxf,0,Limit, "f")
    c=mdl.continuous_var_dict(idxd,0,Limit,'c')


    for i in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for j in range(1,N+1,1)) == 1)
         
    for j in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for i in range(1,N+1,1)) == 1)
         
    for i in range(1,N+1,1):
        for j in range(1,N+1,1):
            if (i!=j) and (j!=A):
                mdl.add_constraint(u[i]-u[j]+N*x[i,j]<=N-1)
                
    for i in range(1,N+1,1):
        if i==A:
            mdl.add_constraint(u[i]==1)
            mdl.add_constraint(c[i]==0)    #c_A=0

    #new constraints
    for i in range(1,N+1,1):
        for j in range(1,N+1,1):
            mdl.add_constraint(f[i,j]<=H*x[i,j])

    for j in range(1,N+1,1):
        if (j!=A):
            mdl.add_constraint(mdl.sum(f[i, j] for i in range(1,N+1,1))== c[j]+mdl.sum(f[j, k] for k in range(1,N+1,1)))
    for k in range(1,N+1,1):
        if (k!=A):
            mdl.add_constraint(c[k]==  mdl.sum(M[i-1][j-1]*x[i,j]for i in range(1,N+1,1)
                                        for j in range (1,N+1,1)) )      

    mdl.set_objective("min", 2*mdl.sum(M[i-1][j-1]*f[i,j]for i in range(1,N+1,1)
                                    for j in range (1,N+1,1)))
    mdl.print_information()
      
    mdl.solve()

    mdl.print_solution()

    print(mdl.solve_details)



    mdl = Model(name='inverse')
    x=mdl.binary_var_dict(idxM,0,1, "x")

    #u=mdl.integer_var_dict(idxd,1,N,'u')

    f=mdl.continuous_var_dict(idxf,0,Limit, "f")
    c=mdl.continuous_var_dict(idxd,0,Limit,'c')
    f2=mdl.continuous_var_dict(idxf,0,Limit, "f2")
    c2=mdl.continuous_var_dict(idxd,0,Limit,'c2')


    t=mdl.continuous_var_dict(idxd,0,Limit,'t')

    for i in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for j in range(1,N+1,1)) == 1)
         
    for j in range(1,N+1,1):
          mdl.add_constraint(mdl.sum(x[i, j] for i in range(1,N+1,1)) == 1)
         
    # for i in range(1,N+1,1):
    #     for j in range(1,N+1,1):
    #         if (i!=j) and (j!=A):
    #             mdl.add_constraint(u[i]-u[j]+N*x[i,j]<=N-1)
                
    for i in range(1,N+1,1):
        if i==A:
            # mdl.add_constraint(u[i]==1)
            mdl.add_constraint(c[i]==0)    #c_A=0
            mdl.add_constraint(t[i]==0) # time constraint
            
    #Time constraints
    for k in range(1,N+1,1):
        if (k!=A):
            mdl.add_constraint(mdl.sum(M[i-1][j-1]*x[i,j]for i in range(1,N+1,1) for j in range (1,N+1,1))>=t[k]+M[k-1][A-1]*x[k,A])  
    for i in range(1,N+1,1):
        for j in range(1,N+1,1):
            if (i!=j)and (j!=A):
                mdl.add_constraint(t[j]+H*(1-x[i,j])>=t[i]+M[i-1][j-1])   #t   
            
    #products constraints
    for i in range(1,N+1,1):
        for j in range(1,N+1,1):
            mdl.add_constraint(f[i,j]<=H*x[i,j])
            mdl.add_constraint(f2[i,j]<=H*x[j,i])

    for j in range(1,N+1,1):
        if (j!=A):
            mdl.add_constraint(mdl.sum(f[i, j] for i in range(1,N+1,1))== c[j]+mdl.sum(f[j, k] for k in range(1,N+1,1)))
            
    for j in range(1,N+1,1): 
        if (j!=A):    
            mdl.add_constraint(mdl.sum(f2[i, j] for i in range(1,N+1,1))== c2[j]+mdl.sum(f2[j, k] for k in range(1,N+1,1)))
            

         
    for k in range(1,N+1,1):
        if (k!=A):
            mdl.add_constraint(c[k] ==  2*mdl.sum(M[i-1][j-1]*x[i,j]for i in range(1,N+1,1) for j in range (1,N+1,1))-2*t[k]) 
            mdl.add_constraint(c2[k]==2*t[k]) 
            


    mdl.set_objective("min", mdl.sum( M[i-1][j-1]*f[i,j]for i in range(1,N+1,1) for j in range (1,N+1,1))
                      +mdl.sum( M[i-1][j-1]*f2[i,j]for i in range(1,N+1,1) for j in range (1,N+1,1)))
                                     

    mdl.print_information()
      
    mdl.solve()

    mdl.print_solution()
   

    print(mdl.solve_details)
    
    
solveTSP()
solveMIP()