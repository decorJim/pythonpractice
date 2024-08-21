public class Main {
    public static int totalClusterSize(int clusterSize,int fileSize) {
        /** makes sure that the division will round up **/
        int totalSize = fileSize + clusterSize;

        /** if the total ever gives a multiple of clusterSize 1 cluster will be
         * allocated for nothing so -1 prevent perfect multiple
         */
        int nbClusters = (totalSize - 1)/clusterSize;

        return nbClusters*clusterSize;
    }

    public static void main(String[] args) {
        System.out.println(totalClusterSize(1024,5000));
        System.out.println(totalClusterSize(128,5125));
        System.out.println(totalClusterSize(128,8847));
    }
}