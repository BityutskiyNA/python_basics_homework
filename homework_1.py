def iterating_routes(points, n, result, post_office):
    if n < 1:
        a = [post_office]
        for point in points:
            a.append(point)
        a.append(post_office)
        result.append(a.copy())
    else:
        j = n - 1
        while j >= 0:
            [points[j], points[n - 1]] = [points[n - 1], points[j]]
            iterating_routes(points, n - 1, result, post_office)
            [points[j], points[n - 1]] = [points[n - 1], points[j]]
            j = j - 1
    return result


def get_minimum_route(result, n):
    min_route_result = 100
    min_route = 0
    final_line = ""
    for route in result:
        if min_route < min_route_result and min_route != 0:
            min_route_result = min_route
            final_line = buffer_line + " = {min_route_result}".format(min_route_result=min_route_result)
        buffer_line = ""
        min_route = 0
        j = 0
        while j <= n:
            point_1 = route[j]
            point_2 = route[j + 1]
            min_route = min_route + ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
            if j == 0:
                buffer_line = buffer_line + "({point_1_0},{point_1_1}) -> ({point_2_0},{point_2_1})[{y}]".format\
                    (point_1_0=point_1[0], point_1_1=point_1[1], point_2_0=point_2[0], point_2_1=point_2[1],
                     y=min_route)
            else:
                buffer_line = buffer_line + " -> ({point_2_0},{point_2_1})[{y}]".format(point_2_0=point_2[0],
                                                                                        point_2_1=point_2[1],
                                                                                        y=min_route)
            j = j + 1

    return final_line


if __name__ == '__main__':
    post_office = [0, 2]
    griboyedov_st = [2, 5]
    baker_st = [5, 2]
    big_sadovaya_st = [6, 6]
    evergreen_terrace = [8, 3]
    points = [griboyedov_st, baker_st, big_sadovaya_st, evergreen_terrace]
    result = []
    sum_points = len(points)
    routes = iterating_routes(points, sum_points, result, post_office)
    minimum_route = get_minimum_route(routes, sum_points)
    print(minimum_route)
