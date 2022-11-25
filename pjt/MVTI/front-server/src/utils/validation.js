function validateEmail(email) {
    // 이메일 형식 정규표현식
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }
   
  export { validateEmail };

function validatePassword(password1) {
    // 패스워드 형식 정규표현식
    var pw = /(?=.*\d)(?=.*[a-zA-ZS]).{8,}/
    return pw.test(String(password1));
}

  export { validatePassword };