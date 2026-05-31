/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCapability = function(nums, k) {
    const canRob = (cap) => {
        let count = 0;
        let last = -2;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] <= cap && i - last > 1) {
                count++;
                last = i;
                if (count >= k) return true;
            }
        }
        return count >= k;
    };
    
    let left = 1;
    let right = Math.max(...nums);
    let ans = right;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canRob(mid)) {
            ans = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
};

console.log(minCapability([2,3,4,5,6], 3))

