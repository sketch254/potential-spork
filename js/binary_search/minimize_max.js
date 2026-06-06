/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
const minimizeMax = function(nums, p) {
    if(p === 0) return 0;
    
    nums.sort((a, b) => a - b);
    const n = nums.length

    const canFormPairs = (maxDiff) => {
        let count = 0;
        let i = 0;
        
        while (i < n - 1 && count < p) {
            if (nums[i + 1] - nums[i] <= maxDiff) {
                count++;
                i += 2;
            } else {
                i++;
            }
        }
        
        return count >= p;

    }

    let low = 0
    let high = nums[n - 1] - nums[0]

    while(low < high){
        const mid = Math.floor((low + high)/2)

        if (canFormPairs(mid)){
            high = mid
        } else {
            low = mid + 1
        }
    }

    return low
}


console.log(minimizeMax([1,2,3,4], 2))
