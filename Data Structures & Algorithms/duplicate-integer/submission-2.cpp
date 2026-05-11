class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            // Start j from i + 1 to avoid self-comparison and redundant checks
            for (int j = i + 1; j < nums.size(); j++) { 
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};