from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.db.models import Count


from django.core.paginator import Paginator, EmptyPage, Page, PageNotAnInteger

from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm


def main(request):
    quotes = Quote.objects.prefetch_related('tags').all().order_by('id')
    quotes_paginator = Paginator(quotes, 6)
    page_num = request.GET.get('page')
    page = quotes_paginator.get_page(page_num )

    context = {
        'quotes': quotes,
        'tags': [],
        'count': quotes_paginator.count,
        'page': page,
        # 'topTenTags': topTenTags,

    }

    return render(request, 'index.html', context)


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)

    return render(request, 'author_detail.html', {'author': author})


def create_tags(tags: list):
    tags_from_db = []

    for name_tag in tags:
        try:
            tag = Tag(name=name_tag)
            tag.save()
            tag.refresh_from_db()
            tags_from_db.append(tag)
        except Exception as err:
            print(err)
            tag = Tag.objects.filter(name=name_tag).first()
            tags_from_db.append(tag)

    return tags_from_db


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = form.save()
            tags = form.cleaned_data['tags'].split(',')
            tags = create_tags(tags)

            for tag in tags:
                quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            form = QuoteForm()
        return render(request, 'add_quote.html', {'form': form})

    return render(request, 'add_quote.html', {'form': QuoteForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            form = AuthorForm()
        return render(request, 'add_author.html', {'form': form})

    return render(request, 'add_author.html', {'form': AuthorForm})


def about_author(request, author_id):
    author = Author.objects.get(id=author_id)

    return render(request, 'about_author.html', {'author': author})


def search_tag(request, tag):
    tag = Tag.objects.get(name=tag)
    quotes = Quote.objects.filter(tags=tag)

    return render (request, "search_tag.html", {"quotes": quotes, "tag": tag})  # "tag": tag


def top_ten_tags():
    tag_list = Tag.objects.values('id').annotate(quotes_count=Count('quotes')).order_by('-num_tags')[:10]
    print(f'{tag_list}')

    return render(request, 'index.html', {'tag_list': tag_list})
