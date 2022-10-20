function addNumbers(...rest) {
  const numbers = [...rest];
  return numbers.reduce((sum, number) => { 
    return sum + number
  }, 0)
}