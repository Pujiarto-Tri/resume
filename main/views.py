from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
    Skill
)
from django.views import generic
from . forms import ContactForm

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        coding_skills = Skill.objects.filter(is_coding_skill=True)
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolios = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolios"] = portfolios
        context["coding_skills"] = coding_skills
        return context

class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please fill in all the required fields correctly')
        return super().form_invalid(form)

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolios = Portfolio.objects.filter(is_active=True)
        context["portfolios"] = portfolios
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = context['object']
        context["portfolio"] = portfolio
        return context
    

class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(is_active=True)
        context["blogs"] = blogs
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = context['object']
        context["blog"] = blog
        return context
     
