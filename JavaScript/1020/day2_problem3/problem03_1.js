  // 1-1
const savedFile = {
  name: 'profile',
  extension: 'jpg',
  size: 29930
}
function fileSummary({name, extension, size}) {
    console.log(`The file ${name}.${extension} is size of ${size} bytes.`)
}
fileSummary(savedFile);


  // 1-2
const data = {
  username: 'myName',
  password: 'myPassword',
  email: 'my@mail.com',
}

const {username, password, email} = data