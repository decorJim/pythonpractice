# Given a file size (in bytes) and a cluster size (in bytes), 
# calculate the total number of bytes required to store the file on disk. 
# Assume that the file is stored in clusters, and even if the file size does not perfectly fit into a whole number of clusters, 
# the last cluster must still be fully allocated.

def totalClustersSize(fileSize: int, clusterSize:int):

    # when we store a file on a cluster 
    # we split that file into parts on each cluster
    # if it doesnt fit then the remaining part will still need to be on a cluster

    # we cannot simply divide the fileSize by the clusterSize to know 
    # how many cluster  is needed because not all programming language
    # gives the exact division

    # ex: fileSize = 10 000 and clusterSize = 4096 
    # normally 10 000/4096 = 2.44 but most programming language just rounds down to 2.00
    # so we add the clusterSize to the fileSize
    # 10 000 + 4096 = 14 096 bytes by doing so it is for sure going to be rounded to a number high enough to store the fileSize

    # another problem is that is adding the clusterSize gives an exact multiple of the clusterSize
    # we are wasting 1 cluster that stores nothing
    # ex: fileSize = 10 000 and clusterSize = 100 we really just need 100 clusters
    # but adding clusterSize then 10 100/100 = 101 clusters
    # to fix this we also substract 1 so that the total is no longer a multiple and fits in

    print("fileSize to fit in clusters is ", fileSize)
    print("the cluster size is ", clusterSize)

    numOfClustersNeeded = (fileSize + clusterSize - 1) // clusterSize

    print("the number of clusters needed is ", numOfClustersNeeded)

    totalClustersSize = numOfClustersNeeded * clusterSize

    return totalClustersSize


print(totalClustersSize(10000, 4096))
print()

print(totalClustersSize(10000, 100))
print()

print(totalClustersSize(2509456, 2096))
print()