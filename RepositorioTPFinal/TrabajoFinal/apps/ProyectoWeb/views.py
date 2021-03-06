from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.categorias.models import Categoria
from datetime import datetime
from django.http import HttpResponse

class NoticiasList(ListView):
    queryset = Noticia.objects.order_by('-created_date')
    model = Noticia
    template_name = 'noticias.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
class NoticiaCreateView(LoginRequiredMixin,CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'createNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    
    def form_valid(self, form):
        
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(NoticiaCreateView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        user = self.request.user
        context.update({
            'view_type': 'create',
            'user': 'user'
            
        })
        
        return context
     

class NoticiaUpdateView(LoginRequiredMixin,UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'updateNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'view_type': 'update'
        })
        return context


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'detailNoticia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'view_type': 'detail'
        })
        return context


class NoticiaDeleteView(LoginRequiredMixin,DeleteView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'deleteNoticia.html'
    success_url = reverse_lazy('ProyectoWeb:noticia_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context.update({
            'view_type': 'delete'
        })
        return context

   
def PruebaIndex(request):
    return render(request, 'index.html')

class FiltroList(ListView):
    model = Noticia
    template_name = 'filtro.html'

    #def get_queryset(self, *args, **kwargs):
    #    categoria_id = self.kwargs['pk']
    #    return Noticia.objects.filter(category = categoria_id)
    
    def get_queryset(self, *args, **kwargs):
        #fecha = self.kwargs['Fecha_day']
        categoria_id = self.kwargs['pk']
        day = self.request.GET.get('Fecha_day')
        month = self.request.GET.get('Fecha_month')
        year = self.request.GET.get('Fecha_year')
        if day:
            return Noticia.objects.filter(created_date__year = year).filter(created_date__month = month).filter( created_date__day = day).filter(category = categoria_id)
        else:
            return Noticia.objects.filter(category = categoria_id)

        print(day)
        print(month)
        print(year)
        return Noticia.objects.filter(created_date__year = year).filter(created_date__month = month).filter( created_date__day = day).filter(category = categoria_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['fecha'] = FormularioFecha()
        return context

class OrdenarList(ListView):
    model = Noticia
    template_name = 'ordenar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['fecha'] = FormularioFecha()
        return context
    
    def get_queryset(self, *args, **kwargs):
        #fecha = self.kwargs['Fecha_day']
        day = self.request.GET.get('Fecha_day')
        month = self.request.GET.get('Fecha_month')
        year = self.request.GET.get('Fecha_year')
        
        noticias = Noticia.objects.all()
        listaNoticias = []
        print(type(listaNoticias))
        a = len(listaNoticias)
        print(a)
        if day != None and month != None and year != None :
            for noticia in noticias:
                day = int(day)
                month = int(month)
                year = int(year)
                fecha = noticia.created_date
                year_post = int(fecha.strftime('%Y'))
                month_post = fecha.strftime('%m')
                month_post = int(month_post.lstrip ( '0'))
                day_post = fecha.strftime('%d')
                day_post = int(day_post.lstrip ( '0'))
                print (day)
                print (day_post)
                print (month)
                print (month_post)
                #print(type(day))
                
                #print(type(day))
                
                
                print (year)
                print (year_post)
               
                    
                if ((year >= year_post) and (month > month_post)):
                    listaNoticias.append((noticia))
                elif ((year >= year_post) and (month == month_post)):
                    if (day == day_post) or (day > day_post):
                       listaNoticias.append((noticia))
                 
                #if ((day >= day_post)):
            print (listaNoticias)
            return listaNoticias 
        else:
            return Noticia.objects.all()
           
            #print(day)
            #print(month)
            #print(year)
            #return Noticia.objects.filter(created_date__year = year).filter(created_date__month = month).filter( created_date__day = day)
            #return Noticia.objects.filter( created_date__gte= day)
            #return Noticia.objects.order_by('created_date__year')
        
    
    
class NoticiaMyPostsView(ListView):
    model = Noticia
    template_name = 'noticia_myposts.html'

    def get_queryset(self, *args, **kwargs):
        categoria_id = self.kwargs['pk']
        return Noticia.objects.filter(category = categoria_id)
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        print (user)
        return Noticia.objects.filter(author = user)
        print (user)
        pass
      

