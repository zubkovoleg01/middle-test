Requirements specification:
===============================
_______________________________________________________________________

Определение оператора и региона по номеру телефона
===============================

Необходимо создать сервис, который позволит определять по номеру
телефона - оператора связи и регион.

Веб-интерфейс
===============================
Должна быть web-форма, которая принимает номер телефона, а в ответ
показывает что-то типа

• сам номер
• ПАО "Мобильные ТелеСистемы"
• Республика Дагестан

API-интерфейс
===============================
Нужен один эндпойнт API, который принимает номер абонента в формате
MSISDN (например, 79173453223).

В случае успешного завершения код должен возвращать информацию о
номере (операторе мобильной связи и регионе), в случае ошибки —
сигнализировать об этой ошибке. Формат JSON.

Определение принадлежности номера
===============================
Нужно проверить наличие номера в реестре российской системы и плана
нумерации:

https://opendata.digital.gov.ru/registry/numeric/downloads

Проверка, не было ли по этому номеру перехода от одного оператора к
другому без смены номера, выходит за рамки этой задачи. Для этого
есть таблица маршрутных номеров от НИИР, это другая история.

Условия:

• Python 3;

• PostgreSQL;

• Django

* можно использовать любые общедоступные библиотеки

_______________________________________________________________________

