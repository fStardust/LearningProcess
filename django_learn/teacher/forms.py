from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20)
    password = forms.CharField(
        label='密码', max_length=8, min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': '请输入6-8位长度密码'}),
        error_messages={'min_length': '密码长度小于6位', 'max_length': '密码长度大于6位', }
    )
    password_repeat = forms.CharField(label='确认密码', widget=forms.PasswordInput())

    def clean(self):  # 多字段
        cleaned_data = super().clean()  # 继承父类

        # 增加提示信息
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password != password_repeat:
            msg = '密码不一致'
            self.add_error('password_repeat', msg)

    def clean_username(self):  # 单字段
        pass
