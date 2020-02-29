import numpy as np


def find_target(a:list, b:list, target:int):

    # numpy 并不是必要的
    # 对数组 去重 排序
    np_a = np.array(sorted(set(a)))
    np_b = np.array(sorted(set(b)))

    # 排序以后左上角坐标为0，0 的元素为加和最小的元素, 作为最开始的参照
    smallest_diff = abs(np_a[0] + np_b[0] - target)

    # 返回查询结果，元祖列表
    result = [(np_a[0], np_b[0])]

    # 元素索引
    i = 0
    j = len(np_b) -1

    while i < len(np_a) and j > 0:
        # 从右上角开始遍历 np_a 为行 np_b 为列
        tmp_diff = np_a[i] + np_b[j] - target

        if abs(tmp_diff) < smallest_diff:
            # 新的差值较小, 重置查询结果
            result = []
            smallest_diff = tmp_diff
            result.append((np_a[i], np_b[j]))
        elif tmp_diff == smallest_diff:
            result.append((np_a[i], np_b[j]))

        # tmp_diff 较大时继续查找是否有新的差值
        if tmp_diff > 0:
            # 当前元素较大 向左上角查找
            j -= 1
        elif tmp_diff < 0:
            # 当前元素较小 向右下角查找
            i += 1
        elif tmp_diff == 0:
            # 差值为0时为当前目标 查找其左下角的元素是否相同, 小于目标值返回结果，相同继续向左下对角遍历
            if np_a[i+1] + np_b[j-1] == target:
                j -= 1
                i += 1
            elif np_a[i+1] + np_b[j-1] != target:
                return result
    return result

