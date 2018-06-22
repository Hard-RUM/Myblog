# 公用分页功能
import math


def custom_paginator(current_page, total_page, max_page):
    # current_page表示当前页
    # total_page:表示总页数
    # max_page:表示最大显示页数

    middle = math.ceil(max_page / 2)
    # 如果总页数小于最大显示页数
    if total_page < max_page:
        start = 1
        end = total_page
    else:
        # 除此之外都是正常的情况
        # 第一种情况，在当前页头部的时候
        if current_page <= middle:
            start = 1
            end = max_page
            # 第二种情况，当前页在中间的位置
        elif (current_page > middle) and (current_page < total_page - middle):
            start = current_page - middle
            end = current_page + middle - 1
        else:
            # 第三种情况，当前页在尾巴
            start = total_page - max_page + 1
            end = total_page

    return start, end
