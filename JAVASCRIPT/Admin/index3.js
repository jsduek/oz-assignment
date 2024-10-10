const form = document.getElementById("form")

form.addEventListener("submit", function(event){
  event.preventDefault()

  let userID = event.target.inputId.value
  let userPw1 =event.target.inputPW4.value
  let userPw2 =event.target.inputPWW5.value
  let userName =event.target.inputName2.value
  let userTel =event.target.inputTel.value
  let userEmail =event.target.inputEmail.value
  let userGender =event.target.gender.value
  
  if(userID.length <= 6){
    alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
  }else if(userID.length > 30){
    alert("아이디가 너무 깁니다. 30자 미만으로 입력해주세요.")
    return
  }

  if(userPw1 !== userPw2){
    alert("비밀번호가 일치하지 않습니다.")
    return
  }else if(userPw1 >= 8 || userPw2 < 30){
    alert("비밀번호는 8자 이상 30자 미만으로 입력해주세요.")
    return
  }
  
  

  document.body.innerHTML = ""
  document.write(`<p>${userID}님 환영합니다</p>`)
  document.write(`<p>회원 가입 시 입력하신 내역은 다음과 같습니다.</p>`)
  document.write(`<p>아이디 : ${userID}</p>`)
  document.write(`<p>이름 : ${userName}</p>`)
  document.write(`<p>전화번호 : ${userTel}</p>`)
  
})

const $checkbox = document.querySelector('.check');

const isUserColorTheme = localStorage.getItem('color-theme');
const isOsColorTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';

const getUserTheme = () => (isUserColorTheme ? isUserColorTheme : isOsColorTheme);

window.onload = function () {
  if (getUserTheme === 'dark') {
    localStorage.setItem('color-theme', 'dark');
    document.documentElement.setAttribute('color-theme', 'dark');
    $checkbox.setAttribute('checked', true);
  } else {
    localStorage.setItem('color-theme', 'light');
    document.documentElement.setAttribute('color-theme', 'light');
  }
};

$checkbox.addEventListener('click', e => {
  if (e.target.checked) {
    localStorage.setItem('color-theme', 'light');
    document.documentElement.setAttribute('color-theme', 'dark');
  } else {
    localStorage.setItem('color-theme', 'light');
    document.documentElement.setAttribute('color-theme', 'light');
  }
});