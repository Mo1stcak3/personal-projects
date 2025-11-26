def space():
    print("\n")
    return

def books():
    book = int(input(
"1. Atomic Habits by James Clear\n"


"2. The 7 Habits of Highly Effective People by Stephen R. Covey\n"

"Review: Considered a timeless classic, reviewers highlight its focus on character ethics and long-term success.\n"

"Preview: Covey introduces habits like 'Be Proactive' and 'Begin with the End in Mind' to transform personal and professional effectiveness.\n\n"

"3. The Power of Now by Eckhart Tolle\n"

"Review: Widely acclaimed for its spiritual depth, reviewers note how it helps reduce anxiety by focusing on the present moment.\n"

"Preview: Tolle guides readers to detach from past regrets and future worries, emphasizing mindfulness and inner peace.\n\n"

"4. Mindset: The New Psychology of Success by Carol S. Dweck\n"

"Review: Readers appreciate its research-based insights into growth vs. fixed mindsets, especially in education and leadership.\n"

"Preview: Dweck shows how adopting a growth mindset can unlock learning, resilience, and achievement in any area of life.\n\n"

"5. The Subtle Art of Not Giving a F*ck by Mark Manson\n"

"Review: Reviews highlight its blunt, humorous style that challenges traditional positivity-focused self-help.\n"

"Preview: Manson argues that embracing limitations and choosing what truly matters leads to a more meaningful life."
))
    
    if book == 1:
        print("1. Atomic Habits by James Clear\n\n\n"

"Review: Readers praise its practical strategies for building good habits and breaking bad ones.\n\n"

"Preview: Clear explains how tiny changes compound into remarkable results, using real-life examples and science-backed methods.\n\n\n")
        return f"" 

print("Welcome To The Library\n")

#Creation of Account
def coa():
    print("  CREATE YOUR ACCOUNT TO CONTIUE!  ")
    clog = input("Username: ")
    cpw = input("Password: ")
    space()
    return clog, cpw

#Account Library
def login_process(clog, pw):
    a = 0
    while a < 3:
        print("  LOGIN YOUR ACCOUNT  ")
        log = input("USERNAME: ")
        pw = input("PASSWORD: ")
        space()

        if log.lower() == clog.lower() and pw.lower() == cpw.lower():
            print("Success Log in")
            books()
            return True
        else:
            print("bulbul kaba?! hackerist yern?")
            a += 1

    print("HECKER KABA???")
    return False

clog, cpw = coa()
login_process(clog, cpw)
