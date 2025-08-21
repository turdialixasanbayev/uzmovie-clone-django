# 📽️ uzmovie-clone-django

A Django-based movie streaming platform clone, designed to manage movies, categories, user reviews, likes/dislikes, and personal wishlists.  

---

## 🚀 Features
- 🎬 Manage movies with detailed metadata (name, slug, description, video, etc.)  
- 📂 Categorize films by category, country, language, year, and age limit  
- ❤️ Like/Dislike reactions for each film  
- 📝 Rich-text reviews  
- ⭐ Rating system with likes/dislikes/reviews count  
- 🎯 User-specific **Wishlist** functionality  

---

## 🗂️ Models Overview

### 🎬 Film
Represents a movie with all essential details.

| Field          | Type         | Notes |
|----------------|-------------|-------|
| name           | CharField   | Movie title |
| slug           | SlugField   | Auto-generated from name |
| image          | ImageField  | Poster/thumbnail |
| description    | RichText    | Full description |
| trailer        | URL/Video   | Movie trailer |
| video          | File/Video  | Main movie file |
| bot_code       | CharField   | Custom integration code |
| category       | FK          | Film category |
| country        | CharField   | Origin country |
| year           | Integer     | Release year |
| language       | CharField   | Language |
| duration       | Duration    | Movie duration |
| age_limit      | Integer     | Age restriction |
| views_count    | Integer     | Default = 0 |
| release_date   | Date        | Instead of created/updated_at |

**Extra fields for analytics:**  
- `reviews_count`  
- `likes_count`  
- `dislikes_count`  
- `rating`  

```python
def get_absolute_url(self, *args, **kwargs):
    pass
```

---

### 📌 WishList
A user’s personal wishlist.

| Field | Type | Notes |
|-------|------|-------|
| user  | OneToOneField | Each user has only one wishlist |

```python
@property
def items_count(self):
    pass
```

---

### 🎞️ WishListItem
Items inside the wishlist (films).

| Field    | Type       | Notes |
|----------|------------|-------|
| wishlist | FK (WishList) | Belongs to a user’s wishlist |
| film     | FK (Film)     | The movie added to wishlist |

⚖️ **Constraint:** `(wishlist, film)` must be unique.

---

### 📝 Review
User-written reviews on movies.

| Field  | Type     | Notes |
|--------|----------|-------|
| user   | FK (User) | Reviewer |
| film   | FK (Film) | Related movie |
| review | RichText | Review content |

---

### 👍👎 Reaction (Like/Dislike)
Stores reactions for films.  
Each user can leave **only one reaction per film**.

| Field    | Type     | Notes |
|----------|----------|-------|
| film     | FK (Film) | Related movie |
| user     | FK (User) | Who reacted |
| reaction | Integer   | `1 = Like`, `-1 = Dislike` |
| created_at | DateTime | Auto timestamp |

⚖️ **Constraint:** `(film, user)` must be unique.  

---

## 📊 Relationships
- `Film` ↔ `Review` → **One-to-Many**  
- `Film` ↔ `Reaction` → **One-to-Many**  
- `WishList` ↔ `WishListItem` ↔ `Film` → **Many-to-Many via intermediate**  

---

## 🛠️ Planned Features
- 🔍 Search and filter by category, year, language  
- 📈 Film analytics (most liked, most viewed, top-rated)  
- 👤 User profile with wishlist & review history  
- 🎨 Rich admin interface with custom filters and inlines  

---

⚡ This project is under development. Stay tuned for updates!

https://chatgpt.com/c/68a3123b-1c48-8324-8906-c1bcf917fd81
