people = {
    '123': {
        'movies' : {'23'},
        'name': 'joselina',
        'birth' : 1923.
    },
      '124': {
        'movies' : {'42','4223', '23'},
        'name': 'andressa',
        'birth' : 200.
    }
}

movies = {
    '42' : {
        'title': 'Carros',
        'year': 2005,
        'stars' :{ 124, 46}
    },
    '23' : {
        'title': 'Shrek',
        'year': 2000,
        'stars' :{ 124, 123}
    }
}
"""
for movie_id in people['123']['movies']:
    for id_person in movies[movie_id]['stars']:
        print(id_person)
"""
"""
for movie_id in people[node.state]['movies']:
            for id_person in movies[movie_id]['stars']:
                if not frontier.contains_state(id_person) and id_person not in explored:
                    print(id_person)
                    child = Node(state=id_person, parent=node.state,action=movie_id)
                    frontier.add(child)
"""

lista = [1,0,3]
