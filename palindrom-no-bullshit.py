def is_palindrome(palindrome):
    str_pal = str(palindrome)
    reversed_palindrome = str_pal[::-1]
    return str_pal == reversed_palindrome

def main():
    if is_palindrome(101) == True:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()