тесты запускались на локальной машине 

win10 home командой 

behave - i testaddnewtask.feature

behave - i newcategory.feature

behave -i oldtask.feature

behave -i testbutton.feature


Для запуска тестов на докере выполнялись следующие команды:

docker run -p 80:80 --name test -t pythonimage

winpty docker exec -i -t test bash

cd features/steps/

behave - i testaddnewtask.feature

behave - i newcategory.feature

behave -i oldtask.feature

behave -i testbutton.feature
