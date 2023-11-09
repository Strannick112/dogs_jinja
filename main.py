from flask import Flask, send_from_directory, render_template, request, redirect

nikita = Flask("my app", static_folder="static")

data_in_the_program = [
    {
        'id': 0,
        'type': 'Хаски',
        'gender': "female",
        'photo': "https://klike.net/uploads/posts/2022-09/1662043782_j-7.jpg",
        'description': "Красивая голубоглазая красавица ищет дом"
    },
    {
        'id': 1,
        'type': 'Немецкая овчарка',
        'gender': "male",
        'photo': "http://faunazoo.ru/wp-content/uploads/2021/02/%D0%9F%D0%BE%D1%80%D0%BE%D0%B4%D0%B0-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA-%D0%9D%D0%B5%D0%BC%D0%B5%D1%86%D0%BA%D0%B0%D1%8F-%D0%9E%D0%B2%D1%87%D0%B0%D1%80%D0%BA%D0%B0.jpg",
        'description': "Ищу очередного хозяина, который сможет меня прокормить"
    },
    {
        'id': 2,
        'type': 'Мопс',
        'gender': "female",
        'photo': "https://porodysobak.ru/wp-content/uploads/2022/07/mops-3.jpg",
        'description': 'а как какать...'
    },
]

@nikita.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')

@nikita.route('/main', methods=['GET'])
def main():
    return render_template('main.html')

@nikita.route('/dogs', methods=['GET'])
def dogs():
    return render_template('dogs.html', data=data_in_the_program)

@nikita.route('/about_us', methods=['GET'])
def about_us():
    return render_template('about_us.html')

@nikita.route('/dog_info', methods=['GET'])
def dog_info():
    if (id := request.values.get('id')) is not None:
        id = int(id)
        if 0 <= id < len(data_in_the_program):
            return render_template('dog_info.html', dog=data_in_the_program[id])
    return redirect('/dogs')

nikita.run()
