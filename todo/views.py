from .forms import AddTodoForm
from .models import Todo
from common.util.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from urllib.parse import urlencode


# Create your views here.
class TodoList(View, TemplateView):
    template_name = "todo/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "To-do's"
        context["link"] = "todo"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        trash_status = bool(request.GET.get("trash_status", None))

        if trash_status:
            messages.success(request, "Todo Item Deleted!")

        form = AddTodoForm()
        todos = Todo.objects.filter(user=request.user).order_by("-created_at")

        context["form"] = form
        context["todos"] = todos

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        trash_status = bool(request.GET.get("trash_status", None))

        if trash_status:
            messages.success(request, "Todo Item Deleted!")

        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Todo created successfully!")

        todos = Todo.objects.filter(user=request.user).order_by("-created_at")

        context["form"] = form
        context["todos"] = todos

        return render(request, self.template_name, context)


class TodoToggleCheckbox(View, TemplateView):

    def post(self, request, *args, **kwargs):

        todo_id = request.POST.get("todo_id", None)
        is_completed = request.POST.get("is_completed") == "true"

        if not todo_id:
            return JsonResponse({"error": "Todo ID is required."}, status=400)

        try:
            todo = Todo.objects.get(id=todo_id, user=request.user)
            todo.is_completed = is_completed
            todo.save()
            messages.success(request, "Todo Updated!")
            return JsonResponse({"success": True, "is_completed": todo.is_completed})
        except Todo.DoesNotExist:
            messages.error(request, "Error!")
            return JsonResponse({"error": "Todo not found."}, status=404)


class TodoTrash(View, TemplateView):

    def get(self, request, *args, **kwargs):

        todo_id = kwargs.pop("todo_id", None)
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()

        url = reverse("todo:todo")

        query_params = {"trash_status": 1}

        url_with_params = f"{url}?{urlencode(query_params)}"

        return redirect(url_with_params)
