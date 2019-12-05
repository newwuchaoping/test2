import xadmin
from xadmin import views
from . import models
class UserProfileAdmin(object):
    list_display=['username','nickname','birthday','gender','leibie','danwei','phone']
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
class GlobalSetting(object):
    site_title = "学习分析在线服务系统"
    site_footer = "天津师范大学@教育科学学院|现代教育技术1811030103"
    menu_style = "accordion"
xadmin.site.unregister(models.UserProfile)
xadmin.site.register(models.UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
