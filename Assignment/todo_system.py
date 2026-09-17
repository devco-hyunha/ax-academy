import pickle
import os
from datetime import datetime

DATA_FILE = "todo_data.pkl"

# @class User - 사용자 클래스
class User:
    # @init - 사용자 초기화
    # @param {string} username - 사용자 이름
    # @param {string} password - 비밀번호
    # @param {user | admin} [role = 'user'] - 권한
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role  # user or admin


# @class Task - 할 일 클래스
class Task:
    # @init - 할 일 초기화
    # @param {string} title - 할 일 제목
    # @param {string} owner - 작업자
    # @param {int} priority - 우선순위 (1: 높음, 2: 보통, 3: 낮음)
    def __init__(self, title, owner, priority):
        self.title = title
        self.owner = owner
        self.priority = priority  # 1(높음) 2(보통) 3(낮음)
        self.status = "진행중"
        self.created_at = datetime.now()

    # 할 일 완료 메서드
    # 완료 상태로 변경
    def complete(self):
        self.status = "완료"

# @class TodoSystem - 투두 시스템
class TodoSystem:
    # @init - 투두 시스템 초기화
    # @set {List<User>} self.users = [] - 사용자 목록 초기화
    # @set {List<Task>} self.tasks = [] - 할 일 목록 초기화
    # @set {User} self.current_user = None - 로그인 사용자 초기화
    # @call load_data() 를 통해 users, tasks 에 저장된 데이터를 로드
    def __init__(self):
        self.users = []
        self.tasks = []
        self.current_user = None
        self.load_data()

   
    # @save_data - 데이터 저장
    # @call DATA_FILE을 "wb" 쓰기용 바이너리 모드로 오픈
    # pickle.dump((self.users, self.tasks), f) 를 통해 users, tasks 에 데이터를 저장
    def save_data(self):
        with open(DATA_FILE, "wb") as f:
            pickle.dump((self.users, self.tasks), f)

    # @load_data - 데이터 로드
    # @if os.path.exists(DATA_FILE) 를 통해 DATA_FILE 여부를 확인
    # @call DATA_FILE을 "rb" 읽기용 바이너리 모드로 오픈
    # pickle.load(f) 를 통해 users, tasks 에 데이터를 로드
    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "rb") as f:
                self.users, self.tasks = pickle.load(f)

   
    # @register - 회원가입
    # @input {string} username - 아이디
    # @input {string} password - 비밀번호
    # @call User(username, password) 를 통해 입력받은 정보로 유저를 생성
    # @call self.users.append(user) 를 통해 사용자 추가
    # @call self.save_data() 를 통해 데이터 저장
    def register(self):
        username = input("아이디: ")
        password = input("비밀번호: ")
        self.users.append(User(username, password))
        print("회원가입 완료")
        self.save_data()

    # @login - 로그인
    # @input {string} username - 아이디
    # @input {string} password - 비밀번호
    # @if users에 입력 받은 정보가 있는지 확인
    # @True : current_user에 일치하는 유저 정보 저장
    # @False : 로그인 실패
    def login(self):
        username = input("아이디: ")
        password = input("비밀번호: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print("로그인 성공")
                return
        print("로그인 실패")

    # @add_task - 할 일 등록
    # @input {string} title - 제목
    # @input {int} priority - 우선순위 (1: 높음, 2: 보통, 3: 낮음)
    # @call Task(title, self.current_user.username, priority) - 입력받은 정보와, 현재 로그인 사용자의 이름을 입력하여 할 일 생성
    # @call self.tasks.append(task) 를 통해 할 일 추가
    # @call self.save_data() 를 통해 데이터 저장
    def add_task(self):
        title = input("할 일 제목: ")
        priority = int(input("우선순위 (1높음,2보통,3낮음): "))
        task = Task(title, self.current_user.username, priority)
        self.tasks.append(task)
        print("할 일 등록 완료")
        self.save_data()

    # @show_tasks - 내 할 일 목록 보기
    # @loop 할일 목록을 enumerate를 통해 인덱스와 함께 순회
    # @if 할일의 작업자와 현자 사용자의 이름을 비교
    # @True : 할일의 상태, 제목, 우선순위 출력
    def show_tasks(self):
        print("\n--- 내 할 일 목록 ---")
        for i, task in enumerate(self.tasks):
            if task.owner == self.current_user.username:
                print(f"{i}. [{task.status}] {task.title} (우선순위:{task.priority})")

    # @complete_task - 할 일 완료 처리
    # @call show_tasks() 를 통해 할 일 목록 보기
    # @input {int} idx - 완료할 할 일 번호 입력
    # @call self.tasks[idx].complete() 를 통해 idx 번째의 할 일 완료 처리
    # @call self.save_data() 를 통해 데이터 저장
    def complete_task(self):
        self.show_tasks()
        idx = int(input("완료할 번호 선택: "))
        self.tasks[idx].complete()
        print("완료 처리됨")
        self.save_data()

    # ---관리자 기능 --
    # @show_statistics - 통계 보기
    # @set {int} total - 할 일 총 개수
    # @set {int} completed - 완료된 할 일 개수
    # @print 총 할 일: {total}
    # @print 완료된 할 일: {completed}
    def show_statistics(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == "완료"])
        print(f"총 할 일: {total}")
        print(f"완료된 할 일: {completed}")

    # @run - 투두 시스템 실행
    # @loop 반복
    # @print "1.회원가입 2.로그인 3.종료" 메뉴 출력
    # @input {string} choice - 메뉴의 번호 선택
    # @if choice 1 : 회원가입
    # @if choice 2 : 로그인, 로그인 완료 후 user_menu() 실행
    # @if choice 3 : 시스템 루프 종료
    def run(self):
        while True:
            print("\n1.회원가입 2.로그인 3.종료")
            choice = input("선택>> ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
                if self.current_user:
                    self.user_menu()
            elif choice == "3":
                break

    # @user_menu - 사용자 메뉴
    # @loop 반복
    # @print "1.할일등록 2.목록보기 3.완료처리 4.통계 5.로그아웃" 메뉴 출력
    # @input {string} choice - 메뉴의 번호 선택
    # @if choice 1 : 할 일 등록
    # @if choice 2 : 내 할 일 목록 보기
    # @if choice 3 : 할 일 완료 처리
    # @if choice 4 : 통계 보기
    # @if choice 5 : 로그아웃, 로그아웃 완료 후 루프 종료
    def user_menu(self):
        while True:
            print("\n1.할일등록 2.목록보기 3.완료처리 4.통계 5.로그아웃")
            choice = input("선택>> ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.current_user = None
                break


# @main - 메인 함수
if __name__ == "__main__":
    # @call TodoSystem() 를 통해 투두 시스템 객체 생성
    system = TodoSystem()

    # @if 관리자 계정이 없는 경우 관리자 계정 생성
    # @call User("admin", "1234", "admin") 를 통해 관리자 계정 생성
    # @call system.users.append() 를 통해 관리자 계정 추가
    # @call system.save_data() 를 통해 데이터 저장
    if not any(u.role == "admin" for u in system.users):
        system.users.append(User("admin", "1234", "admin"))
        system.save_data()

    # @call system.run() 를 통해 투두 시스템 실행
    system.run()


# system = TodoSystem() 을 통해 객체 생성
    # @if 관리자 계정이 없으면 관리자 계정 생성
    # system.run() 을 통해 투두 시스템 실행

# @run - 투두 시스템 실행
    # "1.회원가입 2.로그인 3.종료" 메뉴 출력
    # choice - 메뉴의 번호 선택
    # choice 1 : 회원가입
    # choice 2 : 로그인, 로그인 완료 후 user_menu() 실행
    # choice 3 : 시스템 루프 종료

# choice 1 :
    # @register - 회원가입
    # @input username, password
    # User(username, password)로 user 생성
    # users.append(user) 를 통해 사용자 추가
    # save_data() 를 통해 데이터 저장

# choice 2 :
    # @login - 로그인
    # @input username, password
    # users에 입력 받은 정보가 있는지 확인
    # True : current_user에 일치하는 유저 정보 저장
    # False : 로그인 실패
    # user_menu() 실행


    # @user_menu - 사용자 메뉴
    # "1.할일등록 2.목록보기 3.완료처리 4.통계 5.로그아웃" 메뉴 출력
    # user choice - 메뉴의 번호 선택
    # user choice 1 : 할 일 등록
    # user choice 2 : 내 할 일 목록 보기
    # user choice 3 : 할 일 완료 처리
    # user choice 4 : 통계 보기
    # user choice 5 : 로그아웃, 로그아웃 완료 후 루프 종료 -> run의 메뉴 출력으로 이동
    
    # user choice 1 :
        # @add_task - 할 일 등록
        # @input title, priority
        # Task(title, self.current_user.username, priority)로 task 생성
        # tasks.append(task) 를 통해 할 일 추가
        # save_data() 를 통해 데이터 저장

    # user choice 2 :
        # @show_tasks - 내 할 일 목록 보기
        # @loop 할일 목록을 enumerate를 통해 인덱스와 함께 순회
        # @if 할일의 작업자와 현자 사용자의 이름을 비교
        # @True : 할일의 상태, 제목, 우선순위 출력

    # user choice 3 :
        # @complete_task - 할 일 완료 처리
        # show_tasks() 를 통해 할 일 목록 보기
        # idx - 완료할 할 일 번호 입력
        # tasks[idx].complete() 를 통해 idx 번째의 할 일 완료 처리
        # save_data() 를 통해 데이터 저장

    # user choice 4 :
        # @show_statistics - 통계 보기
        # total - 할 일 총 개수 출력
        # completed - 완료된 할 일 개수 출력

    # user choice 5 :
        # @logout - 로그아웃
        # current_user = None 로 로그아웃 처리
        # run의 메뉴 출력으로 이동

# choice 3 :
    # @exit - 투두 시스템 종료