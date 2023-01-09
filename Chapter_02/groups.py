#!/usr/bin/env python3

# names = ['ラリー', 'カーリー', 'モー']
# message = 'サンバか対象: '

# for index, name in enumerate(names):
#     if index > 0:
#         message += 'に'
#     if index == len(names) - 1:
#         message += '、それから'
#     message += name

# print(message)

def introduce_stooges(names: list[str]) -> None:
    message = '三ばか大将: '

    for index, name in enumerate(names):
        if index > 0:
            message += 'に'
        if index == len(names) - 1:
            message += '、それから'
        message += name
    print(message)

introduce_stooges(['モー', 'ライリー', 'シェンプ'])
introduce_stooges(['カーリー', 'ライリー', 'モー'])

def introduce(title: str, names: list[str]) -> None:
    message = f'{title}: '

    for index, name in enumerate(names):
        if index > 0:
            message += 'に'
        if index == len(names) - 1:
            message += '、それから'
        message += name
    print(message)

introduce('忍者タートルズ', ['ドナテロ', 'ファエロ', '、ミケランジェロ', 'レオナルド'])
introduce('アルビンとチョップマンクス', ['アルビン', 'サイモン', '、セオドア'])

def join_names(names: list[str]) -> str:
    name_string = ''
    for index, name in enumerate(names):
        if index > 0:
            name_string += 'に'
        if index == len(names) - 1:
            name_string += '、それから'
        name_string += name
    return name_string

def introduce_groups(title: str, names: list[str]) -> None:
    print(f'{title}: {join_names(names)}')

introduce_groups('桃太郎', ['Dog', 'Monkey', 'Pheasant'])
