from product import (
    NameError,
    NegativeNumberError,
    Product,
    StatusError,
)


def main() -> None:
    """Функция для запуска программы."""

    products = [Product()]
    is_run = True

    while is_run:
        print('1) Выбрать товар из списка.\n'
              '2) Создать новый товар.\n'
              '0) Выйти из программы.\n'
              '\nВыберите действие: ', end=''
              )

        try:
            first_choise = int(input())
        except ValueError:
            print('Ошибка: Введите число.')
            continue

        match first_choise:
            case 0:
                is_run = False

            case 1:
                print(tuple((i+1, prod.get_name()) for i, prod in enumerate(products)))
                print('\nВведите индекс товара: ', end='')

                try:
                    product_choice = int(input()) - 1

                    if not (0 <= product_choice < len(products)):
                        raise ValueError('Товара с таким номером нет')

                except ValueError as e:
                    print(f'Ошибка: {e}')
                    continue

                print(
                    '\nМеню действий:\n'
                    '1) Получить информацию о товаре.\n'
                    '2) Изменить название товара.\n'
                    '3) Изменить количество товара.\n'
                    '4) Изменить статус товара.\n'
                    '5) Изменить данные о поставщике товара.\n'
                    '6) Изменить данные о производителе товара.\n'
                    '7) Изменить цену товара.\n'
                    '8) Изменить данные о местоположении товара.\n'
                    '9) Изменить данные о цвете товара.\n'
                    '10) Изменить характеристики товара.\n'
                    '11) Изменить описание товара.\n'
                    '12) Изменить массу товара.\n'
                    '\nВыберите действие: ', end=''
                )

                try:
                    second_choice = int(input())
                except ValueError:
                    print('Ошибка: Введите число.')
                    continue

                match second_choice:
                    case 1:
                        products[product_choice].get_info()

                    case 2:
                        print('Введите новое название товара: ', end='')
                        try:
                            new_name = input()
                            products[product_choice].set_name(new_name)
                        except NameError as e:
                            print(f'Ошибка {e}')

                    case 3:
                        print('Введите новое количество товара: ', end='')
                        try:
                            new_quantity = int(input())
                            products[product_choice].set_quantity(new_quantity)
                        except ValueError:
                            print('Ошибка: Введите корректное число.')
                        except NegativeNumberError as e:
                            print(f'Ошибка: {e}')

                    case 4:
                        print(
                            '1) В пути.\n'
                            '2) В наличии.\n'
                            '3) Списан.\n'
                            '\nВыберите новый статус товара: ', end=''
                        )

                        try:
                            status_choice = int(input())

                            if status_choice == 1:
                                products[product_choice].set_status('В пути')
                            elif status_choice == 2:
                                products[product_choice].set_status('В наличии')
                            elif status_choice == 3:
                                products[product_choice].set_status('Списан')
                            else:
                                raise ValueError('Выберите корректное действие.')

                        except ValueError as e:
                            print(f'Ошибка: {e}')
                        except StatusError as e:
                            print(f'Ошибка: {e}')

                    case 5:
                        print('Введите нового поставщика товара: ', end='')
                        new_supplier = input()
                        products[product_choice].set_supplier(new_supplier)

                    case 6:
                        print('Введите нового производителя товара: ', end='')
                        new_developer = input()
                        products[product_choice].set_developer(new_developer)

                    case 7:
                        print('Введите новую цену товара: ', end='')
                        try:
                            new_price = float(input())
                            products[product_choice].set_price(new_price)
                        except ValueError:
                            print('Ошибка: Введите корректное число.')
                        except NegativeNumberError as e:
                            print(f'Ошибка: {e}')

                    case 8:
                        print('Введите новое местоположение товара: ', end='')
                        new_location = input()
                        products[product_choice].set_location(new_location)

                    case 9:
                        print('Введите новый цвет товара: ', end='')
                        new_color = input()
                        products[product_choice].set_color(new_color)

                    case 10:
                        print('Введите новые характеристики товара: ', end='')
                        new_characteristics = input()
                        products[product_choice].set_characteristics(new_characteristics)

                    case 11:
                        print('Введите новое описание товара: ', end='')
                        new_description = input()
                        products[product_choice].set_description(new_description)

                    case 12:
                        print('Введите новую массу товара: ', end='')
                        try:
                            new_weight = float(input())
                            products[product_choice].set_weight(new_weight)
                        except ValueError:
                            print('Ошибка: Введите корректное число.')
                        except NegativeNumberError as e:
                            print(f'Ошибка: {e}')

            case 2:
                products.append(Product())


main()
