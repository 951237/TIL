// html문서에서 버튼 부분을 선택해서 변수로 지정하기 
const moreBtn = document.querySelector('.info .metadata .moreBtn');

// html에서 타이틀 부분을 찾아서 변수로 지정하기
const title = document.querySelector('.info .metadata .title');

moreBtn.addEventListener('click', () => {  // 클릭을 하면 
    moreBtn.classList.toggle('clicked');  // 버튼의 클래스 부분이 'clicked'로 사라졌다, 있다가 토글 기능을 수행
    title.classList.toggle('clamp');  // 타이틀 부분의 클래스의 리스트가 'clamp'가 있다가 없다가 토글기능을 수행
});