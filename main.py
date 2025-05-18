from yelp import YelpSystem

if __name__ == "__main__":
    yelp = YelpSystem()

    yelp.add_user("alice")
    yelp.add_user("bob")

    yelp.add_business("Pizza Palace", "Italian")
    yelp.add_business("Taco Town", "Mexican")

    yelp.add_review("alice", "Pizza Palace", 5, "Amazing pizza!")
    yelp.add_review("bob", "Pizza Palace", 4, "Good but a bit oily.")
    yelp.add_review("alice", "Taco Town", 3, "Not bad, but not authentic.")

    yelp.show_business("Pizza Palace")

    print("\nSearch Results for 'Mexican':")
    for b in yelp.search_business("Mexican"):
        print(b)
