const currentDate = new Date();

const year = currentDate.getFullYear();
const month = currentDate.getMonth() + 1;
const day = currentDate.getDate();
const hours = currentDate.getHours();
const minutes = currentDate.getMinutes();
const seconds = currentDate.getSeconds();

const formattedDate = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')} ${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

document.write(formattedDate);


// localStorage에 저장된 값을 컬러모드로 사용할 수 있습니다.
const colorMode = window.localStorage.getItem('color_mode');
window.document.body.classList.add(colorMode);

// 웹뷰로 사용되는 경우에 userAgent에 앱의 컬러모드 값을 전달받아 사용할 수도 있습니다. 
// 이 경우 웹뷰가 열릴 때 앱팀의 지원을 받아 변경된 UA값을 전달 해 줘야 합니다
const isDarkMode = window.navigator.userAgent.inclues('{isDark property}');
if(isDarkMode){
  window.document.body.classList.add('dark')
}

// 앞서 사용한 prefers-color-scheme 값을 확인 해 시스템의 컬러모드 초기값으로 사용할 수도 있습니다.
if(window.matchMedia('(prefers-color-scheme: dark)').matches){
   window.document.body.classList.add('dark')
}

// css media query 동작과 유사하게, 시스템의 컬러모드가 변경될 때 마다 이를 웹에 반영해 줄 수도 있습니다.
const mediaQueryList = window.matchMedia('(prefers-color-scheme: dark)');
mediaQueryList.addEventListner('change', (e) => {
  if(e.matches){
     window.document.body.classList.add('dark')
  } else {
     window.document.body.classList.remove('dark')
  }
})