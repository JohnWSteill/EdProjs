def writeToOutfile(fun):
    def wrapper(*args,**kwargs):
        ans = fun(*args,**kwargs)
        fileparts = args[1].split('.')
        outFileName = ".".join(fileparts[0:-1]) + "_out." + fileparts[-1]        
        with open(outFileName,'w') as f:
            for a in ans: 
                f.write(a)
    return wrapper

def readInpFileKDna(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            k = int(f.readline())
            dna = f.readline().strip()
        ans = fun(*args,dna = dna, k = k)
    return wrapper

def readInpFileDirGraph(fun):
    def wrapper(*args,**kwargs):
        g = {}
        with open(args[1]) as f:
            for line in f.readlines():
                (k,vs) = line.split('->')
                for v in vs.strip().split(','):
                    addKeyAndValTodeBrujin(g,k.strip(),v)
        ans = fun(*args,g=g)
    return wrapper

def readInpFileDna(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            dna = [el.strip() for el in f.readlines()]
        ans = fun(*args,dna = dna)
    return wrapper

def addKeyAndValTodeBrujin(dB,k,v):
    if k in dB:
        dB[k].append(v)
    else:
        dB[k] = [v]

def outputDeBrujin(dB):
    ans = []
    for k in sorted(dB):
        ans.append(k + ' -> ' + ','.join(dB[k])+'\n')
    return ans
    
    
# http://docs.sublimetext.info/en/latest/basic_concepts.html
class UCSD_Ros_Solver(object): 
    """ This class performs Rosalind Project solutions. 

    Usage is as follows:  
    r = UCSD_Ros_Solver() 
    r.myProb("MyData.txt")
    Assumes that MyData.txt is in working directory or getwd()/Data 
    """

    @readInpFileDirGraph
    @writeToOutfile
    def getEulerCycle(self, inpFile, g = None):

        head = min(g.keys())
        tail = g[head][0]
        if len(g[head])>1:
            g[head] = g[head][1:]
        else:
            g.pop(head)
        cycle = [(head,tail)]
        while g != {}:
            tails = [el[1] for el in cycle]
            for k in g.keys():
                if k in tails:
                    newStart = k
                    break;
                
            indNS = tails.index(newStart)
            cycle = cycle[indNS+1:] + cycle[:indNS+1] 
            
            while True:
                pT = cycle[-1][1]
                try:
                    tail = g[pT][0]
                except:
                    break
                if len(g[pT]) > 1:
                    g[pT] = g[pT][1:]
                else:
                    g.pop(pT)
                cycle.append([pT,tail])
                
        
        c = [cycle[0][0]]
        for el in cycle:
            c.append(el[1])
        return '->'.join(c)
        
        
        
        

    @readInpFileKDna
    @writeToOutfile
    def getDeBrujinK(self,inpFile,k=None,dna=None):
        kmers = [dna[i:i+k] for i in range(len(dna)-k+1)]
        deBrujin = {}
        for d in kmers:
            addKeyAndValTodeBrujin(deBrujin, d[:-1],d[1:])
        return outputDeBrujin(deBrujin)

    @readInpFileDna
    @writeToOutfile
    def getDeBrujinFromKmers(self,inpFile,dna=None):
        deBrujin = {}
        for d in dna:
            addKeyAndValTodeBrujin(deBrujin, d[:-1],d[1:])
        return outputDeBrujin(deBrujin)

    @readInpFileKDna
    @writeToOutfile
    def getDeBrujinfromText(self,inpFile,k=None,dna=None):
        deBrujin= {}
        for i in range(len(dna)-k+1):
            addKeyAndValTodeBrujin(deBrujin, dna[i:i+k-1],dna[i+1:i+k])
        return outputDeBrujin(deBrujin)
        

    @readInpFileDna
    @writeToOutfile
    def getOverlap(self,inpFile,dna=None,echoToScreen=False):
        adjGra = []
        for d1 in dna:
            for d2 in dna:
                if d1[1:] == d2[:-1]:
                    adjGra.append(d1 + ' -> ' + d2 + '\n')
        return adjGra
    
    @readInpFileDna
    @writeToOutfile
    def ReconFromOverlapGraphWalk(self,inpFile,dna=None, echoToScreen=False):
        reconStr = dna[0][0:-1]
        for d in dna:
            reconStr += d[-1]
        return reconstr
            

    def StringRecon(self,inpFile,echoToScreen=False):
        """ Solve the String Composition Problem.

        Input: An integer k and a string Text.
        Output: Compositionk(Text) (the k-mers can be provided in any order).

        Sample Input:
        5
        CAATCCAAC

        Sample Output:
        CAATC
        AATCC
        ATCCA
        TCCAA
        CCAAC
        """
        fileparts = inpFile.split('.')
        outFileName = ".".join(fileparts[0:-1]) + "_out." + fileparts[-1]
        with open(inpFile) as f:
            k = int(f.readline().strip())
            dna = f.readline().strip()
        
        kMers = set()

        for substr in [dna[i:i+k] for i in xrange(len(dna)-k+1)]:
            kMers.add(substr)

        with open(outFileName,"w") as f:
            for kMer in kMers:
                f.write(kMer + "\n")     


