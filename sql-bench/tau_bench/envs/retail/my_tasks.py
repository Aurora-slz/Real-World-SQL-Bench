from tau_bench.types import Task, Action

TASKS_TEST = [
    Task(
        user_id="yusuf_rossi_9620",
        instruction="You are Yusuf Rossi in 19122. You received your order #W2378156 and wish to exchange the mechanical keyboard for a similar one but with clicky switches and the smart thermostat for one compatible with Google Home instead of Apple HomeKit. If there is no keyboard that is clicky, RGB backlight, full size, you'd go for no backlight. You are detail-oriented and want to make sure everything is addressed in one go.",
        actions=[
            Action(
                name="sql",
                kwargs={
                "sql": "SELECT user_id FROM users WHERE first_name = 'Yusuf' AND last_name = 'Rossi' AND zip = '19122';"
                }
            ),
            Action(
                name="sql",
                kwargs={
                "sql": "SELECT * FROM orders WHERE order_id = '#W2378156';"
                }
            ),
            Action(
                name="sql",
                kwargs={
                "sql": "SELECT * FROM products WHERE product_id = '1656367028';"
                }
            ),
            Action(
                name="sql",
                kwargs={
                "sql": "SELECT * FROM products WHERE product_id = '4896585277';"
                }
            ),
            Action(
                name="sql",
                kwargs={
                "sql": "INSERT INTO exchanges (order_id, old_item_id, new_item_id, payment_method_id, timestamp) VALUES ('#W2378156', '1151293680', '7706410293', 'credit_card_9513926', CURRENT_TIMESTAMP), ('#W2378156', '4983901480', '7747408585', 'credit_card_9513926', CURRENT_TIMESTAMP);"
                }
            )
        ],
        outputs=[]
    )
]