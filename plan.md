# uzmovie-clone-django

uzmovie-clone-django

Modellar:

[] - Film
    -- name
    -- slug
    -- image
    -- description
    -- treyler
    -- video (kino videosi)
    -- bot code
    -- category
    -- country
    -- year
    -- language
    -- duration
    -- age_limit
    -- views_count
    -- release_date (created_at orniga, updated_at kerak emas)

    Qo'shimcha kerakli narsalar
    -- reviews_count
    -- likes_count
    -- dislikes_count
    -- rating

    def get_absolute_url(self, *args, **kwargs):
        pass

[] - WishList
    -- user (onetoone)

    @property
    def items_count(self):
        pass

[] - WishListItem
    -- wishlist # foreign key
    -- film # foreign key

    unique together (wishlist, film)

[] - Review
    -- user # foreign
    -- film # foreign
    -- review richtextfield

[] - Like/Dislike
    -- https://chatgpt.com/c/68a3123b-1c48-8324-8906-c1bcf917fd81
