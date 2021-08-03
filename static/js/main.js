    // 종목 선택 Dropdown (toggle을 이용해 펼치기 / 닫기)
    let dropdown = document.querySelector('.dropdown');
    dropdown.addEventListener('click', dropFunction);


    function dropFunction(event) {
        event.stopPropagation();
        dropdown.classList.toggle('is-active');
    }


    // 종목 선택 시 우측 상단에 종목 명 표시
    function sportsChange() {

    }

    // 회원가입 버튼 클릭 시, 회원 가입 창 출력
    let membershipButton = document.querySelector('#join-button');
    let membershipModal = document.querySelector('#membership-modal');
    membershipButton.addEventListener('click',joinMembership);

    function joinMembership(event) {
        event.stopPropagation();
        membershipModal.classList.toggle('is-active');
    }

    let cancelButton = document.querySelector('.join-cancel');
    cancelButton.addEventListener('click', cancelJoin);

    function cancelJoin(event) {
        event.stopPropagation();
        membershipModal.classList.remove('is-active');
    }

    // 로그인 후 박스 변화
    let loginContainer = document.querySelector('#login-container');
    let loginButton = document.querySelector('#login-button');
    loginButton.addEventListener('click', loginTry);
    function loginTry(id) {
        loginContainer.innerHTML =
        `
        <div class="title is-4" style="text-align: center;">
                    ㅇㅇㅇ님, 환영합니다.
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

    // 로그아웃 후 박스 변화

    /*
    let logoutButton = document.querySelector('#logout-button');
    if (logoutButton) {
        logoutButton.addEventListener('click', logoutTry);
    }
    */
    function logoutTry() {
        console.log('yas')
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
    }