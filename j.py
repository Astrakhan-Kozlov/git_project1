from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя">
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты">
                                    <div class="form-group">
                                        <label for="about">Образование</label>
                                        <textarea class="form-control" rows="3" name="education"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Профессии</label>
                                        <select class="form-control" id="classSelect" name="professions">
                                          <option>инженер-исследователь</option>
                                          <option>пилот</option>
                                          <option>строитель</option>
                                          <option>экзобиолог</option>
                                          <option>врач</option>
                                          <option>инженер по терраформированию</option>
                                          <option>климатолог</option>
                                          <option>специалист по радиационной защите</option>
                                          <option>астрогеолог</option>
                                          <option>гляциолог</option>
                                          <option>метеоролог</option>
                                          <option>оператор марсохода</option>
                                          <option>киберинженер</option>
                                          <option>штурман</option>
                                          <option>пилот дронов</option>
                                        </select>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почемы вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" rows="3" name="motivation"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h3>Заявка принята</h3>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
