from newspaper.models import Category,Post,Tag



def navigation(request):
    categories = Category.objects.all()[:4]
    tags = Tag.objects.all()[:10]
    trending_posts= Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-views_count")[:5]

    return{
        "categories": categories,
        "tags": tags,
        "trending_posts": trending_posts,
    }