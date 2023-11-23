class UserName:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        
        
def get_user_name(user: UserName) -> UserName:
    """
        Description: 
            유저의 객체를 통해 유저의 이름을 알아내는 함수.
        Param:
            some_module.user.User 클래스의 객체를 파라미터로 받음.
        Return:
            some_module.user_name.UserName 객체를 반환.     
    """

    ...

    return user_name

print(get_user_name.__doc__)
