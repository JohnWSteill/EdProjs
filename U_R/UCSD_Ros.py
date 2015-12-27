def writeToOutfile(fun):
    def wrapper(*args,**kwargs):
        ans = fun(*args,**kwargs)
        fileparts = args[1].split('.')
        outFileName = ".".join(fileparts[0:-1]) + "_out." + fileparts[-1]        
        with open(outFileName,'w') as f:
            for a in ans: 
                f.write(a)
    return wrapper

def readInpFileDna(fun):
    def wrapper(*args,**kwargs):
        with open(args[1]) as f:
            dna = [el.strip() for el in f.readlines()]
        ans = fun(*args,dna = dna)
    return wrapper

# http://docs.sublimetext.info/en/latest/basic_concepts.html
class UCSD_Ros_Solver(object): 
    """ This class performs Rosalind Project solutions. 

    Usage is as follows:  
    r = UCSD_Ros_Solver() 
    r.myProb("MyData.txt")
    Assumes that MyData.txt is in working directory or getwd()/Data 
    """

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


