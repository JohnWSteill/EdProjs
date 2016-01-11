import UCSD_Ros as u
import pdb
r = u.UCSD_Ros_Solver()
#r.StringRecon("Data\dataset_197_3.txt")
#r.getOverlap('Data/dataset_198_9.txt')
#r.getOverlap(r'Data\dataset_198_9.txt')
#r.getDeBrujinFromKmers('Data/dataset_200_7.txt')
#r.getDeBrujinK('Datra/dataset_199_6.txt')
#r.getEulerCycle('Data/dataset_203_2.txt')
#r.getEulerPath(r'Data\dataset_203_5.txt')
#r.getStringRecon(r'Data\dataset_sampG.txt')
#r.getStringRecon(r'Data\dataset_203_6.txt')
#r.getkCircStr(r'Data\dataset_203_10.txt')
r.getOuterStringReconFromPair(r'Data\dataset_204_14.txt')

