# set_basic.py


# order matter করে না ❌

# duplicate থাকলে remove হয়ে যায় ✔️

# 👉 internally Python এটাকে hash table দিয়ে store করে
# 👉 তাই search খুব fast (O(1))

num1 = {1, 2, 3, 0, 5, 6}
num2 = set([4, 5, 6])

print(4 not in num1)

