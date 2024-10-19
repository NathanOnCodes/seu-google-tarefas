from django.contrib import admin
from tarefas.models import Tarefa, ListaTarefa
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
# Register your models here.

class ListaTarefaAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    select_fields_form_class = SelectableFieldsExportForm
    list_display = ('nome', 'slug')
    list_filter = ['nome', 'tarefas__concluida']
    search_fields = ['nome']
    prepopulated_fields = {'slug': ('nome',)}

class TarefaAdmin(ModelAdmin):
    list_display = ('nome', 'concluida')
    list_filter = ['nome']
    search_fields = ['nome']
    
#admin.site.register(ListaTarefaAdmin)
admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(ListaTarefa, ListaTarefaAdmin)



