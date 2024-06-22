
var longestConsecutive = function(nums) {
     if (nums.length === 0) {
   return 0;
 }
 if (nums.length === 1) {
   return 1;
 }

 const hset = new Set(nums);
 let currmax = 1;
 const visited = new Set();

 for (let i = 0; i < nums.length; i++) {
   if (!visited.has(nums[i])) {
     console.log(visited);
     let src = nums[i] + 1;
     let j = 1;
     while (hset.has(src)) {
       j++;
       visited.add(src);
       src++;
     }
     currmax = Math.max(j, currmax);
   }
 }

 return currmax;
};

longestConsecutive([1,2,3])