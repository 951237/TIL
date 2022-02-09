// id 선택하기
const title = document.querySelector("#title");

// 색변수 지정하기
const BASE_COLOR = "rgb(52, 73, 94)"; // #으로 시작하는 색깔로 하면 색이 변하지 않음. why?
const OTHER_COLOR = "#bdc3c7";

// 클릭햇을 때 동작하는 함수
function handleClick() {
    const currentColor = title.style.color;
    if (currentColor === BASE_COLOR) {
        title.style.color = OTHER_COLOR;
    } else {
        title.style.color = BASE_COLOR;
    }
}

// 초기화 함수
function init() {
    title.style.color = BASE_COLOR;
    // title.addEventListener("click", handleClick); //click를 했을 때 동작하는 함수 연결
    title.addEventListener("mouseenter", handleClick); //마우스가 글자위에 올라갔을 때 동작하는 함수 연결
}

// 함수 실행 파이선에서 main()
init();