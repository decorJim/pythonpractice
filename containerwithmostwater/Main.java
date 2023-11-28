public class Main {

    public static int containerWithMostWater(int[] height) {
        /** 2 pointers at start and end of array we want the longuest base */
        int i=0;
        int j=height.length-1;

        /** start at 0 at if current Area bigger set it */
        int maxArea=0;

        while(i<j) {
            if(Math.min(height[i],height[j])*(j-i)>maxArea) {
                maxArea=Math.min(height[i],height[j])*(j-i);
            }

            /** unlike python else if necessary or next if will use modified height[i] */
            if(height[i]<height[j]) {
                i++;
            }
            else if(height[i]>height[j]) {
                j--;
            }
            else {
                i++;
            }
        }

        System.out.println("final:"+maxArea);
        return maxArea;
    }

    public static void main(String[] args) {
        /**
         *  1,8,6,2,5,4,8,3,7
         *  0 1 2 3 4 5 6 7 8
         *
         */
        int [] height = {1,8,6,2,5,4,8,3,7};
        containerWithMostWater(height);
    }
}