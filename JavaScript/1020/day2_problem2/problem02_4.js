const users = [
  { name: 'John', age: 31, isMarried: true, balance: 100, },
  { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
  { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
  { name: 'Robert', age: 27, isMarried: false, balance: 400, },
  { name: 'Tom', age: 35, isMarried: true, balance: 500, },
]

const newUsers = users.map(({name, age, isMarried, balance}) => {
  return {name, age, isMarried, balance, isAlive: true}
})

// const newUsers = users.map((element) => {
//   return {name: element.name, age: element.age, isMarried: element.isMarried, balance: element.balance, isAlive: true}
// })

// console.log(newUsers)