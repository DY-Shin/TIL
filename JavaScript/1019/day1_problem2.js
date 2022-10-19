function palindrome(str) {
    let len = str.length;
    for (let i = 0; i < len / 2; i += 1){
      if(str[i] !== str[len - i - 1]) {
        return 'false'
      }
    }
    return 'true'
  }

console.log(palindrome('level'))
console.log(palindrome('hi'))
  
  // 출력
  // palindrome('level') => true
  // palindrome('hi') => false