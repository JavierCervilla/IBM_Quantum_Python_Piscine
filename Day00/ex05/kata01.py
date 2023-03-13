#!/usr/bin/env python3

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def main():
    print("Python was created by {python}\nRuby was created by {ruby}\nPHP was created by {php}".format(python = kata['Python'], ruby = kata['Ruby'], php = kata['PHP']))
    return
    
if(__name__ == '__main__'):
    main()