## Описание работы программы

- Программа предлагает пользователю нелинейный способ по созданию, демонстрации, выгрузке, поиску, удалению и редактированию записей телефонного справочника.
- Все действия и переходы осуществляются из главной функции main. По окончанию выполнения вспомогательные функции, возвращают пользователя в главную функцию для повторного выполнения доступных операций, либо для выхода из программы с помощью пункта меню - "Завершить работу".
- В программе реализованы проверки на ошибки в работе, такие как: наличие файла справочника, пустой справочник, корректный ввод вариантов выбора пользователя, корректные переходы внутри меню справочника, проверка безрезультатного поиска, подтверждение удаления и изменения записей справочника, корректное отображение различных подменю внутри программы, игнорирование регистра вводимых знаков при поиске. Также реализованы прерывания вывода информации для демонстрации результатов работы (требуется ввод Enter со стороны пользователя для продолжения). 

## Описание решения

Для работы данной программы был создан ряд функций:

1. Вспомогательная функция "**list_input**" требуется для заполнения вручную записи пользователя, возвращая в сгенерированный список поля заполняемой записи и выводя на экран информацию о текущем заполняемом поле в качестве подсказки.

2. Функция "**phonebook_import**" генерирует единичную запись для справочника, которую вводит пользователь, вызывая внутри функцию "**list_input**". После открывается файл справочника "**phonebook.txt**" (либо создается новый файл под тем же именем), и к текущим записям (если они есть), добавляется созданная пользователем. В качестве разделителя между полями внутри файла добавляется символ **"~"** для дальнейшего использования его в качестве разделителя для реализации функции поиска и по полям справочника и их редактирование.

3. Вспомогательная функция "**check_file**" выполяет проверку на пустой список и на наличие файла справочника - в обоих случаях возвращается пустой список. В случае наличие записей возвращается содержимое справочника в виде списка.

4. Вспомогательная функция "**check_input**" выполяет проверку вводимых пользователем данных. Функция принимает список из строчных символов, и возвращает символ введенный пользователем, (в случае если он принадлежит списку). Если введен неверный символ, будет показано сообщение об ошибке, с предложением повторного ввода данных.

5. Вспомогательная функция "**show_inf**" служит для прерывания выводимой инфорации в различных блоках программы, и для информирования пользователя о возвращении в главное меню.

6. Функция "**download_phonebook**" загружает вспомагательный готовый справочник из 10 записей "**sample.txt**" и заменяет им текущий справочник под именем: "**phonebook.txt**". Если справочника нет, то создается новый под этим именем. Данная функция переписывает собой все ранее добавленные записи в случае вызова.

7. Функця "**display_phonebook**" выводит на экран текущее состояние файла "**phonebook.txt**", также проверяется наличие файла и пустых строк, путём вызова функции "**check_file**".

8. Вспомогательная функция "**show_search()**" выполняет поиск по заданному пользователем полю и возвращает списком все записи с любым совпадением с клавиатурным вводом. Если поиск ничего не дал, то возращается список с единственным значением [1], если пользователь отменил поиск, либо в справочнике нет записей, то возвращается значение [0]. В любом другом случае выводится на экран список из найденных значений и возвращается из функции в виде списка. Функция вызывает внутри себя "**check_file**", "**check_input**".

9. Вспомогательная функция "**repeat_empty_search**" служит для обработки результатов работы "**show_search()**", внутри основных функций "**search_phonebook**" (поиск элементов), "**delete_record**" (удаление элементов) и "**change_record()**" (редактирование элементов). В случае если поиск оказался пустым, либо отсутствовали записи в файле (либо пользователь выбрал отмену операции), возвращаются значение 1 - для нового вызова основных функций, 0 - для возвращения в главное меню, либо 2 - признак того что поиск оказался результативным.

10. Функция **search_phonebook** производит поиск по указанному пользователем полю, выводит на экран результат и даёт возможность проивести новый поисковой запрос, либо вернуться в главное меню.

11. Функция "**delete_record**" удаляет выбранную пользователем запись по результату поискового запроса в заданном поле справочника. После поиска пользователю выводится на экран список найденных для удаления записей, он выбирает одну для удаления и после сможет удалить и другие записи по результату этого поиска, либо выполнить новый поиск с новыми параметрами. В любой момент возможна отмена операции.

12. Функция "**delete_record**" изменяет выбранную пользователем запись по результату поискового запроса в заданном поле справочника. После поиска пользователю выводится на экран список найденных для изменения записей, он выбирает одну для изменения. Изменить предлагается как поле целиком, так и любое выбранное поле. После изменения записи пользователь может выбрать изменить ли ему другую запись по текущему поисковому запросу, выполнить поиск с новыми параметрами, либо вернуться в главное меню. Также в любой момент для пользователя возможен выбор отменить операцию изменения и вернуться в главное меню.

13. Главная функция "**main**". Из неё происходит вызов основных функций для работы со справочником, а также в неё возвращаются все другие вызываемые из неё функции. Она представляет из себя меню с выбором из 7 пунктов: 1 - Занести данные в справочник; 2 - Загрузить готовый справочник; 3 - Просмотреть данные из справочника; 4 - Выполнить поиск по полю справочника; 5 - Удалить запись из справочника; 6 - Изменить данные в справочнике; 7 - Завершить работу. Программа будет выполняться пока пользователь не выберит 7-ой пункт.
