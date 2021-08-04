// $(document).ready(function(){
//     sportlist();
// });



// 종목 선택 Dropdown (toggle을 이용해 펼치기 / 닫기)
let dropdown = document.querySelector('.dropdown');
dropdown.addEventListener('click', dropFunction);

function dropFunction(event) {
    event.stopPropagation();
    dropdown.classList.toggle('is-active');
}


// 종목 선택 시 우측 상단에 종목 명 표시
function sportsChange(item) {
    document.getElementById('dropdown-main').textContent = item
    document.getElementById('select-item').textContent = item

    // 일정을 불러와서 우측 하단에 보여주는 함수
    $.ajax({
        type: 'POST',
        url: '/schedule',
        data: {item_give: item},
        success: function(response) {
            if (response['result'] === 'success') {
                alert('연결 성공!');
            }
        }
    })
}

// 종목 33개 드롭다운에 뿌려주기
function dropdownMaking() {
    $.ajax({
        type: 'GET',
        url: '/makeDropdown',
        data: {},
        success: function(response) {
            if (response['result'] === 'success') {
                alert('연결 성공!');
            }
        }
    })
}

// 회원가입 버튼 클릭 시, 회원 가입 창 출력
// let membershipButton = document.querySelector('#join-button');
// let membershipModal = document.querySelector('#membership-modal');
// membershipButton.addEventListener('click',clickJoinButton);

function clickJoinButton(event) {
    let membershipModal = document.querySelector('#membership-modal');

    membershipModal.classList.toggle('is-active');
}

let cancelButton = document.querySelector('.join-cancel');
cancelButton.addEventListener('click', cancelJoin);

function cancelJoin(event) {
    let membershipModal = document.querySelector('#membership-modal');

    membershipModal.classList.remove('is-active');
}

function postJoin() {
    let new_id = $('#join-id-input').val();
    let new_pw = $('#join-pw-input').val();

    $.ajax({
        type: "POST",
        url: "/join",
        data: {id_give: new_id, pw_give: new_pw},
        success: function(response) {
            if (response['result'] === 'success') {
                alert('가입 완료!');
            }
            else if (response['result'] === 'same') {
                alert('중복된 아이디 입니다.');
            }
            else if (response['result'] === 'blank') {
                alert('아이디를 입력해주세요.');
            }
        }
    })
}

// 로그인 후 박스 변화
// let loginContainer = document.querySelector('#login-container');
// let loginButton = document.querySelector('#login-button');
// loginButton.addEventListener('click', loginTry);
function loginTry() {
    let loginContainer = document.querySelector('#login-container');
    let inputId = $('#login-id').val();
    let inputPw = $('#login-pw').val();

    $.ajax({
        type: 'POST',
        url: '/login',
        data: {login_id: inputId, login_pw: inputPw},
        success: function(response) {
            if (response['result'] === 'success') {
                userName = response['userName'];
                loginContainer.innerHTML =
                                            `
                                            <div class="title is-4" style="text-align: center;">
                                                        ${userName}님, 환영합니다.
                                                    </div>
                                                    <div class="login-buttons">
                                                        <div class="field" style="float: right;">
                                                            <p class="control">
                                                            <button class="button is-success" id="logout-button" onclick="logoutTry()">
                                                                로그아웃
                                                            </button>
                                                            </p>
                                                        </div>
                                                        <div id="bookmark-button" class="field" style="float: right; margin-right: 10px;">
                                                            <p class="control">
                                                            <button class="button is-success">
                                                                내 즐겨찾기
                                                            </button>
                                                            </p>
                                                        </div>
                                                    </div>
                                            `
            }
            else if (response['result'] === 'idError') {
                alert('ID가 틀렸습니다.')
            }
            else if (response['result'] === 'pwError') {
                alert('Pw가 틀렸습니다.')
            }
        }
    })


}

// 로그아웃 후 박스 변화

/*
let logoutButton = document.querySelector('#logout-button');
if (logoutButton) {
    logoutButton.addEventListener('click', logoutTry);
}
*/

function logoutTry() {
    $.ajax({
        type: 'GET',
        url: '/logout',
        data: {},
        success: function(response) {
            if (response['result'] === 'success') {
                let loginContainer = document.querySelector('#login-container');
                loginContainer.innerHTML =
                `
                <div class="field">
                            <p class="control has-icons-left has-icons-right">
                            <input class="input" id="login-id" type="id" placeholder="ID">
                            <span class="icon is-small is-left">
                                <i class="fas fa-user"></i>
                            </span>
                            <span class="icon is-small is-right">
                                <i class="fas fa-check"></i>
                            </span>
                            </p>
                        </div>

                        <div class="field">
                            <p class="control has-icons-left">
                            <input class="input" id="login-pw" type="password" placeholder="Password">
                            <span class="icon is-small is-left">
                                <i class="fas fa-lock"></i>
                            </span>
                            </p>
                        </div>
                        <div class="login-buttons">
                            <div class="field" style="float: right;">
                                <p class="control">
                                <button class="button is-success" id="login-button">
                                    로그인
                                </button>
                                </p>
                            </div>
                            <div id="join-button" class="field" style="float: right; margin-right: 10px;">
                                <p class="control">
                                <button class="button is-success modal-button" data-target="membership-modal" aria-haspopup="true">
                                    회원가입
                                </button>
                                </p>
                            </div>
                        </div>
                `
                window.location.reload();
            }
        }
    })
}




    //종목리스트 생성
    // function sportslist(){
    //     $("#dropdown-menu").html("");
    //     for(let i = 0; i < sportlist.length; i++){
    //         makeDropdown(sportlist[i])
    //     }
    // }

    // function makeDropdown(sport){
    //     let temphtml = `<a href="#" class="dropdown-item" onclick="sportsChange()">${sport}</a>`
    //     $("#dropdown-menu").append(temphtml)
    // }