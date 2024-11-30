public class Main {
    public static int totalClusterSize(int clusterSize,int fileSize) {
        /** when dividing a number in java if its not a perfect multiple
         *  the number will be automatically round down so directly dividing fileSize
         *  will always end up with 1 cluster short for remaining data if
         *  its not a perfect multiple
         *
         *  to fix that we add another clusterSize - 1 to the fileSize
         *  then we get a bigger total so that always allocates a
         *  cluster for the remaining data
         */
        int totalSize = fileSize + clusterSize;
        
        int nbClusters = (totalSize - 1)/clusterSize;

        return nbClusters*clusterSize;
    }

    public static void main(String[] args) {
        System.out.println(totalClusterSize(1024,5000));
        System.out.println(totalClusterSize(128,5125));
        System.out.println(totalClusterSize(128,8847));
    }
}