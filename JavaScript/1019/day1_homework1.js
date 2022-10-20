// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log(nums[i])
}

// i를 재정의하며 for문을 수행하기 때문에 const가 아닌 let으로 정의해야 한다.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// for of를 사용하여 값이 출력되게 하였고 nums의 값은 number형식이다.