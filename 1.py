from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def a():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def b():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>И на Марсе будут яблони цвести!</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def c():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Миссия Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.<br>
                    Человечеству мала одна планета.<br>
                    Мы сделаем обитаемыми безжизненные пока планеты.<br>
                    И начнем с Марса!<br>
                    Присоединяйся!</h1><br>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                     alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


@app.route('/promotion_image')
def pr_im():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                     alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/choice')
def choice():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Выбор планеты</title>
                  </head>
                  <body>
                    <h1>Введите в адестной строке название планеты Солнечной системы для получения её описания</h1>
                  </body>
                </html>"""


@app.route('/choice/Mercury')
def mer():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Меркурий</h1>
                        <img src="{url_for('static', filename='img/1.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                          Ближайшая к Солнцу планета Солнечной системы
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Наименьшая из планет земной группы
                        </div>
                        <div class="alert alert-success" role="alert">
                          По своим физическим характеристикам Меркурий напоминает Луну
                        </div>
                        <div class="alert alert-danger" role="alert">
                          После лишения Плутона в 2006 году статуса планеты к Меркурию перешло звание самой маленькой планеты Солнечной системы.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Меркурианские звёздные сутки равны 58,65 земных суток, то есть 2/3 меркурианского года
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Venus')
def ven():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Венера</h1>
                        <img src="{url_for('static', filename='img/2.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Вторая по удалённости от Солнца и шестая по размеру планета Солнечной системы
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Венера считается «сестрой» Земли, потому что обе планеты похожи размерами и составом.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Венера имеет плотную атмосферу, состоящую более чем на 96 % из углекислого газа
                        </div>
                        <div class="alert alert-danger" role="alert">
                           Из-за высокого давления, CO2 в приповерхностной части атмосферы по агрегатному состоянию является уже не газом,
                            а сверхкритической жидкостью, поэтому эта часть атмосферы представляет собой «полужидкий-полугазообразный»
                             океан из сверхкритического углекислого газа.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Были предложены планы по использованию вездеходов, а также реализации более сложных задач, но им мешают
                           тяжёлые условия на поверхности Венеры
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Earth')
def ear():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Земля</h1>
                        <img src="{url_for('static', filename='img/3.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Третья по удалённости от Солнца планета Солнечной системы
                        </div>
                        <div class="alert alert-warning" role="alert">
                           Самая плотная, пятая по диаметру и массе среди всех планет и крупнейшая среди планет земной группы
                        </div>
                        <div class="alert alert-success" role="alert">
                          Научные данные указывают на то, что Земля образовалась из
                           солнечной туманности около 4,54 миллиарда лет назад и вскоре после этого обрела свой
                            единственный естественный спутник — Луну
                        </div>
                        <div class="alert alert-danger" role="alert">
                           Приблизительно 70,8 % поверхности планеты занимает Мировой океан, остальную
                            часть поверхности занимают континенты и острова
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          По различным оценкам, Земля будет сохранять условия для существования
                           живых организмов ещё в течение 0,5—2,3 млрд лет
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Mars')
def mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Марс</h1>
                        <img src="{url_for('static', filename='img/4.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Четвёртая по удалённости от Солнца и седьмая по размеру планета Солнечной системы
                        </div>
                        <div class="alert alert-warning" role="alert">
                           Иногда Марс называют «красной планетой» из-за красноватого оттенка поверхности,
                            придаваемого ей минералом маггемитом — γ-оксидом железа(III)
                        </div>
                        <div class="alert alert-success" role="alert">
                          Марс — планета земной группы с разреженной атмосферой (давление на поверхности в 160 раз меньше земного)
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Особенностями поверхностного рельефа Марса можно считать ударные кратеры наподобие
                             лунных, а также вулканы, долины, пустыни и полярные ледниковые шапки наподобие
                              земных
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          У Марса есть два естественных спутника — Фобос и Деймос (в переводе с древнегреческого — «страх» и «ужас»
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Jupiter')
def jup():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Юпитер</h1>
                        <img src="{url_for('static', filename='img/5.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Юпи́тер — крупнейшая планета Солнечной системы, пятая по удалённости от Солнца
                        </div>
                        <div class="alert alert-warning" role="alert">
                           Наряду с Сатурном, Ураном и Нептуном, Юпитер классифицируется как газовый гигант
                        </div>
                        <div class="alert alert-success" role="alert">
                          Ряд атмосферных явлений на Юпитере: штормы, полярные сияния — имеет масштабы,
                           на порядки превосходящие земные. Примечательным образованием в атмосфере является
                            Большое красное пятно — гигантский шторм, известный с XVII века
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Юпитер имеет, по крайней мере, 79 спутников, самые крупные из которых — Ио, Европа, Ганимед и Каллисто
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Во время великих противостояний (одно из которых происходило в сентябре 2010 года)
                           Юпитер виден невооружённым глазом как один из самых ярких объектов на ночном небосклоне после Луны и Венеры
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Saturn')
def sat():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Сатурн</h1>
                        <img src="{url_for('static', filename='img/6.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Сатурн — шестая планета от Солнца и вторая по размерам планета в Солнечной системе после Юпитера
                        </div>
                        <div class="alert alert-warning" role="alert">
                           В основном Сатурн состоит из водорода, с примесями гелия и следами воды, метана, аммиака и тяжёлых элементов
                        </div>
                        <div class="alert alert-success" role="alert">
                          Сатурн обладает заметной системой колец, состоящей главным образом из частичек льда,
                           меньшего количества тяжёлых элементов и пыли
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Вокруг планеты обращается 82 известных на данный момент спутника. Титан — самый крупный
                             из них, а также второй по размерам спутник в Солнечной системе
                              (после спутника Юпитера, Ганимеда), который превосходит по своим размерам 
                              Меркурий и обладает единственной среди спутников планет Солнечной системы плотной атмосферой
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          На орбите Сатурна находилась автоматическая межпланетная станция
                           (АМС) «Кассини», запущенная в 1997 году и достигшая системы Сатурна
                            в 2004 году. В задачи АМС входило изучение структуры колец, а также динамики
                             атмосферы и магнитосферы планеты. 15 сентября 2017 года станция 
                             завершила свою миссию, сгорев в атмосфере планеты
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Uranus')
def urs():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Уран</h1>
                        <img src="{url_for('static', filename='img/7.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Уран — планета Солнечной системы, седьмая по удалённости от Солнца, третья по диаметру и четвёртая по массе
                        </div>
                        <div class="alert alert-warning" role="alert">
                           В отличие от газовых гигантов — Сатурна и Юпитера, состоящих в основном из водорода
                            и гелия, в недрах Урана и схожего с ним Нептуна отсутствует металлический водород,
                             но зато много льда в его высокотемпературных модификациях. По этой причине специалисты
                              выделили эти две планеты в отдельную категорию «ледяных гигантов»
                        </div>
                        <div class="alert alert-success" role="alert">
                          Так же как у газовых гигантов Солнечной системы, у Урана имеется система колец и магнитосфера, а кроме того, 27 спутников
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Ориентация Урана в пространстве отличается от остальных планет Солнечной системы
                             — его ось вращения лежит как бы «на боку» относительно плоскости обращения этой
                              планеты вокруг Солнца. Вследствие этого планета бывает обращена к Солнцу попеременно
                               то северным полюсом, то южным, то экватором, то средними широтами.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Скорость ветров на Уране может достигать 250 м/с (900 км/ч)
                        </div>
                      </body>
                    </html>"""


@app.route('/choice/Neptune')
def nep():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Выбор планеты</title>
                      </head>
                      <body>
                        <h1>Моё предложение: Нептун</h1>
                        <img src="{url_for('static', filename='img/8.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                           Нептун — восьмая и самая дальняя от Солнца и Земли планета Солнечной системы
                        </div>
                        <div class="alert alert-warning" role="alert">
                           Обнаруженный 23 сентября 1846 года, Нептун стал первой планетой,
                            открытой благодаря математическим расчётам. Обнаружение непредвиденных
                             изменений в орбите Урана породило гипотезу о неизвестной планете,
                              гравитационным возмущающим влиянием которой они и обусловлены.
                               Нептун был найден в пределах предсказанного положения
                        </div>
                        <div class="alert alert-success" role="alert">
                          Вскоре был открыт его спутник Тритон, однако остальные 13 спутников, известные ныне, были неизвестны до XX века
                        </div>
                        <div class="alert alert-danger" role="alert">
                            В атмосфере Нептуна бушуют самые сильные ветры среди планет
                             Солнечной системы; по некоторым оценкам, их скорости могут достигать 600 м/с[
                        </div>
                        <div class="alert alert-secondary" role="alert">
                           У Нептуна есть слабая и фрагментированная система колец, возможно,
                            обнаруженная ещё в 1960-е годы, но достоверно подтверждённая «Вояджером-2» лишь в 1989 году
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')