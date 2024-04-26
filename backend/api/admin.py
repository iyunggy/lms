from django.contrib import admin
from api import models 
from import_export.admin import ImportExportModelAdmin

class TeacherAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Teacher, TeacherAdmin)

class CategoryAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Category, CategoryAdmin)

class CourseAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Course, CourseAdmin)

class VariantAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Variant, VariantAdmin)

class VarianItemAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.VariantItem, VarianItemAdmin)

class QuestionAnswerAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Question_Answer, QuestionAnswerAdmin)

class QuestionAnswerMessageAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Question_Answer_Message, QuestionAnswerMessageAdmin)

class CartAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Cart, CartAdmin)

class CartOrderAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.CartOrder, CartOrderAdmin)

class CartOrderItemAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.CartOrderItem, CartOrderItemAdmin)

class CertificateAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Certificate, CertificateAdmin)

class CompletedLessonAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.CompletedLesson, CompletedLessonAdmin)

class EnrolledCourseAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.EnrolledCourse, EnrolledCourseAdmin)

class NoteAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Note, NoteAdmin)

class ReviewAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Review, ReviewAdmin)

class NotificationAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Notification, NotificationAdmin)

class CouponAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Coupon, CouponAdmin)

class WishlistAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Wishlist)

class CountryAdmin(ImportExportModelAdmin):
  pass
admin.site.register(models.Country, CountryAdmin)
