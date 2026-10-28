class Solution {
public:
    int maxArea(vector<int>& heights) {
        // two pointer method

        int left =0, right = heights.size()-1;
        int maxArea = 0, area = 0;
        while (left < right){
            area = (right-left)*min(heights[left],heights[right]);
            maxArea = max(area,maxArea);
            if (heights[left]>heights[right])
                right--;
            else
                left ++;
        }
        return maxArea;
        
    }
};
