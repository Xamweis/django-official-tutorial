from re import search
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Product, Customer, Order


def index(request):
    return render(request, "polls/index.html", {
        "products": Product.objects.all()
    })


def purchase(request):
    if request.method == "GET":
        return index(request)

    new_customer = Customer.objects.create(
        firstName=request.POST["first_name"],
        lastName=request.POST["last_name"],
        street=request.POST["street"],
        plz=request.POST["city"],
        email=request.POST["email"]
    )

    articles_ordered = []
    amounts = []

    for item_key, item_value in request.POST.items():
        if item_key.startswith("product"):
            product_id = search("\d+", item_key).group()
            product_order_count = int(item_value)

            if product_order_count == 0:
                continue

            article = Product.objects.get(id=product_id)
            articles_ordered.append(article)

            amounts.append(product_order_count)

            Order.objects.create(
                customerID=new_customer,
                articleOrdered=article,
                amount=product_order_count
            )

    return render(request, "polls/confirmation.html", {
        "customer": new_customer,
        "articles_ordered": zip(amounts, articles_ordered),
        "total_price": 3456.99
    })

    # return HttpResponseRedirect(reverse("polls:order_confirmation"))


def order_confirmation(request):
    return render(request, "polls/confirmation.html", {})


# class IndexView(generic.ListView):

#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'


#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question': question,
            'error_message': "You didn’t select a choice."
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
