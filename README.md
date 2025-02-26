# SauceDemo Automated Tests

Этот репозиторий содержит автотесты для сайта [SauceDemo](https://www.saucedemo.com/) с использованием Python 3.10+, Selenium и pytest.

## Описание тестов

- **test_login**: Проверка возможности входа зарегистрированного пользователя.
- **test_logout**: Проверка возможности выхода из системы для залогиненного пользователя.

## Дополнительные возможности

- **Выбор браузера и версии**: При запуске тестов можно указать браузер и его версию.
  - Пример: `pytest --browser=firefox --browser-version=102.0`
- **Запуск на Selenoid**: Для удалённого запуска тестов добавьте параметр `--remote`. Убедитесь, что Selenoid запущен и настроен.
- **Генерация Allure-отчёта**: Результаты тестового прогона сохраняются для Allure.

## Требования

- Python 3.10+
- Браузер (Chrome или Firefox)
- Соответствующий драйвер (ChromeDriver для Chrome или GeckoDriver для Firefox)

## Установка

### Для Windows

Клонировать репозиторий

   ```bash
   cd sauce_demo_test
   ```
   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate
   ```
   ```bash
   pip install -r requirements.txt
   ```
### Для Linux

Клонировать репозиторий
  ```bash
  cd sauce_demo_test
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
