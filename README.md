
# Assignment1

**Goal**: Implement Insertion Sort that sorts an array in **monotonically decreasing** order and practice Git/GitHub workflows.

## Requirements
- Python 3.8+ (tested with Python 3.13)
- (Optional) VS Code with Python extension

## Run
```bash
python3 insertion_sort.py
# or provide numbers via argv or stdin
python3 insertion_sort.py "10 3 7 1 2"
echo "10 3 7 1 2" | python3 insertion_sort.py
```

**Expected:**
```text
Original: [10, 3, 7, 1, 2]
Sorted (decreasing): [10, 7, 3, 2, 1]
```

## Tests (basic)
```bash
python3 -m unittest -v tests/test_insertion_sort.py
```

## Suggested Commit Plan
1. `feat: add insertion sort (decreasing)`  
2. `test: add basic unit tests & README`  
3. `chore: polish CLI parsing and docs`

## How to Push to GitHub
```bash
# inside the project folder
git init
git add .
git commit -m "feat: initial insertion sort (decreasing)"

# create remote repo named MSCS532_Assignment1 on GitHub (public), then:
git branch -M main
git remote add origin https://github.com/<your-username>/MSCS532_Assignment1.git
git push -u origin main
```

# Author
```
Vanitha Togata Lingam
University of the Cumberlands
MSCS532 – Assignment 1
```