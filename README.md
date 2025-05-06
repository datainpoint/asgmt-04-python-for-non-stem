# asgmt-04-python-for-non-stem
Assignment 04: Python for Non-STEM.

## 練習題指引

- 將練習題的 GitHub Repository 下載到自己的電腦，解壓縮後以 VS Code 開啟專案資料夾。
- 先閱讀 `README.md`，再將答案寫在 `answers.py`
- 練習題共分為三種：
  - 是非題：預設答案 `answer_01 = None`，請以布林型別宣告答案，若覺得是非題的敘述**不正確**，就宣告 `answer_01 = False`，若覺得是非題的敘述**正確**則宣告 `answer_01 = True`
  - 單選題：預設答案 `answer_02 = None`，請以整數型別宣告答案，若覺得單選題的第一個選項**正確**宣告為 `answer_02 = 1`，若覺得單選題的第二個選項**正確**則宣告 `answer_02 = 2`，若覺得單選題的第三個選項**正確**則宣告 `answer_02 = 3`，若覺得單選題的第四個選項**正確**則宣告 `answer_02 = 4`
  - 程式題：以函數/類別宣告答案，函數/類別名稱下的長字串（docstring）會描述測試資料與預期輸出，能夠讓我們充分暸解預期輸入以及預期輸出之間的對應關係，寫作完畢後要記得輸出答案的變數 `return your_answer_variable`
- 如果練習題需要載入檔案，檔案會與練習題存放在同個資料夾中，這時可以運用工作目錄的相對路徑直接指定檔案名稱載入。
- 寫作完成後將 `answers.py` 存檔，再執行專案資料夾中的 `test_runner.py` 進行測試，再依照測試結果修正答案或截圖測試結果繳交作業。

## 01.（是非題）Python 資料結構中的 `list` 與 `tuple` 在應用情境上完全相同、沒有差異。

```python
answer_01 = None
```

## 02.（單選題）下列何者不是 Python 的內建資料結構？

1. `list`
2. `tuple`
3. `dict`
4. `DataFrame`

```python
answer_02 = None
```

## 03.（程式題）定義函數 `answer_03()` 能夠將輸入 `list` 的第一個資料與最後一個資料取出。

```python
def answer_03(x: list) -> tuple:
    """
    >>> answer_03([2, 3, 5, 7, 11])
    (2, 11)
    >>> answer_03(["Python", "Reticulate", "Anaconda"])
    ("Python", "Anaconda")
    """
```

## 04.（程式題）定義函數 `answer_04()` 能夠將輸入 `list` 的第一個資料與最後一個資料移除後再回傳。

```python
def answer_04(x: list) -> list:
    """
    >>> answer_04([2, 3, 5, 7, 11])
    [3, 5, 7]
    >>> answer_04(["Python", "Reticulate", "Anaconda"])
    ["Reticulate"]
    """
```

## 05.（程式題）定義函數 `answer_05()` 能夠將輸入 `str` 的前三個字元取出。

```python
def answer_05(x: str) -> str:
    """
    >>> answer_05("Python")
    "Pyt"
    >>> answer_05("Reticulate")
    "Ret"
    >>> answer_05("Anaconda")
    "Ana"
    """
```

## 06.（程式題）定義函數 `answer_06()` 能夠將長度為奇數 `list` 的「中位」整數取出。

```python
def answer_06(x: list) -> int:
    """
    >>> answer_06([2, 3, 5])
    3
    >>> answer_06([2, 3, 5, 7, 11])
    5
    >>> answer_06([2, 3, 5, 7, 11, 13, 17])
    7
    """
```

## 07.（程式題）定義函數 `answer_07()` 能夠將字元個數為奇數 `str` 的中間三個字元取出。

```python
def answer_07(x: str) -> str:
    """
    >>> answer_07("Steve")
    "tev"
    >>> answer_07("Stark")
    "tar"
    >>> answer_07("Natasha")
    "tas"
    """
```

## 08.（程式題）定義函數 `answer_08()` 能夠輸入國家名稱，回傳 ISO 國家二位字母代碼、三位字母代碼。本題不需要完成所有國家的名稱與 ISO 國家字母代碼之對應關係，只需要能完成測試範例即可。

```python
def answer_08(country_name: str) -> dict:
    """
    >>> answer_08("Taiwan")
    {'alpha2': 'TW', 'alpha3': 'TWN'}
    >>> answer_08("Japan")
    {'alpha2': 'JP', 'alpha3': 'JPN'}
    >>> answer_08("United States")
    {'alpha2': 'US', 'alpha3': 'USA'}
    >>> answer_08("Czech Republic")
    {'alpha2': 'CZ', 'alpha3': 'CZE'}
    >>> answer_08("Lithuania")
    {'alpha2': 'LT', 'alpha3': 'LTU'}
    >>> answer_08("Slovakia")
    {'alpha2': 'SK', 'alpha3': 'SVK'}
    >>> answer_08("Poland")
    {'alpha2': 'PL', 'alpha3': 'POL'}
    """
```

## 09.（程式題）定義函數 `answer_09()` 能夠將輸入 `list` 中重複的元素剔除後遞增排序回傳。

```python
def answer_09(x: list) -> list:
    """
    >>> answer_09([5, 5, 6, 6])
    [5, 6]
    >>> answer_09([2, 2, 6, 6])
    [2, 6]
    >>> answer_09([9, 9, 8, 1])
    [1, 8, 9]
    """
```

## 10.（程式題）定義函數 `answer_10()` 能夠回傳兩份資料之間的相同元素個數。

```python
def answer_10(x: set, y: set) -> int:
    """
    >>> answer_10({5, 5, 6, 6}, {5, 6, 7, 8})
    2
    >>> answer_10({1, 3, 5, 7, 9}, {2, 3, 5, 7})
    3
    >>> answer_10({1, 3, 5, 7, 9}, {1, 3, 5, 7, 9})
    5
    >>> answer_10({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10})
    0
    """
```