import java.util.regex.Pattern;

public class Main {
    public static int totalClusterSize(int clusterSize,int fileSize) {
        /** divison round to higher number */
        int nbClusters=Math.ceilDiv(fileSize,clusterSize);
        System.out.println("nbClusters:"+nbClusters);
        int totalSize=nbClusters*clusterSize;
        return totalSize;
    }

    public static void main(String[] args) {
        System.out.println(totalClusterSize(1024,5000));
        System.out.println(totalClusterSize(128,5125));
        System.out.println(totalClusterSize(128,8847));
    }
}