from django.contrib import admin
from .models import Member,  Post , Category , ForbiddenWord
# Register your models here.

class InlinePost(admin.StackedInline):
    model=Post
    extra =1

class MemberAdmin(admin.ModelAdmin):
    fieldsets=(
        ["Member Information",{'fields':["first_name","last_name","email"]}],
    )
    list_display=("first_name","last_name","email")
    list_filter=["first_name","last_name","email"]
    search_fields=["first_name","last_name","email"]
    model=Post
    inlines=[InlinePost]

class PostAdmin(admin.ModelAdmin):
    fieldsets=(
        ["Post Information",{'fields':["Title","Image","Content","category","tags","author"]}],
    )
    list_display=("Title","author","category","date")
    list_filter=["Title","category","tags","author","date"]
    search_fields=["Title","category","tags","author"]
     
class CategoryAdmin(admin.ModelAdmin):
    fieldsets=(
        ["Category Information",{'fields':["category"]}],
    )
    list_display=("category",)
    list_filter=["category"]
    search_fields=["category"]
    model=Post
    inlines=[InlinePost]
    
class ForbiddenWordAdmin(admin.ModelAdmin):
    fieldsets=(
        ["Forbidden_Word Information",{'fields':["forbidden_word"]}],
    )
    list_display=("forbidden_word",)
    list_filter=["forbidden_word"]
    search_fields=["forbidden_word"]


admin.site.register(Member,MemberAdmin) 
admin.site.register(Post,PostAdmin) 
admin.site.register(Category,CategoryAdmin) 
admin.site.register(ForbiddenWord,ForbiddenWordAdmin) 



