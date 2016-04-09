import pdb
import random

def writeToOutfile(fun):
    def wrapper(*args,**kwargs):
        ans = fun(*args,**kwargs)
        fileparts = args[1].split('.')
        outFileName = ".".join(fileparts[0:-1]) + "_out." + fileparts[-1]        
        with open(outFileName,'w') as f:
            for a in ans: 
                f.write(a)
    return wrapper

class readInpDecorator():
    def __init__(self,varList):
        self.varList = varList
    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            with open(args[1]) as f:
                inputData = f.readlines()
            if len(self.varList)==1:
                kwargs = {self.varList[0]: [el.strip() for el in inputData]}
            elif len(self.varList[0])==1:
                kwargs = {self.varList[0]: inputData[0].strip()}
                kwargs[self.varList[1]] = [el.strip() for el in inputData[1:]]
            else:
                kwargs = {el:int(d) for el,d in
                              zip(self.varList[0],inputData[0].split())}
                kwargs[self.varList[1]] = [el.strip() for el in inputData[1:]]
            ans = fun(*args, **kwargs)
        return wrapper
                        

def readInpFileKDna(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            k = int(f.readline())
            dna = f.readline().strip()
        ans = fun(*args,dna = dna, k = k)
    return wrapper

def readInpFileK(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            k = int(f.readline())            
        ans = fun(*args,k = k)
    return wrapper

def readInpFileK_Kmers(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            k = int(f.readline())
            dna = [el.strip() for el in f.readlines()]
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
    @readInpDecorator([['k','d'],'kdmers'])
    @writeToOutfile
    def getOuterStringReconFromPair(self,inpfile,k=None, d = None, kdmers=None):
        ans = ""
        while ans == "":
            ans = self.getStringReconFromPair(k,d,kdmers)
        return ans

    def getStringReconFromPair(self,k,d,kdmers):
        def getHT(kdmerL):
            for s in kdmerL:
                head = (s[:k-1],s[k+1:-1])
                tail = (s[1:k],s[k+2:])
                yield (head,tail)

        deBrujin = {}
        for (h,t) in getHT(kdmers):
            addKeyAndValTodeBrujin(deBrujin,h,t)

            
        cycle = self.getEulerPath(None,deBrujin)
        pref = ( cycle[0][0][0] + "".join([el[1][0][-1] for el in cycle]))
        suff = ( cycle[0][0][1] + "".join([el[1][1][-1] for el in cycle]))
        #pdb.set_trace()
        print (len(pref),
               len([el for el,el1 in zip(pref[k+d:],suff[:-k-d]) if el != el1]))
        if pref[k+d:] == suff[:-k-d]:
            return pref + suff[-k-d:]
            
        return ""

        

        

    
    @readInpDecorator([['k','d'],'kdmers'])
    @writeToOutfile
    def outerStringSpelledByKdmers(self, inpfile, k=None, d=None, kdmers=None):
        return self.stringSpelledByKdmers(k,d,kdmers)

    def stringSpelledByKdmers(self,k,d,kdmers):
        nodeJ = lambda(x):x[0] + "".join(el[-1] for el in x[1:])
        pref = nodeJ([el[:k] for el in kdmers])
        suff = nodeJ([el[k+1:] for el in kdmers])
        pdb.set_trace()
        if pref[k+d:] == suff[:-k-d]:
            return pref + suff[-k-d:]
        return ""      
            

    @readInpFileK
    @writeToOutfile
    def getkCircStr(self,inpfile, k = None):
        keys = [bin(el)[2:].zfill(k-1) for el in range(2**(k-1))]
        g = {k:[k[1:]+'0',k[1:]+'1'] for k in keys}
        cStr = self.getEulerCycle(None, g = g)
        kmers = cStr.split('->')
        
        return kmers[0] + "".join([kmer[-1] for kmer in kmers[1:-k+1]])
        

    
    @readInpFileK_Kmers
    @writeToOutfile
    def getStringRecon(self, inpfile, k = None, dna = None):
        deBrujin = {}
        for d in dna:
            addKeyAndValTodeBrujin(deBrujin, d[:-1],d[1:])
        cStr = self.getEulerPath(inpfile, g = deBrujin)
        kmers = cStr.split('->')
        return kmers[0] + "".join([kmer[-1] for kmer in kmers[1:]])
        
    
    #@readInpFileDirGraph
    #@writeToOutfile
    def getEulerPath(self, inpFile, g = None):
        edgeImb = {}

        for (h,t) in g.items():
            if h in edgeImb:
                edgeImb[h] += len(g[h])
            else:
                edgeImb[h] = len(g[h])
            for t_i in t:
                if t_i in edgeImb:
                    edgeImb[t_i] -= 1
                else:
                    edgeImb[t_i] = -1
        head = edgeImb.keys()[edgeImb.values().index(1)]
        tail = edgeImb.keys()[edgeImb.values().index(-1)]
        if tail in g:
            g[tail].append([head])
        else:
            g[tail] = [head]
        cycle = self.eulerAlgorithm(g)
        fakeNodeIndx = cycle.index([tail,head])
        cycle = cycle[fakeNodeIndx+1:] + cycle[:fakeNodeIndx]
        return cycle
        c = [cycle[0][0]]
        for el in cycle: 
            c.append(el[1])
        return '->'.join(c)
        
    

    #@readInpFileDirGraph
    #@writeToOutfile
    def getEulerCycle(self, inpFile, g = None):
        cycle = self.eulerAlgorithm(g)
        c = [cycle[0][0]]
        for el in cycle:
            c.append(el[1])
        return '->'.join(c)

    def getAndRemoveAnyTail(self,g,head):
        #tail = g[head].pop(random.choice(range(len(g[head]))))
        tail = g[head].pop()
        if not g[head]:
            g.pop(head)
        return tail

    def eulerAlgorithm(self,g):
        head = min(g.keys())
        cycle = [(head,self.getAndRemoveAnyTail(g,head))]
        
            
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
                    tail = self.getAndRemoveAnyTail(g,pT)
                except:
                    break
                cycle.append([pT,tail])
                
        return cycle

    #@readInpFileKDna
    #@writeToOutfile
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


