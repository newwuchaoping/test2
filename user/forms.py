from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)
    captcha = CaptchaField()
class RegisterForm(forms.Form):
    danwei_choices = (
        ('yizhong', '一中'),
        ('erzhong', '二中'),
    )
    username = forms.IntegerField(min_value=1000000, max_value=9999999)
    email = forms.EmailField(required=True)
    nickname = forms.CharField(required=True, max_length=10)
    password = forms.CharField(required=True, min_length=5)
    danwei = forms.ChoiceField(label='所在单位', choices=danwei_choices, required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
class UserInfoForm(forms.Form):
    gender_choices = (
		('male', '男'),
		('female', '女'),
	)
    leibie_choices = (
        ('guanliyuan', '管理员'),
        ('jiaoshi', '教师'),
        ('xuesheng', '学生'),
    )
    danwei_choices = (
        ('yizhong', '一中'),
        ('erzhong', '二中'),
    )
    nianji_choices = (
        ('yinianji', '一年级'),
        ('ernianji', '二年级'),
        ('sannianji', '三年级'),
    )
    nick_name = forms.CharField(label='姓    名',required=True, max_length=50)
    birthday = forms.DateField(label='生    日',required=True)
    gender = forms.ChoiceField(label='性    别',choices=gender_choices, required=True)
    leibie = forms.ChoiceField(label='人员类别',choices=leibie_choices, required=True)
    danwei = forms.ChoiceField(label='所在单位',choices=danwei_choices, required=True)
    nianji = forms.ChoiceField( label='所在年级', choices=nianji_choices, required=True)